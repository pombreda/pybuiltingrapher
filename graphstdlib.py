#!/usr/bin/env python

from pybuiltingrapher import graph
from pybuiltingrapher.stdlib_modules import modules

import argparse
import json

# Command Line invocation
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C.")
  parser.add_argument("cpythondir", help="The root directory of the CPython repository. Should have a Modules folder in it.")
  parser.add_argument("--skipinternal", help="Include modules whose names start with an underscore.", action="store_true")
  args = parser.parse_args()

  symbols = []
  docs = []
  refs = []

  for module,filename in modules.items():
    #If skipinternal flag was not passed, skip modules starting with an underscore
    if args.skipinternal and module[0] == "_":
      continue
      
    try:
      module_symbols, module_docs, module_refs = graph(module, args.cpythondir, filename)
    except:
      # If error occured, simple ignore module
      pass
    else:
      symbols.extend(module_symbols)
      docs.extend(module_docs)
      refs.extend(module_refs)

  print(json.dumps({
    "Symbols" : symbols,
    "Docs" : docs,
    "Refs" : refs
  }))
