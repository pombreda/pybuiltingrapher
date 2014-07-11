import re

PyModuleDef = """
static\s*struct\s*PyModuleDef\s*
(?P<struct_name>\w*)\s*=\s*{
\s*PyModuleDef_HEAD_INIT\s*,
\s*"%s"\s*,
\s*(\w*)\s*,
\s*(\S*)\s*,
\s*(?P<method_table>\w*)\s*,
\s*(\w*)\s*,
\s*(\w*)\s*,
\s*(\w*)\s*,
\s*(\w*)\s*
};
"""

PyMethodDef = """
{\s*"%s"\s*,.*,.*,.*}
"""

PyModule_AddObject = """
PyModule_AddObject(.*,\s*"%s"\s*,.*);
"""

PyTypeObject = """
static\s*PyTypeObject\s*(\w*)\s*=\s*{
\s*PyVarObject_HEAD_INIT\(\s*NULL\s*,\s*0\s*\)\s*
"%s"\s*,\s*
"""
