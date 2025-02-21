# OOP (Object Oriented Programing)

Is a programing paradigm that is based on the concepts of `"objects"`, 
which are instances of a class.  
In OOP a class is a blueprint for creating objects, which have both 
attributes and methods. The main idea is to model real-world objects and 
their interaction, making it well-suited for creating complex and 
large-scale software systems.  

## OOP pilars
**Inheritance**  
Is a fundamental concept in object-oriented programming that allows a new 
class to inherit the properties and methods of an existing class.  
The class that is inherited from is called the `parent` or `super class`, 
while the class that inherits is called the `child` or `sub class`.  
Inheritance enables code reuse, where a child class can inherit the 
properties and methods of its parent class and potentially add or override
them.  
The main advantage of inheritance is that it allows for a clean and 
organized way to reuse code and share functionality among classes.  
  
**Polymorphism**  
Is a concept in OOP that allows objects of different classes to be treated
as objects of a common parent class.  
This is achieved by defining a common `interface` for all classes that need 
to be treated polymorphically.  
  
**Abstraction**  
Is a concept in OOP that refers to the process of hiding the implementation
details of an object and exposing only its essential features. It enables 
the use of objects without the need to understand the underlying complexity
of their internal structure and behavior.  
  
**Encapsulation**  
Is a concept in OOP that refers to the practice of wrapping an object’s 
internal data and behavior within a defined interface, and hiding the 
implementation details from the outside world.  
It is one of the fundamental concepts of OOP and is closely related to the
concepts of data hiding and information hiding.  
Encapsulation is achieved by using access modifiers (such as `public`, 
`private`, and `protected`) to control the visibility and accessibility of
an object’s data and methods.  
  
## OOP Consequences
**Interfaces**  
Is a contract or a set of methods that a class must implement.  
It defines a common set of methods that a class must provide, but it does 
not provide any implementation details.  
An interface can include both method signatures and constants.  
Interfaces are used to define a common behavior for a group of related 
classes, and to provide a way for objects of different classes to be 
treated polymorphically.  
A class can implement multiple interfaces, but can only inherit from one 
base class.  

**Abstract classes**  
Are classes that cannot be instantiated. Instead, they serve as a 
`template` or `blueprint` for other classes to inherit from.  
An abstract class can contain both abstract and non-abstract methods.  
Abstract classes are used to provide a common interface and implementation
for a group of related classes. They are also used to define common 
behavior that must be implemented by all subclasses.  
A subclass that inherits from an abstract class is called a concrete class,
and it must provide an implementation for all the abstract methods declared
in the parent class.  

**Concrete classes**  
Are classes that can be instantiated, meaning objects can be created from 
it.  
A concrete class is a class that provides an implementation for all of the
abstract methods declared in its parent class, if it inherits from an 
abstract class.  
A concrete class can also be a class that does not inherit from an abstract
class.  
Concrete classes are used to provide specific implementation details for a
group of related classes that inherit from a common class.  
A concrete class can have its own methods and variables, and can also 
override the methods of its parent class.  

## Abstract classes x Interfaces
We use an abstract class when exists an hierarchy between those classes and
we want to share some behaviour which must exist but it has a different 
implementation for each child class.  
Interfaces are used when there isn't a hierarchy between the classesa and 
they aren't reladed in meaning, they just share a common behaviour.  
For example both human and cars can run, but the implementation of those 
methods will probably be different for each class, in this case your should
probably use interface to represent this abstraction.  
Another example is about walk, both gorllas and cats are able to walk, even
they are both Animals, the implementation of their walkin might be 
different as gorillas are able to walk in two legs, therefore you should 
probably use an Abstract class to represent this abstraction.  
  
## More about polymorphism
There are two types of polymorphism:
 - **Compile-time** polymorphism occurs when the type of the object that is
   going to be acted upon is determined at compile-time. This is achieved 
   through method overloading, which allows multiple methods to have the 
   same name but different parameters within the same class.
 - **Run-time** polymorphism occurs when the type of the object is 
   determined at run-time. This is achieved through method overriding, 
   which allows a child class to provide a specific implementation of a 
   method that is already defined in its parent class.
