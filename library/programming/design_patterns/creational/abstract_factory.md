# Abstract Factoy
Is a creational design pattern that lets you produce families of related 
objects without specifying their concrete classes.

## Definitions
- family: Different objects that are grouped by some criteria.  
  e.g.: A uniform is composed of various different objects, 
  shirts, shoes, skirts or pants, etc. There're many different 'families' 
  of uniforms, police, fireman, militar, etc. Each family has the same 
  object, for example, shirt, but with different properties.
- product: an specifig object.

## Problem
You have an application which has families of related products (objects), 
where each product can have a variation.  
You need to crete individual products so that they match other products of
the same family.  
Also, you don't want to change existing code when adding new products or 
families of products to the program.  

## Solution
This pattern suggests to explicitly declare interfaces for each distinct 
product of the product family. Then you can make all variants of products 
follow those interfaces.  
  
Next, you declare the Abstract Factory - an interface with a list of 
creation methods for all products that are part of the product family. 
These methods must return abstract product types represented by the 
previously extracted interfaces.  
  
Finally, for each product variant in a family, we create a separate 
concrete factory class based on the Abstract Factory interface. A factory 
is a class that returns products of a particular kind which must implement
the product interface.  
  
The client code has to work with both factories and products via their 
respective abstract interfaces. This lets you change the type of a factory
that you pass to the client code, as well as the product variant that the 
client code receives, without breaking the actual client code.  
  
As you might have noticed the client is only exposed to the abstract 
interfaces, so, how does it creates the actual factory objects? Usually, 
the application creates a concrete factory object at the initialization 
stage. Just before that, the app must select the factory type depending on
the configuration or the environment settings.

## Pseudo code of the structure
```plaintext
interface Shirt {
    # define signature of a product.
    # each product should have it's own interface.
    # different families share the same product interface.
}

class MilitarShirt implement Shirt {
    # concrete implementation of a variation of Product
}

class PoliceShirt implement Shirt {...}

interface AbstractFactory {
    # define methods for creating each product of the family.
    createShirt(): Shirt
}

class MilitarFactory implement AbstractFactory {
    # concrete implementation of methods to create products of this family.
    createShirt(): Shirt {
	...
	return MilitarShirt()
    }
}

class PoliceFactory implement AbstractFactory {
    createShirt(): Shirt {
	...
	return PoliceShirt()
    }
}
```

## Applicability
- Use when your code needs to work with various families of related 
  products.
- Consider when you have a class with a set of Factory Methods that blur 
  its primary responsibility.

> In a well-designed program each class is responsible only for one thing. 
  When a class deals with multiple product types, it may be worth 
  extracting its factory methods into a stand-alone factory class or a 
  full-blown Abstract Factory implementation.

## Advantages
- You can be sure that the products you’re getting from a factory are 
  compatible with each other.
- You avoid tight coupling between concrete products and client code.
- Single Responsibility Principle. You can extract the product creation 
  code into one place, making the code easier to support.
- Open/Closed Principle. You can introduce new variants of products without
  breaking existing client code.

## Disadvantages
- The code may become more complicated than it should be, since a lot of 
  new interfaces and classes are introduced along with the pattern.

## Factory Method
This pattern is a consequence of the factory method.  
  
The factory method pattern defines a method for creating an object in the 
creator class, subclasses alter the type of object that will be created.  
  
Key differences of the factory method:  
- The exact type of the object to be created is determined at runtime.
- Limited to one `family` of products.
- Single object.
  
The structure of the Factory method pattern is very simmilar to the 
abstract factory.  
The `Creator` abstract class of the Factory method must define an abstract
`create()` method like the methods defined in the `AbstractFactory`
interface.  
The difference is that the `Creator` abstract class only exposes one method
to create a specific product, which subclasses must implement to provide a
concrete product.  
Also, the main functionality of the `Creator` abstract class is not to 
create a particualr product. Usually the creator class already has some 
core business logic related to products. The factory method helps to 
decouple this logic from the concrete product classes. 
