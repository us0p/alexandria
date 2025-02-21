# Builder
Lets you construct complex objects step by step. The pattern allows you to 
produce different types and representations of an object using the same 
construction code.  

## Problem
Imagine a complex object that requires laborious, step-by-step 
initialization of many fields and nested objects. Such initialization code 
is usually buried inside a monstrous constructor with lots of parameters.
The constructor with lots of parameters has its downside: not all the 
parameters are needed at all times.  
In most cases most of the parameters will be unused, making the constructor
calls pretty ugly.  

## Solution
This pattern suggests that you extract the object construction code out of 
its own class and move it to separate object called builder.  

The Builder doesn’t allow other objects to access the product during the 
build steps.  

The builder object has the steps for constructing the product object as a set
of its methods (i.e. buildWalls(), buildDoor()).  

The important part is that you don’t need to call all of the steps. You can
call only those steps that are necessary for producing a particular 
configuration of an object.  

Some of the construction steps might require different implementation when
you need to build various representations of the product.  
In this case, you can create several different builder classes that 
implement the same set of building steps, but in a different manner.  

You can further extract the calls to the builder steps used to construct a
product into a separate class director. The director defines the order in
which to execute the building steps, while the builder provides the 
implementation.  
Having a director class in your program isn’t strictly necessary.
However, the director class might be a good place to put various 
construction routines so you can reuse them across your program.
In addition, the director class completely hides the details of product 
construction from the client code. The client only needs to associate a 
builder with a director, launch the construction with the director, and get
the result from the builder.  

## Structure
!["structure example"](https://refactoring.guru/images/patterns/diagrams/builder/structure-indexed.png)
1. A builder interface that defines the common steps to all types of 
   builders. Note that if the hierarchy of products that your builder
   supports is too complex, you should leave the fetching product method
   outside the interface as the builder pattern isn't required to produce
   products that follow a given interface.
2. The concrete builders, different builders are necessary only if there
   must be different implementation regarding the steps of building the
   product, the concrete builders aren't created to express the different
   types of final products.
   A builder should have a method getResult(), which yields the assembled
   product, this is necessary as the builder doesn't allow access to a 
   product during its construction.
3. The director class defines the order in which to call construction 
   steps, so you can create and reuse specific configurations of products.
   The director class is optional.
   The construction result can be obtained directly from the director only 
   if all products follow the same interface. Otherwise, the client should
   fetch the result from the builder.
4. The Client must associate one of the builder objects with the director. 
   Usually, it’s done just once, via parameters of the director’s 
   constructor. Then the director uses that builder object for all further 
   construction.

## Applicability
1. If your constructor has many optional parameters.
2. If you want your code to be able to create different representations of
   some product.
3. As builders are able of constructing products step by step, it's 
   possible to defer execution of a step or even call steps recursively 
   which is pretty handy when building an object tree.

## Pros:
- You can construct objects step-by-step, defer construction steps or run 
  steps recursively.
- You can reuse the same construction code when building various 
  representations of products.
- Single Responsibility Principle. You can isolate complex construction 
  code from the business logic of the product.

## Cons:
- The overall complexity of the code increases since the pattern requires 
  creating multiple new classes.
