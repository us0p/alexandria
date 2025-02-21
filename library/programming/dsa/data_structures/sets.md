# Set
It's a data structure which stores a collection of distinct elements.
Values within sets are immutable. You add and remove new values but you 
can't change existing values within the set.

A set can be implemented in various ways, the most common are:
- **Hash-Based Set:** the set is represented as a hash table where each 
  element in the set is stored in a bucket based on its hash code.
- **Tree-Based Set:** the set is represented as a binary search tree where 
  each node in the tree represents an element in the set.

There are two types of set:
- **Unordered sets:** is implemented using a hash table where insertion is 
  always randomized, all operations in an unordered set take O(1) time on 
  average depending on the hashing function.
- **Ordered sets:** it's generally implemented using a balanced BST and 
  support `O(log n)` lookups, insertion and delete operations.
