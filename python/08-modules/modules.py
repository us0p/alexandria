# Module
# It's a file with definitions and statements which can be used as a script.

# The file name is the module name with the sufix ".py".
# Within a module, the module's name is available as __name__ global var.
# The __name__ for the entry point of your program is "__main__". This
# makes it possible to use the file as a script or a importable module.

# A module can contain executable statements. These statements are intended
# to initialize the module.
# They are executed only the first time the module name is encountered in an 
# import statement. (They are also run if the file is executed as a script.)

# The imported module names, if placed at the top level of a module 
# (outside any functions or classes), are added to the module’s global 
# namespace.

# Module search path
# When a module is imported, the interpreter first searches for a built-in
# module with that name. If not found, it then searcher for a file with
# the name of the module with the suffix ".py" in a list of directories
# given by the variable sys.path.
# One of those paths is the directory containing the input script (or the
# current directory when no file is specified).

# Packages
# Packages are a way of structuring Python’s module namespace by using 
# “dotted module names”. For example, the module name A.B designates a 
# submodule named B in a package named A.

# The __init__.py files are required to make Python treat directories 
# containing the file as packages. This prevents directories with a common 
# name, from unintentionally hiding valid modules that occur later on the 
# module search path. In the simplest case, __init__.py can just be an empty 
# file, but it can also execute initialization code for the package or set 
# the __all__ variable.

# Note that when using "from package import item", the item can be either a 
# submodule (or subpackage) of the package, or some other name defined in 
# the package, like a function, class or variable.

# Contrarily, when using syntax like "import item.subitem.subsubitem", each 
# item except for the last must be a package; the last item can be a module 
# or a package but can’t be a class or function or variable defined in the 
# previous item.

# Now what happens when we "import *"? It would take too much time to go 
# out to the filesystem and find which submodules are present in the 
# package to import them all.

# The solution is for the package author to provide an explicit index of 
# the package. If a package’s __init__.py code defines a list named
# __all__, it is taken to be the list of module names that should be 
# imported when from package import * is encountered. 
# It is up to the package author to keep this list up-to-date. 
# Package authors may also decide not to support it, if they don’t see a 
# use for importing * from their package.

# Be aware that locally defined names can shadow submodules * imports.

# Relative imports:
# For subpapckages modules you can use relative imports.
# These imports use leading dots to indicate the current and parent 
# packages involved in the relative import.
# main modules can't use relative imports.
