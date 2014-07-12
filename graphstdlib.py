#!/usr/bin/env python

from pybuiltingrapher import graph
import argparse
import json

modules = {
  "math" : "Modules/mathmodule.c",
  "cmath" : "Modules/cmathmodule.c",
  "zlib" : "Modules/zlibmodule.c",
  "zibimport" : "Modules/zipimport.c",
  "unicodedata" : "Modules/unicodedata.c",
  "xxsubtype" : "Modules/xxsubtype.c",
  "time" : "Modules/timemodule.c",
  "termios" : "Modules/termios.c",
  "syslog" : "Modules/syslogmodule.c",
  "_symbtable" : "Modules/symtablemodule.c",
  "spwd" : "Modules/spwdmodule.c",
  "_socket" : "Modules/socketmodule.c",
  "_signal" : "Modules/signalmodule.c",
  "_sha512" : "Modules/sha512module.c",
  "_sha256" : "Modules/sha256module.c",
  "_sha1" : "Modules/sha1module.c",
  "select" : "Modules/selectmodule.c",
  "resource" : "Modules/resource.c",
  "readline" : "Modules/readline.c",
  "pyexpat" : "Modules/pyexpat.c",
  "pwd" : "Modules/pwdmodule.c",
  "posix" : "Modules/posixmodule.c",
  "parser" : "Modules/parsermodule.c",
  "_overlapped" : "Modules/overlapped.c",
  "ossaudiodev" : "Modules/ossaudiodev.c",
  "nis" : "Modules/nismodule.c",
  "mmap" : "Modules/mmapmodule.c",
  "_md5" : "Modules/md5module.c",
  "itertools" : "Modules/itertoolsmodule.c",
  "grp" : "Modules/grpmodule.c",
  "gc" : "Modules/gcmodule.c",
  "fpetest" : "Modules/fpetestmodule.c",
  "fpectl" : "Modules/fpectlmodule.c",
  "fcntl" : "Modules/fcntlmodule.c",
  "faulthandler" : "Modules/faulthandler.c",
  "errno" : "Modules/errnomodule.c",
  "binascii" : "Modules/binascii.c",
  "audioop" : "Modules/audioop.c",
  "atexit" : "Modules/atexitmodule.c",
  "array" : "Modules/arraymodule.c",
  "_winapi" : "Modules/_winapi.c",
  "_weakref" : "Modules/_weakref.c",
  "_tracemalloc" : "Modules/_tracemalloc.c",
  "_tkinter" : "Modules/_tkinter.c",
  "_pickle" : "Modules/_pickle.c",
  "_datetime" : "Modules/_datetimemodule.c",
  "_bisect" : "Modules/_bisectmodule.c",
  "_bz2" : "Modules/_bz2module.c",
  "_codecs" : "Modules/_codecsmodule.c",
  "_collections" : "Modules/_collectionsmodule.c",
  "_crypt" : "Modules/_cryptmodule.c",
  "_csv" : "Modules/_csv.c",
  "_curses_panel" : "Modules/_curses_panel.c",
  "_curses" : "Modules/_cursesmodule.c",
  "_dbm" : "Modules/_dbmmodule.c",
  "_elementtree" : "Modules/_elementtree.c",
  "_thread" : "Modules/_threadmodule.c",
  "_testimportmultiple" : "Modules/_testimportmultiple.c",
  "_testcapi" : "Modules/_testcapimodule.c",
  "_testbuffer" : "Modules/_testbuffer.c",
  "_struct" : "Modules/_struct.c",
  "_stat" : "Modules/_stat.c",
  "_sre" : "Modules/_sre.c",
  "_ssl" : "Modules/_ssl.c",
  "_scproxy" : "Modules/_scproxy.c",
  "_random" : "Modules/_randommodule.c",
  "_posixsubprocess" : "Modules/_posixsubprocess.c",
  "_operator" : "Modules/_operator.c",
  "_opcode" : "Modules/_opcode.c",
  "_lzma" : "Modules/_lzmamodule.c",
  "_lsprof" : "Modules/_lsprof.c",
  "_locale" : "Modules/_localemodule.c",
  "_json" : "Modules/_json.c",
  "_heapq" : "Modules/_heapqmodule.c",
  "_hashlib" : "Modules/_hashopenssl.c",
  "_gdbm" : "Modules/_gdbmmodule.c",
  "_functools" : "Modules/_functoolsmodule.c",
  "_sqlite3" : "Modules/_sqlite/module.c",
  "_multiprocessing" : "Modules/_multiprocessing/multiprocessing.c",
  "io" : "Modules/_io/_iomodule.c",
  "decimal" : "Modules/_decimal/_decimal.c",
  "_ctypes" : "Modules/_ctypes/_ctypes.c",
  "_ctypes_test" : "Modules/_ctypes/_ctypes_test.c"
 }

# Command Line invocation
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grapher for modules in python standard lib, intended to be used for modules written in C.")
  parser.add_argument("cpythondir", help="The root directory of the CPython repository. Should have a Modules folder in it.")
  args = parser.parse_args()

  symbols = []
  docs = []
  refs = []

  #TODO - add option to ignore modules starting with an underscore

  for module,filename in modules.items():
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
