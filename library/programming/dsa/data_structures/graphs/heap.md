## Terms
- heap condition: the condition applied to the heap (max or min)

# Heap
It's a binary tree in which every child or grand child is smaller (max 
heap) or larger (min heap) than the current node.
We need to adjust the tree whenever we add or remove a node.
A heap maintain a weak order, where there's no need to compare sibiling 
nodes.

## Min Heap
Every node in the tree is larger than it's parent, the root node is the
smallest node in the tree.

## Max Heap
Every node in the tree is smaller than it's parent, the root node is the
largest node in the tree.

## Adding a node to heap
A heap is always filled from left to right, until it fills the whole level.
You won't find a middle level of the heap with a dead end.
Whenever you add a new node you must check your heap condition.
If the node fits in the heap condition at the current level, you have 
nothing to do.
If it doesn't, you need to bubble it up, until the heap condition apply or 
until it becomes the root. For that, you need to swap the adding node with 
its parent until you reach that condition.

## Deleting a node from a heap
If you are removing a node from the height of the heap, you hove nothing to
do.
If you are removing from any other place withing the heap you need to 
replace the selected node with the rightest node from the height of the 
heap, then you need to bubble it down following your heap condition, until 
it gets to the right place.

## Heap structure
In order to be able add and remove nodes from the heap we need to have 
access to the height of the heap which is impossible to do without a 
traversing operation.
Therefore, while we work with heaps, we'll work with arrays and not with 
nodes. While nodes provide a better understanding of the operations within 
the heap the structure that really provide the means to perform those 
operations with maximum efficiency are arrays.

Every node has an index, nodes are indexed from left to right, one level at
the time.

To get the index of the left child: 2i + 1
To get the index of the right child: 2i + 2
To get the index of the parent node: (i - 1)/2

Where i is the current index.

Note that, in lower level languages, you won’t get a floating number if you
divide two integers, you get only the integer part.
With those formulas you are know able to get the correct child or parent of
every item of the heap, and is able to get the root (value at index 0), and
the rightest value (value at length - 1) of the heap.
