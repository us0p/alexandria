# Object Oriented Programming (OOP)
Is a programming paradigm that is based on the concepts of `"objects"`,  which are instances of a class.  
In OOP a class is a blueprint for creating objects, which have both attributes and methods. The main idea is to model real-world objects and their interaction.  
## OOP pillars
### Inheritance
Allows a new class to inherit the properties and methods of an existing class.  

The class that is inherited from is called the `parent`, while the class that inherits is called the `child`.  

Inheritance enables code reuse, where a child class can inherit the properties and methods of its parent class and potentially add or override them.
### Polymorphism
Allows objects of different classes to be treated as objects of a common parent class.  

This is achieved by defining a common `interface`.  
### Abstraction
Refers to the process of hiding the implementation details of an object and exposing only its essential features.

It enables  the use of objects without the need to understand the underlying complexity of their internal structure and behavior.  
### Encapsulation
Refers to the practice of wrapping an object’s internal data and behavior within a defined interface, and hiding the implementation details from the outside world.

Encapsulation is achieved by using access modifiers (such as `public`, `private`, and `protected`) to control the visibility and accessibility of an object’s data and methods.  
## OOP Consequences
### Interfaces
Interfaces are used to define a common behavior for a group of related classes, and to provide a way for objects of different classes to be treated polymorphically.  

It defines a common set of methods that a class that wants to implement the interface must provide, but it does not provide any implementation details.  

A class can implement multiple interfaces.  
### Abstract classes
Are classes that cannot be instantiated. Instead, they serve as a `template` or `blueprint` for other classes to inherit from.

An abstract class can contain both abstract and non-abstract methods.

Abstract classes are used to provide a common interface and implementation for a group of related classes. They are also used to define common behavior that must be implemented by all subclasses.

A subclass that inherits from an abstract class is called a concrete class, and it must provide an implementation for all the abstract methods declared in the parent class.  
### Concrete classes
Are classes that can be instantiated, meaning objects can be created from it.

A concrete class is a class that provides an implementation for all of the abstract methods declared in its parent class, if it inherits from an abstract class.

A concrete class can also be a class that does not inherit from an abstract class.  

Concrete classes are used to provide specific implementation details for a group of related classes that inherit from a common class.  

A concrete class can have its own methods and variables, and can also override the methods of its parent class.  
### Scope Visibility
Accessibility or visibility of variables, functions, and other elements in a class.

Common scope visibility are:
- **Public**: A public element can be accessed from anywhere in the program, both within the class and outside of it.
- **Private**: A private element can only be accessed within the class in which it is defined. It is not accessible to other classes, even if they inherit from the class.
- **Protected**: A protected element can only be accessed within the class and its subclasses.
## Abstract classes x Interfaces
We use an abstract class when exists an hierarchy between those classes and we want to share some behavior which must exist but it has a different implementation for each child class.

Interfaces are used when there isn't a hierarchy between the classes and they aren't related in meaning, they just share a common behavior.

For example both human and cars can run, but the implementation of those methods will probably be different for each class, in this case your should probably use interface to represent this abstraction.

Another example is about walk, both gorillas and cats are able to walk, even they are both Animals, the implementation of their walking might be different as gorillas are able to walk in two legs, therefore you should  probably use an Abstract class to represent this abstraction.  