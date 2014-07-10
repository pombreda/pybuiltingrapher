import argparse
import re
import shlex

from regexes import *

# Command Line arguments
parser = argparse.ArgumentParser(description="Naive grapher for modules in python standard lib, written in C.")
parser.add_argument('files', metavar='N', type=str, nargs='+',
                   help='.c modules to parse')
args = parser.parse_args()

for filename in args.files:
  code = open(filename).read()

  def rangeFor(segment):
    start = code.find(segment)
    end = start + len(segment)
    return str(start) + "-" + str(end)

  def mergeDocstring(docstring):
    linemerge = "".join(re.split('"\s*\n\s*"', docstring))
    return linemerge.replace("\\n", "\n")

  objects_by_module = {}
  for match in PyModule_AddObject.finditer(code):
    if match.groupdict()['module'] not in objects_by_module:
      objects_by_module[match.groupdict()['module']] = []

    object_table = {
      "symbol" : match.groupdict()['symbol'],
      "range" : str(match.start()) + "-" + str(match.end())
    }
    objects_by_module[match.groupdict()['module']].append(object_table)

  doc_strings = {}
  for match in PyDoc_STRVAR.findall(code):
    doc_strings[match[0]] = match[1]

  module_defs = {}
  for match in PyModuleDef.findall(code):
    module_defs[match[0]] = match

  created_modules = {}
  for match in PyModule_Create.findall(code):
    created_modules[match[0]] = match[1]

  method_tables = {}
  for match in PyMethodDef.findall(code):
    table = {}
    for line in re.split("},\s*{", match[1].strip().strip("{},")):
      words = line.split(",")

      method = {}
      method['name'] = words[0].strip().strip('"')
      method['cfunction'] = words[1].strip().strip('"')
      method['type'] = words[2].strip().strip('"')
      method['range'] = rangeFor(line)

      docstring_var = words[3].strip().strip('"')
      if docstring_var in doc_strings:
        method['docstring'] = doc_strings[docstring_var]

      table[method['name']] = method
    method_tables[match[0]] = table

  for module in created_modules:
    module_struct = created_modules[module]
    module_name = module_defs[module_struct][1]
    module_doc = doc_strings[module_defs[module_struct][2]]

    method_table = method_tables[module_defs[module_struct][3]]
    objects = objects_by_module[module]

    print module_name
    print mergeDocstring(module_doc)

    print "\n##### Methods #####"
    for method in method_table.values():
      print method

    print "\n##### Objects #####"
    for obj in objects:
      print obj
