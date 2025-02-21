# Linked List
Linked lists are organized into nodes in which each node points to the next
one in the list.  

A node is a container which store references to other nodes and the data 
itself.  

To get any item in the middle of the list you need to traverse the list 
until that specific node.  

There are two types of linked lists:
1. **Singly linked lists:** each item points to the next one in the list 
   only:
   structure:
     - **prev/next:** pointer to the next or previous node;
     - **data:** the actual value of the node;
2. **Doubly linked lists:** each item points to the next and previous nodes
   in the list.
   structure:
     - **prev:** pointer to the previous node;
     - **next:** pointer to the next node;
     - **data:** the actual value of the node;

## Time complexity for each operation
- **prepend/append:** O(1), only break the links, it doesn’t matter the 
  size of the list.
- **deletion from the ends:** O(1), only breaks the links, it doesn’t 
  matter the size of the list.
- **get head:** O(1), the Linked list should have a reference to the the 
  head of the list.
- **get tail:** O(1), the Linked list should have a reference to the tail 
  of the list.
- **insertion in the middle:** O(n), need to traverse the list until the 
  specified index to insert.
- **deletion in the middle:** O(n), need to traverse the list until the 
  specified index to delete.

## Circular linked list
In a circular linked list, the tail instead of pointing to null will point to 
the start of the list.
In a doubly circular linked list, each node point to the next node and the 
edges (head and tail) point to each other.
