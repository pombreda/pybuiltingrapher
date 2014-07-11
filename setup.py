from setuptools import setup

setup(
  name = "PyBuiltinGrapher",
  version = "0.1",
  url = 'http://github.com/sourcegraph/pybuiltingrapher',
  packages=['pybuiltingrapher'],
  description = "Tool for exporting symbols of python standard lib built-ins.",
  scripts = ['graphstdlib.py'],
  author = "Varun Ramesh",
  zip_safe = False
)
