Terms:
- **root:** the first node.
- **height:** the longest path from the root to the most recent childish node.
- **binary tree:** nodes in this tree can have any number of children between
  0 and 2.
- **general tree:** nodes in this tree can have any number of children.
- **leaves:** a node without children.
- **branching factor:** the average number of child nodes that each non-leaf 
  node posseses.
- **height-balanced:** The depth of the two subtrees of every node neves 
  differs by more than one.
- **diameter:** the length of the longest path between any two nodes in a 
  tree. This path may or may not pass through the root. The length of a 
  path between two nodes is represented by the number of edges between 
  them.
- **tilt:** is the absolute difference between the sum of all left subtree 
  node values and all right subtree node values. If a node does not have a 
  left child, then the sum of the left subtree node values is treated as 0.
  The rule is similar if the node does not have a right child.

# Tree
It's a data structure in which, starting from a single point, you have many 
possible paths.
For example, the file system of your computer is a tree, you have the 
origin of your file system at / and then you have other directories inside 
of it, which can have more directories within then and so on.

Each element of a tree is a node. The structure of the node depends of the
format of the tree:
- Binary tree node structure:
  - left: *Node
  - right: *Node
  - value: any
- General tree node structure:
  - children: *Node[]
  - value: any

## Traversing a tree
Traversing is the action of visiting every node.
There are three traversal techniques:
- preorder: visit the node and then you go to the next node, the root will
  always be the the first visited node in this strategy.
- inorder: follow a path until the end, visit the node in your way back up,
  the root will always be the middle node in this strategy.
- postorder: follow a path until the end, then visit the node and adjacent
  nodes, the root will always be the last node in this strategy.

inorder, and postorder traversals are known as Depth-First Search as you
first traverse a path as deep as possible to only then visit the node.
In Depth First Traversal we’ve implicit used a Stack data structure as we first
traverse all nodes in one direction (create our stack) and only then start to 
visit each node (First in, Last Out).
Depth First preserves the shape of the traversing (the direction of the arrows) 
of the tree.

## Breadth-First Search
This is the opposite of a Depth First Search so instead of using a Stack we’ll 
using a Queue.
it visits each node of the current level, before going to the next one. This is
valid for every tree, not only binary trees.
Breadth First doesn’t preserves the shape of the traversing (the direction of 
the arrows) of the tree.

## Binary Search Tree (BST):
A binary search tree is just a binary tree with two rules:
- Everything at the left side of the root is less or equal to the root.
- Everything at the right side of the root is greater than it.

Remember that each individual node is also a tree, as it also has children, so 
when we say root, we’re not specifically saying the root of the tree, but each 
individual point.
It’s good to know that in a BST an in-order traversal produces an ordered array.

## Methods
The time complexit of the methods will depend on which type of tree your are
working with.
A binary tree for example, takes `O log(n)` in average.
- Find
- Insert
- Delete

## Balanced Binary Tree
Is a binary tree that follow the following conditions:
- The absolute difference of heights of left and right subtrees at any 
  node is at most 1.
- For each node, its left subtree is a balanced binary tree.
- For each node, its right subtree is a balanced binary tree.

One of its properties is that a balanced tree has a height proportional to
`O(log n)`, where n is the number of nodes.
This ensures that operations like search, insertion, and deletion take 
`O(logg n)` time in the worst case.

> Note that the height of a given node in the three is the maximum value 
  between it's left and right side. A node with 3h in the left and 0h in 
  the right, has 3h.
