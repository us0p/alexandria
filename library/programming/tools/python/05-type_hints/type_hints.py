from typing import Callable, ClassVar, Literal, NamedTuple, NewType, ParamSpec, Protocol, Sequence, TypeVar, TypedDict

def moon_weight(earth_weight: float) -> str:
    return f'On the moon, you would weight {earth_weight * 0.166} kilograms'

# Type alias: creates an instance of TypeAliasType.
# Vector and list[float] are now treated equivalently.
Vector = list[float]

# From Python 3.12, you can create type aliases through the "type" statement
# type Vector = list[float]

dict[str, str] # dict types is abstract over two types, key and value.

# New types: creates a new type by making the new a subtype of the provided.
# static type checker will treat the new type as if it were a subclass
# of the original type.
# parent classes can't be used as values for subclasses requirements but,
# subclasses can be used as values for parent class requirements.
UserId = NewType('UserId', int)

# you may still perform all int operations on a variable of type UserId,
# but the result will always be of type int.

# it's invalid to create a subtype of a synthetic type.
# class AdminUser(UserId): pass - Base class "UserId" is marked final and 
# cannot be subclassed.

ProUserId = NewType('ProUserId', UserId)

# Callable objects: functions and other callable objects can be annotated
# using Callable.

Fn = Callable[[int], str]

# Fn is a type alias for a function which receiver a singular int parameter
# and returns a str.
# the subscription syntax must always be used with exactly two values:
# the argument list and the return type.
# the argument list must be a list of types, a ParamSpec, Concatenate, or
# an elipsis.
# the return type must be a single type.
# if a literal ellipsis is given as the argument list, it indicates that a
# callable with any arbitrary parameter list would be acceptable.

def age(age: int) -> str:
    return f"I'm {age}"

fn: Fn = age # age function matches Fn type alias Callable signature.

# Callable cannot express complex signatures such as functions that take a 
# variadic number of arguments, overloaded functions, or functions that 
# have keyword-only parameters.
# For this you need to inherit from the Protocol base class with a __call__
# method.

class Combiner(Protocol):
    def __call__(
            self,
            *vals: bytes,
            maxlen: int | None = None) -> list[bytes]: ...

# now you can use Combiner as a fn type with complex signatures in your
# typings.

# generics:
# functions, classes and type aliases may contain a type parameter list:
U = TypeVar('U')

# Function is generic over TypeVar "U"
def second(l: Sequence[U]) -> U:
    return l[1]

# new in Python 3.12 -> added syntatic support for generics.
# function is generic over TypeVar "T"
# def first[T](l: Sequence[T]) -> T:
#     return l[0]

# class is generic over T and inherits from Mapping which has str keys,
# and values are generic over the class T.
# could also use "Mapping" which would default to "Mapping[Any, Any]".
# class MyDict[T](Mapping[str, T]):
#     ...

# TypeVar declarations can define bounds and constraints.
T = TypeVar("T", bound=int)
ListOrSet = list[T] | set[T]

# V must be a subclass of int or str but it'll be treated as int or str
V = TypeVar("V", int, str) # Constraints are defined as *args.
GenericListOrSet = list[V] | set[V]

# since Python 3.12:
# The new generic sintax allow type variables to defines bounds and
# constraints with a colon (:) followed by an expression.

# A single expression after the colon indicates a bound. Semantically, 
# this means that the typing.TypeVar can only represent types that are a 
# subtype of this bound. 

# A parenthesized tuple of expressions after the colon indicates a set of 
# constraints. Constrained type variables can only take on one of the 
# types in the list of constraints.

# type ListOrSet[T: int] = list[T] | set[T] # T must be a subclass of int.
# type GenericListOrSet[T: (int, str)] = list[T] | set[T]

W = TypeVar("W", str, bytes)

def concatenate(x: W, y: W) -> W:
    return x + y

# concatenate('one', b'two') - "Literal[b"two"]" is incompatible with "str"
# can't use both types of a constraint in generic functions or classes.

# annotating tuples:
# in Python, is common for tuples to have elements with different types.
# for this reason, in Python's typing system, tuple annotations accepts
# any number of type arguments.
# the number of type arguments also determines the length of the tuple.
# each type is respective for its position in the tuple:

x: tuple[int] = (5,)

y: tuple[int, str] = (5, "foo")

# z: tuple[int] = (1, 2, 3)
# error, type annotation indicates a tuple of length 1, but z has been 
# assigned to a tuple of length 3.

