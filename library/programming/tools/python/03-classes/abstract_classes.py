# Abstract Base Classes
# This module provides the metaclass ABCMeta for defining ABCs and a
# helper class ABC to alternatively define ABCs through inheritance.
from abc import ABC, ABCMeta, abstractmethod

# ABC is a helper class that has ABCMeta as its metaclass.
# Note that the type of ABC is still ABCMeta.
class MyABC(ABC):
    pass

# One may also define an abstract base class by passing the metaclass
# keyword and using ABCMeta directly:
class MyABC2(metaclass=ABCMeta):
    pass

# Use this metaclass to create an ABC. An ABC can be subclassed directly, 
# and then acts as a mix-in class. You can also register unrelated 
# concrete classes (even built-in classes) and unrelated ABCs as 
# “virtual subclasses” – these and their descendants will be considered 
# subclasses of the registering ABC by the built-in issubclass() function,
# but the registering ABC won’t show up in their MRO 
# (Method Resolution Order) nor will method implementations defined by the
# registering ABC be callable (not even via super())

# Register subclass as a “virtual subclass” of this ABC.
MyABC.register(tuple)

# @abstractmethod, is a decorator indicating abstract methods.
# Using this decorator requires the class's metaclass to be ABCMeta, or is
# derived from it.

class C(ABC):
    @abstractmethod
    def my_abstract_method(self):
        ...

    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls):
        ...

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod():
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        ...
