# Decorator
# It's a design pattern that allows the user to add new functionality to an
# existing object without modifying its structure.
# They are typically applied to functions.

# In Python, function are first class citzens. This means that they can:
# - be passed as an argument.
# - returned from a function.
# - assigned to a variable.

# A decorator is a high order function that expects a function as input and
# return a function as result.
# The decorated function (function received as argument) is modified by the
# decorator closure, which is then returned as a new function.

import functools
from typing import Callable

Fn = Callable[[], str]

def upper_decorator(function: Fn) -> Fn:
    def wrapper():
        fn_output = function()
        return fn_output.upper()
    return wrapper

def hello_world() -> str:
    return "Hello, World!"

upper_hello_world = upper_decorator(hello_world)
print(upper_hello_world())

# We can make our code simples by using the decorator "@" syntax:
# It must be used before the declaration of the function.
@upper_decorator
def hello_brazil() -> str:
    return "Hello, Brazil!"

print(hello_brazil())

# We can apply multiple decorators to a single function.
# The decorators will be applied in reverse order.

def lower_decorator(fn: Fn) -> Fn:
    def wrapper():
        fn_ouput = fn()
        return fn_ouput.lower()
    return wrapper

# It's a common practice to use functools.wraps to ensure that the 
# metadata of the original function is preserved throughout the stacking 
# process. This helps maintain clarity and consistency in debugging and 
# understanding the properties of the decorated function.
def capitalize_decorator(fn: Fn) -> Fn:
    @functools.wraps(fn)
    def wrapper():
        fn_output = fn()
        return fn_output.capitalize()
    return wrapper

@capitalize_decorator # executed second
@lower_decorator # executed first
def hello_japan_upper() -> str:
    return "HELLO, JAPAN!"

print(hello_japan_upper())

FnArg = Callable[[str, str], None]

# Decorators with arguments
# The number and type of the arguments must match between the wrapper and
# the decorated function.
def decorator_with_arguments(fn: FnArg) -> FnArg:
    def wrapper(arg1: str, arg2: str):
        print(f"args 1: {arg1}, {arg2}")
        fn(arg1, arg2)
    return wrapper

@decorator_with_arguments
def args(arg1: str, arg2: str):
    print(f"args 2: {arg1}, {arg2}")

args("a", "b")

# General purpose decorators
# To define any number of arguments for a wrapper, we can use *args and
# **kwargs to collect all arguments received and use then as needed.
def arbitrary_arguments_decorator(fn):
    def arbitrary_arguments_wrapper(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        fn(*args)
    return arbitrary_arguments_wrapper

@arbitrary_arguments_decorator
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

# Passing arguments to the decorator
# decorator with arguments follow the structure:
# - The outmost function is the decorator maker. It's the function that
#   will receive the arguments for the decorator.
# - The decorator. It's the function that will receive the decorated
#   function.
# - The wrapper. This is the function that will modify the behavior of
#   the received function. it must return the result of a call of the
#   received function.

Fn1 = Callable[[int, int], str]
Fn2 = Callable[[Fn1], Fn1]

def decorator_maker(d_arg1: str, d_arg2: int, d_arg3: int) -> Fn2:
    def decorator(fn: Fn1) -> Fn1:
        def wrapper(f_arg1: int, f_arg2: int) -> str:
            print(
                "wrapper has access to decorator arguments",
                d_arg1,
                d_arg2,
                d_arg3
            )

            return fn(f_arg1, f_arg2)
        return wrapper
    return decorator

@decorator_maker("name", 1, 2)
def decorated_function_with_arguments(f_arg1: int, f_arg2: int) -> str:
    return f"arg1: {f_arg1}, arg2: {f_arg2}"

print(decorated_function_with_arguments(5, 10))
