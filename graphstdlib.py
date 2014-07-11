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
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C. Invoke in the root directory of the CPython repository.")
  args = parser.parse_args()

  symbols = []
  docs = []

  for module,filename in modules.items():
    module_symbols, module_docs = graph(module, filename)
    symbols.extend(module_symbols)
    docs.extend(module_docs)

  print json.dumps({
    "Symbols" : symbols,
    "Docs" : doc
  })
