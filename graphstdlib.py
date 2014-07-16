#!/usr/bin/env python

from pybuiltingrapher import graph, create_fake
from pybuiltingrapher.stdlib_modules import modules

import argparse
import json
import sys
import os

# Command Line invocation
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C.")
  parser.add_argument("cpythondir", help="The root directory of the CPython repository. Should have a Modules folder in it.")
  parser.add_argument("--skipinternal", help="Include modules whose names start with an underscore.", action="store_true")

  parser.add_argument("--generatefakes", help="Creates fake .py modules that mimics the builtin - for tricking PySonar.", action="store_true")
  parser.add_argument("--fakesdir", help="Directory in which to place the fake py modules. Default: cpythondir/Fakes/", type=str, default=None)

  args = parser.parse_args()

  symbols = []
  docs = []
  refs = []

  # Setup directory for generating fakes
  if args.fakesdir == None:
    args.fakesdir = args.cpythondir + '/Fakes/'
  if args.generatefakes:
    if not os.path.exists(args.fakesdir):
      os.makedirs(args.fakesdir)

  for module,filename in modules.items():
    #If skipinternal flag was not passed, skip modules starting with an underscore
    if args.skipinternal and module[0] == "_":
      continue

    try:
      module_symbols, module_docs, module_refs = graph(module, args.cpythondir, filename)

      if args.generatefakes:
        f = open(args.fakesdir + module + ".py", 'w')
        f.write(create_fake(module))
        f.close()
    except:
      # If error occured, simply ignore module
      sys.stderr.write(str(sys.exc_info()) + "\n")
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
