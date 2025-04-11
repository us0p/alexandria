## `pprint`
Provides capability of "pretty-print" arbitrary Python data structures in a form which can be used as input to the interpreter.

The formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don't fit within the allowed width, adjustable by the *width* parameter defaulting to 80 characters.

Dictionaries are sorted by key before the display is computed.
## `pp`
Prints the formatted representation of the received object, followed by a newline.
## `pprint`
Alias for `pp()` with `sort_dicts` set to `True` by default.