# to denote a tuple which could be of any length, and in which all elements 
# are of the same type:

w: tuple[int, ...] = (1, 2, 3)

v: tuple[()] = () # can only be assigned to empty tuples.

u: tuple = ('a', 'b', 'c') # same as tuple[Any, ...]

# the type of class objects:

# variables annotated with type[T] may accept values that are classes
# themselves, specifically, it will accept the class object of T.

class A:
    pass

# A() has type A
# A has type type[A]

def t(a: type[A]) -> None:
    print(a)

# t(A()) - can't use A() as A != type[A]

# ParamSpec:
# is used to represent a set of function parameters in type hints. It
# allows you to specify that a function accepts a variable number of
# positional or keyword arguments.
# can be specified with an instance of ParamSpec or with ** notation:

X = ParamSpec("X")

def my_decorator(func: Callable[X, int]) -> Callable[X, int]:
    def wrapper(*args: X.args, **kwargs: X.kwargs) -> int:
        result = func(*args, **kwargs)
        return result

    return wrapper

# new in Python 3.12: 
# ParamSpec variables can be specifiedn in generic syntax by prefixing "**".

# def my_decorator[**V](func: Callable[V, int]) -> Callable[V, int]:
#   ...

# nominal subtyping:
# class A is allowed where a class B is expected if and only if A is 
# a subclass of B.
# this means that you need to explicit inform that a class is subclass 
# of another by inheriting.
# this isn't the default behavior expected of a dynamically typed
# language at run-time.

# structural subtyping:
# allows a class to be implicitly considered subclass of another based
# on it's methods return types and arguments.

# Special typing primitives:
# can be used as types in annotations. They don't support subscription
# using [].

# Any - Special type indicating an unconstrained type.
# AnyStr - meant to be used in functions that may accept str or bytes
#          but cannot allow the two mix.
# LiteralString - includes only literal strings. objects types as just
#                 str can't be used.
# Never/NoReturn - are used to indicate that a function never returns.
# Self - Represent an instance of the current enclosed class. You
#        should not use Self as the return annotation if the method is
#        not guaranteed to return an instance of a subclass when the
#        class is subclassed.

class Eggs():
    # Self would be an incorrect return annotation here,
    # as the object returned is always an instance of Eggs,
    # even in subclasses
    def return_eggs(self) -> 'Eggs':
        return Eggs()

# Special forms:
# can be used as types in annotations. They all support subscription
# using [].

# Union - Union[X, Y] is equivalent to X | Y and means eiter X or Y.
# Optional - Optional[X] is equivalent to X | None (or Union[X, None]).
#            This is not the same concept as an optional argument, which
#            is one that has a default.  An optional argument with a 
#            default does not require the Optional qualifier on its type 
#            annotation just because it is optional. On the other hand, 
#            if an explicit value of None is allowed, the use of Optional 
#            is appropriate, whether the argument is optional or not.
# Lieteral - Can be used to indicate that the annotated object has a value
#           equivalent to one of the provided literals.

Mode = Literal['r', 'rb', 'w', 'wb'] 

def open_helper(file: str, mode: Mode) -> None: ...
# mode can be any literal present in Mode.

# ClassVar - a variable annotation wrapped in ClassVar indicates that a
#            given attribute is intented to be used as a class variable
#            and should not be set on instances of that class.

class Starship:
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 0                      # instance variable

# Final - final names  cannot be reassigned in any scope. Final names 
#         declared in class scopes cannot be overridden in subclasses.

# Special directives:
# These functions and classes should not be used directly as 
# annotations. Their intended purpose is to be building blocks for 
# creating and declaring types.

# NamedTuple - used to type named tuples, named tuple subclasses can
#              have docstrings and methods.
class Employee(NamedTuple):
    name: str
    id: int = 3

employee = Employee('Guido')

# TypedDict - declares a dictionary type that expects all of its 
#             instances to have a certain set of keys, where each key 
#             is associated with a value of a consistent type.
#             you can mark keys as required or not with Required and
#             NotRequired respectively.
#             You can mark all keys as non required or not with the
#             'total' argument.
Point2D = TypedDict(
    'Point2D',
    {
        'x': int,
        'y': int,
        'label': str
    },
    total = False
)

a: Point2D = {"x": 1, "y": 2, "label": "good"}

# can also be used as:
# class Point2D(TypedDict, total = True): all keys are required (default)
#     x: int
#     y: int
#     label: NotRequired[str]
