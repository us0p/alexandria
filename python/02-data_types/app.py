print("Data Types\n")

print("Text => luan:", type('luan'))

print("""
Numeric types:
""")
print("Integer => 0:", type(0))
print("Float => 0.0:", type(0.0))
print("Complex => 1j:", type(1j))

print("""
Sequence types:
""")
print("List => ['apple', 'banana']:", type(['apple', 'banana']))
print("Tuple => ('apple', 'banana'):", type(('apple', 'banana')))
print("range => range(2):", type(range(2)))

print("""
Mapping types:
""")
print("Dict => {'name': 'Luan'}:", type({'name': 'Luan'}))

print("""
Set types:
""")
print("Set => {'apple', 'banana'}:", type({'apple', 'banana'}))
print("FrozenSet => frozenset({'apple', 'banana'}):", type(
    frozenset({'apple', 'banana'})))

print("\nBoolean => True:", type(True))

print("""
Binary types:
""")
print("Bytes => b'Hello':", type(b'Hello'))
print("ByteArray => bytearray(5):", type(bytearray(5)))
print("MemoryView => memoryview(bytes(5)):", type(memoryview(bytes(5))))

print("\nNone => None:", type(None))

print("""
Look at the code for more examples in setting these values
""")

x = str("Hello, World")

x = int(20)

x = float(20.5)

x = complex(1j)

x = list(("apple", "banana"))

x = tuple(("apple", "banana"))

x = range(5)

x = dict(name="John", age=36)

x = set(("apple", "banana"))

x = frozenset(("apple", "banana"))

x = bool(5)

x = bytes(5)

x = bytearray(5)

x = memoryview(bytes(5))
