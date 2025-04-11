# `sys.argv`
It's the list of command line arguments passed to a Python script.

```python
import sys

sys.argv[0] # script name, depending on the OS, might be full path name or not.
```

> On Unix, command line arguments are passed by bytes from OS. Python decodes them with filesystem encoding and `"surrogateescape"` error handler. When you need original bytes, you can get it by `[os.fsencode(arg) for arg in sys.argv]`