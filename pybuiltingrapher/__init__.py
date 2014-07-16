import re
import importlib
import inspect
import copy

from pybuiltingrapher import regexes

Unit = "Python"
UnitType = "PipPackage"

def recursable(live_object):
  '''Helper function to determine if an object
  should be recursed into during inspection. Currently
  only modules and classes.'''
  return inspect.ismodule(live_object)

def find_location(path, name, live_object, code):
  '''Naive attempt to find location of object definition in C source file.'''
  if inspect.ismodule(live_object):
    # Find struct that defines the module
    PyModuleDef = re.compile(regexes.PyModuleDef % name, re.VERBOSE)
    match = PyModuleDef.search(code)
    if match:
      return match.start(), match.end()

  elif inspect.isroutine(live_object):
    # Find entry in method table
    PyMethodDef = re.compile(regexes.PyMethodDef % name, re.VERBOSE)
    match = PyMethodDef.search(code)
    if match:
      return match.start(), match.end()

  elif inspect.isclass(live_object):
    # Find PyTypeObject structs
    PyTypeObject = re.compile(regexes.PyTypeObject % (path.replace("/", ".")), re.VERBOSE)
    match = PyTypeObject.search(code)
    if match:
      return match.start(), match.end()

  else:
    # Look for a matching Add Object call
    PyModule_AddObject = re.compile(regexes.PyModule_AddObject % name, re.VERBOSE)
    match = PyModule_AddObject.search(code)
    if match:
      return match.start(), match.end()

  return 0,0

def exportable(name, live_object):
  '''Return True if this is a object that we want to export'''

  if re.match("__.*__", name): return False

  return (inspect.ismodule(live_object)
    or inspect.isroutine(live_object)
    or inspect.isclass(live_object)
    or type(live_object) is str
    or type(live_object) is float
    or type(live_object) is dict
    or type(live_object) is list
    or type(live_object) is int)

def get_kind(live_object):
  if inspect.ismodule(live_object):
    return "module"
  elif inspect.isroutine(live_object):
    return "func"
  elif inspect.isclass(live_object):
    return "type"
  else:
    return "var"

def is_callable(live_object):
  if inspect.ismodule(live_object):
    return False
  elif inspect.isroutine(live_object):
    return True
  elif inspect.isclass(live_object):
    return False
  else:
    False

def data_field(live_object):
  data = {}
  if inspect.ismodule(live_object):
    data['Kind'] = "module"
    data['FuncSignature'] = ""
  elif inspect.isroutine(live_object):
    data['Kind'] = "function"
    data['FuncSignature'] = ""
  elif inspect.isclass(live_object):
    data['Kind'] = "class"
    data['FuncSignature'] = ""
  else:
    data['Kind'] = "scope"
    data['FuncSignature'] = ""
  return data

def graph(module_name, rootdir, filename):
  '''Returns the sourcegraph formatted graph of the module, separated
  into Symbols, Docs, and Refs'''

  common = {
    "UnitType" : UnitType,
    "Unit" : Unit,
    "File" : filename
  }

  # Load source file
  code = ""
  try:
    code = open(rootdir + "/" + filename).read()
  except:
    # Continue, even if file could not be opened
    sys.stderr.write("Could not fild file " + rootdir + "/" + filename + "\n")

  module = importlib.import_module(module_name)

  symbols = []
  docs = []
  refs = []

  def analyze(path, name, live_object):
    # If this is not a supported type of symbol, return
    if not exportable(name, live_object): return

    start, end = find_location(path, name, live_object, code)

    # Create Symbol
    symbol = copy.deepcopy(common)
    symbol.update({
      "Kind" : get_kind(live_object),
      "Name" : name,
      "DefStart" : start,
      "DefEnd" : end,
      "Callable" : is_callable(live_object),
      "Exported" : True,
      "Path" : path,
      "Data" : data_field(live_object),
      "TreePath" : path
    })
    symbols.append(symbol)

    # Create identity reference for Symbol
    ref = copy.deepcopy(common)
    ref.update({
      "SymbolUnitType" : symbol['UnitType'],
      "SymbolUnit" : symbol['Unit'],
      "SymbolRepo" : "",
      "SymbolPath" : symbol['Path'],
      "Repo" : "",
      "Start" : start,
      "End" : end,
      "Def" : True
    })
    refs.append(ref)

    # Create Doc
    doc = copy.deepcopy(common)
    doc.update({
      "Start" : 0,
      "End" : 0,
      "Format" : "text/plain",
      "Path" : path,
      "Data" : inspect.getdoc(live_object),
    })
    docs.append(doc)

    if recursable(live_object):
      for member in inspect.getmembers(live_object):
        analyze(path + "/" + member[0], member[0], member[1])

  analyze(module_name, module_name, module)

  return symbols, docs, refs

def create_fake(module_name):
  '''Creates a fake .py module that happends to export the same symbols as the the given builtin module.'''
  module = importlib.import_module(module_name)

  def fake(object_name, live_object):
    # If this is not a supported type of symbol, return
    if not exportable(object_name, live_object): return None

    member_fakes = []
    if recursable(live_object):
      for member in inspect.getmembers(live_object):
        result = fake(member[0], member[1])
        if result != None:
          member_fakes.append(result)

    if type(live_object) is str:
      return object_name + " = 'fake'"
    elif type(live_object) is int:
      return object_name + " = 0"
    elif type(live_object) is float:
      return object_name + " = 0.0"
    elif type(live_object) is list:
      return object_name + " = []"
    elif type(live_object) is dict:
      return object_name + " = {}"
    elif inspect.ismodule(live_object):
      return "\n".join(member_fakes)
    elif inspect.isroutine(live_object):
      return "def %s(): return" % object_name
    elif inspect.isclass(live_object):
      indented = map(lambda x: "\t" + x, member_fakes) # Class members must be indented
      classbody = "\n".join(indented) if len(member_fakes) > 0 else "\tpass"
      return "class %s:\n%s" % (object_name, classbody)
    else:
      return ""

  return fake(module_name, module)
