# Dynamic Array

A dynamic array (Vector in C++ or ArrayList in Java), is a simple array of 
fixed-size, typically larger than the number of elements immediately 
required.  
 
Elements can be added at the end of a dynamic array in constant 
time by using the spare space until this space is completely consumed.  

When all space is consumed, and an additional element is to be added, the 
underlying fixed-sized array needs to be increased in size. Usually the 
area doubles in size.  

Resizing is expensive because you have to allocate a bigger array and copy 
over all of the elements from the array you have overgrow before we can 
finally append our item.  

Dynamic arrays are also a view of the underlying array. Typically dynamic 
arrays have a length and a capacity.  

The capacity represents the number of elements the underlying array can 
store, the length represents the number of actual elements that are present
in the underlying array, so there’s no need to shrink actual size in memory
of the underlying array as you can control it with the length property.

Any operation that adds, get, or removes elements at the end of the array 
have a runing time of O(1).  

If you need to add/remove elements at the start or in the middle of the array
you'll need to shift over every element after the inserting/removing index
which will take a runing time of O(n).
