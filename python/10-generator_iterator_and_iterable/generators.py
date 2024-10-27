# Generators
# Generator objects are iterators.

# Generator function
# Is a function that contains a yield statement. This makes the function
# produce a generator object.
print("Generator fn")
def square(length: int):
    for n in range(length):
        yield n ** 2

type(square(3)) # generator

for n in square(3):
    print(n)

# Generator Expressions
# Is an expression that returns a generator object.
print("Generator exp")
squares = (n**2 for n in range(3))

type(squares) # generator

for sqr in squares:
    print(sqr)
