print("""
Binary Sequence Types:
""")

print("""
The core built-in types for manipulating binary data are bytes and bytearray.
They are supported by memoryview which uses the buffer protocol to access the
memory of other binary objects without needing to make a copy.
""")

print("""Bytes Objects:
Bytes objects are immutable sequences of single bytes.
Only ASCII characters are permitted in bytes literals (<b'...'>, regardless
of the declared source code encoding). Any values over 127 must be entered
into bytes literals using the appropriate escape sequence.
""")

print("bytes(10):", bytes(10))

print("bytes('asdf', 'utf-8'):", bytes("asdf", 'utf-8'))

print("""
Bytearray Objects:
""")

print("""
bytearray objects are a mutable conterpart to bytes objects.
""")

print("bytearray(10):", bytearray(10))
print("bytearray(b'Hi!', bytearray(b'Hi!')):", bytearray(b'Hi!'))

print("""
As bytearray objects are mutable, they support the mutable sequence operations
in addition to the common bytes and bytearray operations.
""")

print("""Since 2 hexadecimal digits correspond precisely to a single byte,
hexadecimal numbers are a commonly used format to describing binary data.
""")

print("""
Since bytes and bytearray objects are sequences of integers (akin to a tuple),
for a bytes or bytearray object b, b[0] will be an integer, while b[0:1] will
be a bytes or bytearray object of lenght 1.
""")

print("""
Memory Views:
""")

print("""
memoryview objects allow Python code to access the internal data of an object
that supports the buffer protocol without copying.
""")

print("memoryview(b'Hi!'):", memoryview(b'Hi!'))

print("""
The provided object must support the buffer protocol. Built-in objects that
support the buffer  protocol include bytes and bytearray.
""")

print("""
A memoryview has the notion of an element, which is the atomic memory unit
handled by the originating object. For many simple types such as bytes and
bytearray, an element is a single byte, but other types such as array.array
may have bigger elements.
""")

print("""
A memoryview supoprts slicing and indexing to expose its data. One-dimensional
slicing will result in a subview:
""")

v = memoryview(b'abcefg')

print('v:', v)

print('v[1]:', v[1])

print('v[-1]:', v[-1])

print('v[1:4]:', v[1:4])

print('bytes(v[1:4]):', bytes(v[1:4]))
