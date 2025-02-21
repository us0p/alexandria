# def is an abreviation for define.
def fib(n: int) -> None:
    """
        fibbonacci sequency function.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

# the first line of your function's body might be a multi-line string which
# will be treated as a docstring and will be displayed as documentation for
# your function.

fib(2000)

# you can define a function inside another function:
def a():
    def b():
        print("b")
    return b

# default argument values:
def greet(name: str, greeting='Hello') -> str:
    return f'{greeting}, {name}!'

# this function can be called in many different ways.
print(greet('luan'))
print(greet('luan', 'Whats up'))

# default values are evaluted at the point of function definition in the
# defining scope.

i = 5
def f(arg=i) -> None:
    print(arg)
i = 6
f() # will print 5.

# default values are evaluted only once. This makes a differece when the
# default is a mutable object such as a list, dictionary, or instances
# of most classes.

def memf(a: int, L: list[int] = []) -> list[int]:
    L.append(a)
    return L

print(memf(1)) # [1]
print(memf(2)) # [1, 2]
print(memf(3)) # [1, 2, 3]

# keyword arguments:
# a function can also name the argument it wants to reference.
# in this case it doesn't need to follow the paremeter declaration order.
print(greet(name='luan'))
print(greet(greeting='Whats up', name='luan'))

# you can't use a non-kwarg after a kwarg.
# greet(greeting='What up', 'luan') - Positional argument cannot appear 
# after keyword arguments.

# you can't duplicate value for the same argument
# greet("luan", name="lopes") - Parameter "name" already assigned.

# you can't use unknown parameters.
# greet('luan', test=1) - No parameter named "test".

# you can pass any number of kwargs to a function with the ** operator:
def kwf(**kwargs) -> None:
    for kw in kwargs:
        print(kw, '=', kwargs[kw])

kwf(test=1, asdf=2)

# the order of the printed arguments is guaranteed to match the order in
# which they were provided to the function call.

# arbitrary argument list
# functions can be called with an arbitrary number of arguments.
# these arguments will be wrapped up in a tuple.
# before the variable number of arguments, zero or more normal
# arguments may occur.

def varf(*args) -> None:
    for v in args:
        print(v, end = ' ')
    print()

varf(1)
varf('a', 'b', 'c', 'd')

# variadic arguments will be last in the list of formal parameters, as they
# scoop up all remaining input arguments.
# any parameters which occur after *args are keyword-only arguments.

# unpacking argument lists
# if you have a list and want to use its elements as arguments for a given
# function you can do so by using the * operator.

str_list = ['luan', 'Whats up']
print(greet(*str_list))

# if the list has more items than the function params you'll get a type error

# you can also use this for dictionaries with the ** operator.

greet_dict = {"name": "luan", "greeting": "Hey"}
print(greet(**greet_dict))

# lambda expressions
# lambda expressions can be created with the lambda keyword.
# they are small anonymous functions syntatically restricted to a single
# expression.

greet_lamb = lambda name, greeting = 'Hello': f'{greeting}, {name}!'

print(greet_lamb('luan'))

# lambda IIFE (Immediately Invoked Function Expression)
(lambda x: x + 1)(2)

# The traceback of an exception raised while a lambda function is executed 
# only identifies the function causing the exception as <lambda>.
# While using normal functions, the name of the function is used.

# Note that in lambda, the value of arguments are bound at the execution
# time of the lambda expression.
# To overcome this issue, you can assign default value to the argument
# at definition time.
