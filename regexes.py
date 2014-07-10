import re

PyModuleDef = re.compile("""
static\s*struct\s*PyModuleDef\s*([\w]*)\s*=\s*{
\s*PyModuleDef_HEAD_INIT*\s*,
\s*"(.*)",
\s*(\w*),
\s*\S*,
\s*(\w*),
\s*\S*,
\s*\S*,
\s*\S*,
\s*\S*
\s*};
""",re.VERBOSE)

PyDoc_STRVAR = re.compile("""
PyDoc_STRVAR\(\s*
(\w*)\s*,
\s*"
((?:\\"|.)*?) #Will only match the inside of the string
"\);
""", re.VERBOSE | re.DOTALL)

PyModule_Create = re.compile("""
(\w*)\s*=\s*PyModule_Create\(&(\w*)\);
""", re.VERBOSE)

PyMethodDef = re.compile("""
static\s*PyMethodDef\s*(\w*)\[\]\s*=\s*{
(.*)
{\s*NULL\s*,\s*NULL\s*}
""", re.VERBOSE | re.DOTALL)

# TODO
PyModule_AddObject = re.compile("""
PyModule_AddObject\(
\s*
(?P<module>\w*)
\s*,
\s*"
(?P<symbol>\w*)
""", re.VERBOSE)

# TODO
MATHMACRO_FUNC1 = re.compile("""
""", re.VERBOSE | re.DOTALL)
