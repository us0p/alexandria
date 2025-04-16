# Import related attributes on module objects
When a module is created using the machinery associated with the import system, these attributes are filled in based on the module's spec, before the loader executes and loads the module.

## `__name__`
The name used to uniquely identify the module in the import system. For a directly executed module, this will be set to `"__main__"`.

## `__file__`
Are both optional attributes that may or may not be set. Both attributes should be a `str` when they are available.

It indicates the path name of the file from which the module was loaded (if loaded from a file), or the path name of the shared library file for extension modules loaded dynamically from a shared library.

It might be missing for certain types of modules, such as C modules that are statically linked into the interpreter, and the import system may opt to leave it unset if it has no semantic meaning (for example, a module loaded from a database).