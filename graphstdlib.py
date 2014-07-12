#!/usr/bin/env python

from pybuiltingrapher import graph
import argparse
import json

modules = {
  "math" : "Modules/mathmodule.c",
  "cmath" : "Modules/cmathmodule.c"
}

# Command Line invocation
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C.")
  parser.add_argument("cpythondir", help="The root directory of the CPython repository. Should have a Modules folder in it.")
  args = parser.parse_args()

  symbols = []
  docs = []
  refs = []

  for module,filename in modules.items():
    module_symbols, module_docs, module_refs = graph(module, args.cpythondir, filename)
    symbols.extend(module_symbols)
    docs.extend(module_docs)
    refs.extend(module_refs)

  print json.dumps({
    "Symbols" : symbols,
    "Docs" : docs,
    "Refs" : refs
  })
