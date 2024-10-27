print("Variables\n")

name = full_name = 'Luan'

print("Consider the variables name = full_name =", name)

name = 30

print('Python is not statically type, so i can say that my name now is:', name)
print("But full_name stil is:", full_name)

print("""
Python is a highly object-oriented language, every item of data in a
Python program is an object of a specific type or class.
""")

print('name:', name, 'as:', type(name))

name = 'Luan'

print('name:', name, 'as:', type(name))

print("""
A Python variable is a symbolic name that is a reference or pointer to
an object. Once an object is assigned to a variable, you can refer to the
object by that name. But the data it self is still contained within the object
""")

print("so m = 300 and n = m are two variables that point to the same object.")

print("""
Python is garbage collected, so when the number of pointers to an
object drops to zero, the allocated memory will be reclaimed.
""")

print("""Object Identity:
Every object that is created is given a number that uniquely identifies it. it
is guaranteed that no two objects will have the same identifier during any
period in which their lifetimes overlap.

The id() function returns an object's identifier:""")

m = 300

print('m:', m)

n = m

print('m = n, n:', n)

print('id(n)', id(n))
print('id(m)', id(m))

print("""
The id's are equals because these variables point to the same object
""")

n = 400

print("if we update n value:", n)

print("Then, id(m):", id(m), "and id(n):", id(n))

print("""
For purposes of optimization, the interpreter creates objects for the integers
in the range [-5, 256] at startup, and then reuses them during program
execution. Thus, when you assign separate variables to an integer value in this
range, they will actually reference the same object.
""")

x = 30
y = 30

print("x = 30, y = 30")

print("id(x):", id(x), "and id(y):", id(y))

print("""
Naming
Accordingly to PEP 8:
Snake Case should be used for functions and variable names.
Pascal Case should be used for class names. (e.g. CapWords).
""")
