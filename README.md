## Sample Invocation
`python modulegrapher.py -m math -s testdata/mathmodule.c`

## Sample Output (math module)
```json
{
  "Symbols": [
    {
      "Kind": "module",
      "Name": "math",
      "DefStart": 65146,
      "DefEnd": 65309,
      "Callable": false,
      "UnitType": "PipPackage",
      "Exported": true,
      "File": "testdata/mathmodule.c",
      "Path": "math",
      "Data": {
        "FuncSignature": "",
        "Kind": "module"
      },
      "TreePath": "math",
      "Unit": "Python"
    },
    {
      "Kind": "func",
      "Name": "acos",
      "DefStart": 61892,
      "DefEnd": 61958,
      "Callable": true,
      "UnitType": "PipPackage",
      "Exported": true,
      "File": "testdata/mathmodule.c",
      "Path": "math/acos",
      "Data": {
        "FuncSignature": "",
        "Kind": "function"
      },
      "TreePath": "math/acos",
      "Unit": "Python"
    },
    ...
  ],
  "Docs": [
    {
      "End": 65309,
      "Format": "text/plain",
      "Start": 65146,
      "UnitType": "PipPackage",
      "File": "testdata/mathmodule.c",
      "Path": "math",
      "Data": "This module is always available.  It provides access to the\nmathematical functions defined by the C standard.",
      "Unit": "Python"
    },
    ...
  ]
}

```
