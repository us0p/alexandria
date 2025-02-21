# Terms
- cycle: when you follow a series of links and end back where you started
         a cycle requires at least tree nodes to be valid.
- acycle: a graph that contains no cycles.
- connected: when every node has a path to other node.
- disconnected: There's at least one pair of vertices that have no edge
  connecting them.
- directed: when there's a direction to the connections.
- undirected: when there's no direction in the connection.
- weighted: the edges have weight associated with them.
- asymetric: in a given edge, the connection weight is different deppending 
  on the direction of the connection.
- dag: directed, acyclic graph.
- vertex: a point in the graph.
- edge: the connection between two vertexes.

# Graphs
A graph is a data structure in which each node is a vertex and each vertex 
might be connected to other vertices through edges.
In graphs, Big O is commonly stated in terms of `V(Vertexes)` and 
`E(Edges)`.
`O(V * E)` means that we will check every vertex and on every vertex we'll
check every edge.

There are two common structures to Graphs

## Adjacent List
it’s an array where each element is an array which represents a node. The 
elements of this node represents the edges of that node, each edge should 
inform where is pointing to and the weight of the connection.

## Adjacent Matrix
It's a matrix were each line represents node vertex and each colmn 
represents an edge, the value of each line + column represents the weight 
of the connection.
It’s not as widely used as an adjacent list because it uses a lot of memory
and takes a lot of time to setup, time complexity of `O(v^2)`

## Searches
Time complexity: O(V + E)
Breadth First search and Depth first search are available in graphs too.
