## Sample Invocation
`python modulegrapher.py ../cpython/Modules/mathmodule.c`

## Sample Output (math module)
```
math
This module is always available.  It provides access to the
mathematical functions defined by the C standard.

##### Methods #####
{'docstring': 'pow(x, y)\\n\\nReturn x**y (x to the power of y).', 'range': '64369-64432', 'type': 'METH_VARARGS', 'name': 'pow', 'cfunction': 'math_pow'}
{'docstring': 'fsum(iterable)\\n\\n\\\nReturn an accurate floating point sum of values in the iterable.\\n\\\nAssumes IEEE-754 floating point arithmetic.', 'range': '63421-63485', 'type': 'METH_O', 'name': 'fsum', 'cfunction': 'math_fsum'}
{'range': '62620-62684', 'type': 'METH_O', 'name': 'cosh', 'cfunction': 'math_cosh'}
{'docstring': 'ldexp(x, i)\\n\\n\\\nReturn x * (2**i).', 'range': '63861-63926', 'type': 'METH_VARARGS', 'name': 'ldexp', 'cfunction': 'math_ldexp'}
{'docstring': 'hypot(x, y)\\n\\nReturn the Euclidean distance, sqrt(x*x + y*y).', 'range': '63566-63631', 'type': 'METH_VARARGS', 'name': 'hypot', 'cfunction': 'math_hypot'}
{'range': '61965-62030', 'type': 'METH_O', 'name': 'acosh', 'cfunction': 'math_acosh'}
{'range': '64730-64793', 'type': 'METH_O', 'name': 'tan', 'cfunction': 'math_tan'}
{'range': '62038-62102', 'type': 'METH_O', 'name': 'asin', 'cfunction': 'math_asin'}
{'docstring': 'isnan(x) -> bool\\n\\n\\\nReturn True if x is a NaN (not a number), and False otherwise.', 'range': '63788-63853', 'type': 'METH_O', 'name': 'isnan', 'cfunction': 'math_isnan'}
{'docstring': 'log(x[, base])\\n\\n\\\nReturn the logarithm of x to the given base.\\n\\\nIf the base not specified, returns the natural logarithm (base e) of x.', 'range': '64008-64071', 'type': 'METH_VARARGS', 'name': 'log', 'cfunction': 'math_log'}
{'range': '63054-63118', 'type': 'METH_O', 'name': 'fabs', 'cfunction': 'math_fabs'}
{'docstring': 'floor(x)\\n\\nReturn the floor of x as an int.\\n"\n             "This is the largest integral value <= x.', 'range': '63203-63268', 'type': 'METH_O', 'name': 'floor', 'cfunction': 'math_floor'}
{'range': '62328-62393', 'type': 'METH_O', 'name': 'atanh', 'cfunction': 'math_atanh'}
{'docstring': 'modf(x)\\n"\n"\\n"\n"Return the fractional and integer parts of x.  Both results carry the sign\\n"\n"of x and are floats.', 'range': '64297-64361', 'type': 'METH_O', 'name': 'modf', 'cfunction': 'math_modf'}
{'range': '64658-64722', 'type': 'METH_O', 'name': 'sqrt', 'cfunction': 'math_sqrt'}
{'range': '63934-64000', 'type': 'METH_O', 'name': 'lgamma', 'cfunction': 'math_lgamma'}
{'docstring': 'frexp(x)\\n"\n"\\n"\n"Return the mantissa and exponent of x, as pair (m, e).\\n"\n"m is a float and e is an int, such that x = m * 2.**e.\\n"\n"If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.', 'range': '63348-63413', 'type': 'METH_O', 'name': 'frexp', 'cfunction': 'math_frexp'}
{'docstring': 'degrees(x)\\n\\n\\\nConvert angle x from radians to degrees.', 'range': '62692-62759', 'type': 'METH_O', 'name': 'degrees', 'cfunction': 'math_degrees'}
{'docstring': 'log10(x)\\n\\nReturn the base 10 logarithm of x.', 'range': '64152-64217', 'type': 'METH_O', 'name': 'log10', 'cfunction': 'math_log10'}
{'range': '64515-64578', 'type': 'METH_O', 'name': 'sin', 'cfunction': 'math_sin'}
{'range': '62110-62175', 'type': 'METH_O', 'name': 'asinh', 'cfunction': 'math_asinh'}
{'docstring': 'log2(x)\\n\\nReturn the base 2 logarithm of x.', 'range': '64225-64289', 'type': 'METH_O', 'name': 'log2', 'cfunction': 'math_log2'}
{'range': '62910-62973', 'type': 'METH_O', 'name': 'exp', 'cfunction': 'math_exp'}
{'range': '62183-62247', 'type': 'METH_O', 'name': 'atan', 'cfunction': 'math_atan'}
{'docstring': 'factorial(x) -> Integral\\n"\n"\\n"\n"Find x!. Raise a ValueError if x is negative or non-integral.', 'range': '63126-63195', 'type': 'METH_O', 'name': 'factorial', 'cfunction': 'math_factorial'}
{'range': '62473-62541', 'type': 'METH_VARARGS', 'name': 'copysign', 'cfunction': 'math_copysign'}
{'range': '62981-63046', 'type': 'METH_O', 'name': 'expm1', 'cfunction': 'math_expm1'}
{'docstring': 'ceil(x)\\n\\nReturn the ceiling of x as an int.\\n"\n             "This is the smallest integral value >= x.', 'range': '62401-62465', 'type': 'METH_O', 'name': 'ceil', 'cfunction': 'math_ceil'}
{'docstring': 'isinf(x) -> bool\\n\\n\\\nReturn True if x is a positive or negative infinity, and False otherwise.', 'range': '63715-63780', 'type': 'METH_O', 'name': 'isinf', 'cfunction': 'math_isinf'}
{'range': '64586-64650', 'type': 'METH_O', 'name': 'sinh', 'cfunction': 'math_sinh'}
{'docstring': 'trunc(x:Real) -> Integral\\n"\n"\\n"\n"Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.', 'range': '64873-64938', 'type': 'METH_O', 'name': 'trunc', 'cfunction': 'math_trunc'}
{'range': '62549-62612', 'type': 'METH_O', 'name': 'cos', 'cfunction': 'math_cos'}
{'range': '64801-64865', 'type': 'METH_O', 'name': 'tanh', 'cfunction': 'math_tanh'}
{'docstring': 'radians(x)\\n\\n\\\nConvert angle x from degrees to radians.', 'range': '64440-64507', 'type': 'METH_O', 'name': 'radians', 'cfunction': 'math_radians'}
{'range': '62255-62320', 'type': 'METH_VARARGS', 'name': 'atan2', 'cfunction': 'math_atan2'}
{'range': '62767-62830', 'type': 'METH_O', 'name': 'erf', 'cfunction': 'math_erf'}
{'range': '62838-62902', 'type': 'METH_O', 'name': 'erfc', 'cfunction': 'math_erfc'}
{'docstring': 'fmod(x, y)\\n\\nReturn fmod(x, y), according to platform C."\n"  x % y may differ.', 'range': '63276-63340', 'type': 'METH_VARARGS', 'name': 'fmod', 'cfunction': 'math_fmod'}
{'range': '61893-61957', 'type': 'METH_O', 'name': 'acos', 'cfunction': 'math_acos'}
{'range': '64079-64144', 'type': 'METH_O', 'name': 'log1p', 'cfunction': 'math_log1p'}
{'docstring': 'isfinite(x) -> bool\\n\\n\\\nReturn True if x is neither an infinity nor a NaN, and False otherwise.', 'range': '63639-63707', 'type': 'METH_O', 'name': 'isfinite', 'cfunction': 'math_isfinite'}
{'range': '63493-63558', 'type': 'METH_O', 'name': 'gamma', 'cfunction': 'math_gamma'}

##### Objects #####
{'symbol': 'pi', 'range': '65448-65473'}
{'symbol': 'e', 'range': '65513-65537'}
```
