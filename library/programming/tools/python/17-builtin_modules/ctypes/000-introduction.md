# ctypes
Foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

`ctypes` exports the `cdll`, and on Windows `windll` and `oledll` objects, for loading dynamic link libraries.

You load libraries by accessing them as attributes of these objects.
- `cdll` loads libraries which export functions using the standard `cdecl` calling convention.
- `windll` libraries call functions using the `stdcall` calling convention.
- `oledll` also uses the `stdcall` convention, and assumes the functions return a Windows `HRESULT` error code. Which is used to automatically raise an `OSError` exception when the function call fails.

On Linux, it is required to specify the filename including the extension to load a library. Either the `LoadLibrary()` method of the `dll` loaders should be used, or you should load the library by creating an instance of `CDLL`:
```python
from ctypes import *

# Windows
win_libc = windll.kernel32

also_win_libc = cdll.msvcrt

# Linux
# In linux is required to specify the filename including the extension.
# Attribute access can not be used to load libraries.
libc = cdll.LoadLibrary("libc.so.6")

also_libc = CDLL("libc.so.6")
```
>`msvcrt` is the MS standard C library and uses the `cdecl` calling convention.

>Accessing the standard C library through `cdll.msvcrt` will use an outdated version of the library that may be incompatible with the one being used by Python. Where possible, use native Python functionality, or import and use the `msvcrt` module.
## Accessing functions from loaded `dlls`
Functions are accessed as attributes of `dll` objects
```python
from ctypes import *

libc = cdll.LoadLibrary("libc.so.6")

printf = libc.printf
```
>`win32` systems `dlls` like `kernel32` and `user32` often export ANSI as well as UNICODE versions of a function. The UNICODE version is exported with a `W` appended to the name, while the ANSI version is exported with an `A` appended to the name. `windll` does not try to select one of them by magic, you must specify the version.

Sometimes, `dlls` export functions with names which aren't valid Python identifiers, like `??2@YAPAXI@Z`. In this case you have to use `getattr()` to retrieve the function:
```python
from ctypes import *

crazy_fn = getattr(cdll.msvcrt, "??@YAPAXI@Z")
```

On Windows, some `dlls` export functions not by name but by ordinal. These functions can be accessed by indexing the `dll` object with the ordinal number:
```python
from ctypes import *

more_crazy_fn = cdll.kernel32[1]
```
## Calling functions
You can call these functions like any other Python callable.
```python
from ctypes import *

libc = cdll.LoadLibrary("libc.so.6")

# prints some randon number
print(libc.rand())
```

On Windows, you can cal the `GetModuleHandleA()` function, which returns a `win32` module handle passing `None` as a single argument to call it with a `NULL` pointer.

To find out the correct calling convention you have to look into the C header file or the documentation for the function you want to call.

On Windows, `ctypes` uses `win32` structured exception handling to prevent crashes from general protection faults when functions are called with invalid arguments values.

The `faulthandler` module can be helpful in debugging crashes e.g. from segmentation faults produced by erroneous C library calls.

`None`, integers, bytes objects and (unicode) strings are the only native Python objects that can directly be used as parameters in these function calls.
`None` is passed as a C `NULL` pointer, bytes objects and string are passed as pointer to the memory block that contains their data. Python integers are passed as the platform's default C `int` type, their value is masked to fir into the C type.
## Fundamental data types
| ctypes type  | C type                                                                                          | Python type              |
| ------------ | ----------------------------------------------------------------------------------------------- | ------------------------ |
| c_bool       | _Bool                                                                                           | bool)                    |
| c_char       | char                                                                                            | 1-character bytes object |
| c_wchar      | `wchar_t`                                                                                       | 1-character string       |
| c_byte       | char                                                                                            | int                      |
| c_ubyte      | unsigned char                                                                                   | int                      |
| c_short      | short                                                                                           | int                      |
| c_ushort     | unsigned short                                                                                  | int                      |
| c_int        | int                                                                                             | int                      |
| c_uint       | unsigned int                                                                                    | int                      |
| c_long       | long                                                                                            | int                      |
| c_ulong      | unsigned long                                                                                   | int                      |
| c_longlong   | __int64 or long long                                                                            | int                      |
| c_ulonglong  | unsigned __int64 or unsigned long long                                                          | int                      |
| c_size_t     | `size_t`                                                                                        | int                      |
| c_ssize_t    | `ssize_t` or [Py_ssize_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | int                      |
| c_time_t     | `time_t`                                                                                        | int                      |
| c_float      | float                                                                                           | float                    |
| c_double     | double                                                                                          | float                    |
| c_longdouble | long double                                                                                     | float                    |
| c_char_p     | char* (NUL terminated)                                                                          | bytes object or `None`   |
| c_wchar_p    | wchar_t* (NUL terminated)                                                                       | string or `None`         |
| c_void_p     | void*                                                                                           | int or `None`            |

All these types can be created by calling them with an optional initialized of the correct type and value:
```python
from ctypes import *

string = c_wchar_p("Hello, World")

# Since these types are mutable:
string.value = "It's good to be here!"

```
 
Note that assigning value to instances of the pointer types `c_char_p`, `c_wchar_p`, and `c_void_p` changes the memory location they point to, not the contents of the memory block.

You should not pass them to functions expecting pointer to mutable memory. If you need mutable memory blocks, `ctypes` has a `create_string_buffer()` which creates these in various ways.
```python
from ctypes import *

# create a 3 byte buffer, initialized to NULL
p = create_string_buffer(3) 

# is the size of the buffer
p.size # 3

# is the raw data of the buffer 
p.raw # b'\x00\x00\x00'

# Strings are NULL terminated
p = create_string_buffer(b"Hello")
p.size # 6
p.raw # b'Hello\x00'

# You can also create a buffer with some extra space
p = create_string_buffer(b"Hello", 10)
p.size # 10
p.value # b'Hello\x00\x00\x00\x00\x00'
```

To create a mutable memory block containing unicode characters of the C type `wchar_t`, use the `create_unicode_buffer()`.

Functions that redirect some output to some standard stream channel (`std in, out, err`), not to `sys.stdout` only provide the expected output at the console prompt, not from within `IDLE`.
All Python types, except integers, string, and bytes objects have to be wrapped in their corresponding `ctypes` type, so that they can be converted to the required C data type:
```python
from ctypes import *

libc = cdll.LoadLibrary("libc.so.6")

libc.printf(
	b"An int %d, a double %f\n",
	1234,
	c_double(3.14)
) # An int 1234, a double 3.140000
```
## Calling variadic functions
On a lot platforms calling variadic functions through `ctypes` is exactly the same as calling functions with a fixed number of parameters. On some platforms, the calling convention for variadic functions is different than that for regular functions.
On those platforms, it is required to specify the `argtypes` attribute for the regular, non-variadic, functions arguments:
```python
from c types import *

libc = cdll.LoadLibrary("libc.so.6")

libc.printf.argtypes = [c_char_p]
```

>Because specifying the attribute does not inhibit portability it is advised to always specify `argtypes` for all variadic functions.
## Calling functions with your own custom data types
`ctypes` looks for an `_as_parameter_` attribute and uses this as function argument. The attribute must be an integer, string, bytes, a `ctypes` instance, or an object with an `_as_parameter_` attribute:
```python
from ctypes import *

libc = cdll.LoadLibrary("libc.so.6")

class Bottles:
	def __init__(self, number):
		self._as_parameter_ = number

bottles = Bottles(42)
libc.printf(b"%d bottles of beer\n", bottles)
# 42 bottles of beer
```