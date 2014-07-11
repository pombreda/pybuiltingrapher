import argparse
import re
import json
import importlib
import inspect
import copy

from regexes import *

Unit = "Python"
UnitType = "PipPackage"

def recursable(live_object):
  '''Helper function to determine if an object
  should be recursed into during inspection. Currently
  only modules and classes.'''
  return inspect.ismodule(live_object)

def exportable(live_object):
  return inspect.ismodule(live_object) or inspect.isroutine(live_object)

def get_kind(live_object):
  if inspect.ismodule(live_object):
    return "module"
  if inspect.isroutine(live_object):
    return "func"

def is_callable(live_object):
  if inspect.ismodule(live_object):
    return False
  if inspect.isroutine(live_object):
    return True

def data_field(live_object):
  data = {}
  if inspect.ismodule(live_object):
    data['Kind'] = "module"
    data['FuncSignature'] = ""
  if inspect.isroutine(live_object):
    data['Kind'] = "function"
    data['FuncSignature'] = ""
  return data

def graph(module_name, filename):
  common = {
    "UnitType" : UnitType,
    "Unit" : Unit,
    "File" : filename
  }
  # Load source file
  code = "" if filename == None else open(filename).read()

  module = importlib.import_module(module_name)

  symbols = []
  docs = []

  def analyze(path, name, live_object):
    # If this is not a supported type of symbol, return
    if not exportable(live_object): return

    # Create Symbol
    symbol = copy.deepcopy(common)
    symbol.update({
      "Kind" : get_kind(live_object),
      "Name" : name,
      "DefStart" : 0,
      "DefEnd" : 0,
      "Callable" : is_callable(live_object),
      "Exported" : True,
      "Path" : path,
      "Data" : data_field(live_object),
      "TreePath" : path
    })
    symbols.append(symbol)

    # Create Doc
    doc = copy.deepcopy(common)
    doc.update({
      "End" : 0,
      "Format" : "text/plain",
      "Start" : 0,
      "Path" : path,
      "Data" : inspect.getdoc(live_object),
    })
    docs.append(doc)

    if recursable(live_object):
      for member in inspect.getmembers(live_object):
        analyze(path + "/" + member[0], member[0], member[1])

  analyze(module_name, module_name, module)

  print json.dumps(symbols, indent=1)
  print json.dumps(docs, indent=1)

# Command Line invocation
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C.")
  parser.add_argument('-m', '--module', type=str, help="The name of the module, eg: math, cmath, or gc.")
  parser.add_argument('-s', '--source', type=str, help="The C source for the module. This will allow the grapher to try and find line numbers, though this is merely an optional heuristic.")

  args = parser.parse_args()
  graph(args.module, args.source)
