Open file and return a corresponding file object. If the file cannot be opened, an `OSError` is raised.
## File mode
The `open()` function expects an optional mode string that represents in which mode the file will be opened. The default is `"r"` which means **open for reading in text mode**.

| Character | Meaning                                                         |
| --------- | --------------------------------------------------------------- |
| `'r'`     | open for reading (default)                                      |
| `'w'`     | open for writing, truncating (erasing) the file first           |
| `'x'`     | open for exclusive creation, failing if the file already exists |
| `'a'`     | open for writing, appending to the end of file if it exists     |
| `'b'`     | binary mode                                                     |
| `'t'`     | text mode (default)                                             |
| `'+'`     | open for updating (reading and writing)                         |
The default mode `"r"` is a synonym of `"rt"`.

Files opened in binary mode return contents as bytes objects without any decoding. In text mode, the contents of the file are returned as `str`

The type of file object returned by the `open()` function depends on the mode.

When `open()` is used to open a file in a text mode (`'w', 'r', 'wt', 'rt'`, etc.), it returns a subclass of `io.TextIOBase` (specifically `io.TextIOWrapper`).

When used to open a file in a binary mode with buffering, the returned class is a subclass of `io.BufferedIOBase`. The exact class varies