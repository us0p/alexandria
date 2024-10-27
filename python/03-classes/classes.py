# class definition:
class MyClass:
    i = 12345

    # for methods, the instance object is the first argument of the
    # function.
    def f(self):
        return "hello world"


# class instantiation:
x = MyClass()


# class definition with customizable instantiation:
# when a class defines a __init__() method, class instantiation
# automatically invokes __init__() for the newly created class instance.
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Dog:
    king = "canine"  # class variable, shared by all instances

    tricks = []  # shouldn't use list or dictionaries as class variables.

    def __init__(self, name):
        self.name = name  # instance variable, unique to each instance

    # calls to this method would update tricks property, which can cause
    # unexpected behaviour in other instances of the class.
    def add_trick(self, trick):
        self.tricks.append(trick)


# if the same attribute name occurs in both an instance and a class, then
# attribute lookup prioritizes the instance.


class Cat:
    species = "cat"

    def __init__(self, species):
        self.species = species


# in python there's no enforcing of data hiding. It's all based upon
# conventions.
# each value is an object, and therefore has a class (also called its type).
# It's stored as object.__class__.

# inheritance


class Animal:
    def __init__(self, group):
        self.group = group


class Lion(Animal):
    def __init__(self, group, name):
        super().__init__(group)
        # you could also: Animal.__init__(self, group)
        self.name = name


# An overriding method in a derived class may want to extend rather than
# simply replace the base class method.
# A simple way to call the base class method directly is to call
# BaseClassName.methodname(self, arguments). Clients can use this as well.

# python has two built-in functions that work with inheritance:
# isistance(obj1, obj2), will yield True only if obj.__class__ is equal to
# obj2 or some derived class from obj2.
# issubclass(type1, type2), will check class inheritance.

# multiple inheritance


class Wolf(Animal, Dog):
    def __init__(self, group, name, age):
        Animal.__init__(self, group)
        Dog.__init__(self, name)
        self.age = age


# You can think of the search for attributes inherited from a parent class
# as depth-first, left-to-right, not searching twice in the same class
# where there is an overlap in the hierarchy. Thus if an attribute is not
# found in Wolf, it's searched for in Animal, then recursively in the base
# class of Animal, and then it goes to class Dog and so on.

# Private variables:
# since there's no variable hiding in Python a convention followed by most
# Pyhon code is that a name prefixed with an underscore (e.g. _spam) should
# be treated as a non-public part of the API.

# name mangling:
# any identifier of the form __spam (at least two leading underscores, at
# most one trailing underscore) is textually replaced with _classname__spam,
# where classname is the current class name with leading underscore(s)
# stripped.


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method.


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# The above example would work even if MappingSubclass were to introduce a
# __update identifier since it is replaced with _Mapping__update in the
# Mapping class and _MappingSubclass__update in the MappingSubclass class
# respectively.


class Employee:
    raise_amount = 1.04

    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay

    # class methods can be defined with decorators.
    # class methods receive the base class instead of an instance of the class.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # class methods can also be used as alternative constructors.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # static methods doesn't receive any default arguments.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Accessors in python are defined with the use of decorators:
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # to define a getter we use the @property decorator
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # to define a setter we use the @property_name.setter decorator
    @fullname.setter
    def fullname(self, name):
        fisrt, last = name.split(" ")
        self.first = fisrt
        self.last = last


# property()
# a property represent an intermediate functionality between a plain
# attribute and a method. They allow you to create methods that
# behave like attributes. Properties are a.k.a. managed attributes.
# With property(), you can attach getter and setter methods to given
# class attributes.

# property(fget=None, fset=None, fdel=None, doc=None)

# The return value of property() is the managed attribute itself.
# You can use property() either as a function or a decorator to build
# your properties.

# Properties are also overriding descriptors.


class Property:
    def __init__(self, p):
        self._p = p

    def _get_p(self):
        print("Get p")
        return self._p

    def _set_p(self, value):
        print("Set p")
        self._p = value

    def _del_p(self):
        print("Del p")
        del self._p

    p = property(
        fget=_get_p, fset=_set_p, fdel=_del_p, doc="The p property"
    )


class Property2:
    def __init__(self, p):
        self._p = p

    @property
    def p(self):
        """The p property"""
        print("Get p")
        return self._p

    @p.setter
    def p(self, value):
        print("Set p")
        self._p = value

    @p.deleter
    def p(self):
        print("Del p")
        del self._p


# The decorator approach for creating properties requires defining a first
# method using the public name for the underlying managed attribute, which
# is .p in this case. This method should implement the getter logic.

# When you decorate the second .p() method with @p.setter, you
# create a new property and reassign the class-level name .p to hold
# it. This new property contains the same set of methods of the initial
# property with the addition of the new setter method provided. Finally,
# the decorator syntax reassigns the new property to the .p class-level
# name.

# In subclasses, if you override a method of the property, you'll lose the
# reference to all other metods.
# For example, If you have a class A with a getter and setter for "name".
# If the subclass B overrides the getter of "name", instances of B wont be
# able to set the property anymore as the reference to the setter method
# will be lost.

# __setattr__() and __getattr__() methods
# Are dunder methods similar to properties, but apply to every attribute
# of your class.


class Property3:
    def __init__(self, p):
        self._p = p

    def __getattr__(self, name):
        return self.__dict__[name]

    def __setattr__(self, name, value):
        self.__dict__[name] = value


# descriptors
# are objects that implement the methods of the descriptor protocol.
# __get__(self, obj, type=None) -> object,
# __set__(self, obj, value) -> None,
# __delete__(self, obj) -> None,
# __set_name__(self, owner, name)
# where:
# - self is the descriptor itself.
# - obj is the instance of the object the descriptor is attached to.
# - type is the type of the object the descriptor is attached to.

# the following lookup chain is used when you use dot notation to
# access an attribute of a class.
# 1. you’ll get the result returned from the __get__ method of the
#    data descriptor named after the attribute you’re looking for.
# 2. you’ll get the value of your object’s __dict__ for the key
#    named after the attribute you’re looking for.
# 3. you’ll get the result returned from the __get__ method of the
#    non-data descriptor named after the attribute you’re looking
#    for.
# 4. you’ll get the value of your object type’s __dict__ for the
#    key named after the attribute you’re looking for.
# 5. you’ll get the value of your object parent type’s __dict__
#    for the key named after the attribute you’re looking for.
# 6. repeat the previous step for all the parent’s types in the
#    method resolution order of your object.
# 7. If everything else has failed, then you’ll get an
#    AttributeError exception.

# __get__() is a non-data descriptor.
# __set__() or __delete__() are data descriptors.
# Note that according to the lookup chain, data descriptor take
# precedence to non-data descriptors.


class OneDigitNumericValue:
    # since python 3.6
    # __set_name__ is used to get the name of the attribute which
    # the descriptor has been attached to.
    # This was implemented to solve the single descriptor instance
    # per class problem, in which the common solution was to store
    # the values within the owner class __dict__ attribute in a
    # property with the same name as the descriptor, leading the
    # __init__ method to have an argument "name" which had to be
    # equal to the property the descriptor was being attached to.
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value


class Foo:
    number = OneDigitNumericValue()


# Objects that implement those methods can be used as attributes of
# oher objects and provide special behavior.

# descriptors are instantiated just once per class. That means that
# every single instance of a class containing a descriptor shares
# that descriptor instance.
