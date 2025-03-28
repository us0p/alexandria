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