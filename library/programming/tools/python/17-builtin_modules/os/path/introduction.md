This module implements some useful functions on path names. 
## Canonical Paths
A canonical path is a unique, absolute, and resolved representation of a file or directory path, essentially the "shortest" and most unambiguous way to refer to a file system object.

It is obtained by resolving symbolic links, removing redundant navigation components like "." and "..", and ensuring the path is absolute. 
## `path.dirname(path)`
Return the directory name of path name path
## `path.exists(path)`
Return `True` if path refers to an existing path or an open file descriptor. Returns `False` for broken symbolic links.

On some platforms, this function may return `False` if permission is not granted to execute `os.stat()` on the requested file, even if the path physically exists.
## `path.realpath(path)`
Return the canonical path of the specified filename, eliminating any symbolic links encountered in the path (if they are supported by the operating system).

If a path doesn’t exist or a symlink loop is encountered, and strict is `True`, `OSError` is raised. If strict is `False` these errors are ignored, and so the result might be missing or otherwise inaccessible.
## `path.join(path, *paths)`
Join one or more path segments intelligently. The return value is the concatenation of path and all members of *paths, with exactly one directory separator following each non-empty part, except the last
## Examples
```python
from os.path import dirname, exists, realpath, join

unix_path = "/home/user/projects/python/main.py"

print(dirname(unix_path)) # "/home/user/projects/python" 

print(exists(unix_path)) # True

new_path = unix_path + "/.."

print(realpath(new_path)) # "/home/user/projects/python"

print(join("home", "user")) # "home/user"
```