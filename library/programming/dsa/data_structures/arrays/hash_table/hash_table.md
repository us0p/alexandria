[ ] - What is hashing
[ ] - Direct Address Table
[ ] - Double hasing

Terms:
- Linear probing: is a technique used to resolve collisions in hash tables.
  The hash function calculates the hash code, and the search starts from 
  that index, moving sequentially until the target key is found or an empty
  cell is encountered. When the end of the array is reached you modulo it 
  to look over every space in the table.

# Hash Table (Map)
A hash table is an array with a hash function. A hash table provides 
constant time lookup, insert, deletion and update.

The hash function receives an input and produces an output which maps to an
index in the internal array where the value is stored.

A hash function should:
1. produce the same output for a given input.
2. be fast.
3. produce a random output, meaning, the output shouldn't follow a linear 
   basis.

An ideal hash function would always hash different inputs to different 
locations.

## Load Factor
represents how full the table is. it's defined as the ratio of the number 
of elements in the table to the total number of slots or  

`ld = ne/ns`  

A low load factor means the table has many empty slots, leading to fewer 
collisions and faster operations. Many hash tables resize when the load 
factor exceeds a certain threshold (e.g. `0.7`). Resizing typically 
involves creating a new, larger table and rehashing all elements.

Lower load factors reduce collision rates, improving speed at the cost of 
higher memory usage.
Higher load factors save memory but may increase the time complexity of 
operations due to collisions.

## Colisions
When 2 keys maps to the same cell.

There are two traditional ways to deal with collisions:
1. open addressing.
   - we keep everything in the table;
   - linear probing is used to solve collisions in open addressing
   - with open addressing the table is always the same size.
   - but with this linear lookup your table might get a O(n) runtime if 
     your hash table produces many collisions.
   - it's good for small to medium load factors.
2. external chaining.
   - you'll always put the value in the location that was produced by the 
     hashing function.
   - for this, every array index is instead the head of a stack. Whenever 
     you add a new item, you add it as the head of the stack.
   - thus, collisions will create a stack that can be looked upon in that
     location.
   - is usually faster than open addressing, as you don't have to traverse 
     the whole table every time you get a collision.
   - it uses more memory as the size of the table is not fixed anymore.
   - if your hash function produces a lot of collisions your will end up 
     with a running time of O(n), as the lookup function will have to 
     search through the stack which might have many elements.
   - it's good for high load factors.
