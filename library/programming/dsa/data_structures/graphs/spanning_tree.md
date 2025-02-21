# Spanning Tree
A spanning tree is defined as a tree-like subgraph of a connected, 
undirected graph that includes all the vertices of the graph.

Properties of a Spanning Tree:
- The number of vertices (V) in the graph and the spanning tree are the
  same.
- There's a fixed number of edges in the spanning tree which is equal to
  one less than the total number of vertices (E = V - 1).
- The spanning tree shouldn't be disconnected.
- Every vertex in the tree should be reachable from a designated root vertex 
  through an unique path. If there were multiple sources, it would imply 
  that the spanning tree is fragmented into separated trees.
- The spanning tree should be acyclic.
- The total cost (or weight) of the tree is defined as the sum of the edge's
  weight of all the tree's edges.
- There can be many possible spanning trees for a graph.

Minimum Spanning Tree
Is defined as a spanning tree that has the minimum weight among all the 
possible spanning trees.
The minimum spanning tree has all the properties of a spanning tree with 
an added constraint of having the minimum possible weights among all 
possible spanning trees. Like a spanning tree, there can also be many 
possible MSTs for a graph.

Applications of Spanning Trees:
- Network design: Can be used to find the minimum number of connections
  required to connect all nodes. Minimum spanning trees, in particular,
  can help minimize the cost of the connections by selecting the cheapest
  edges.
- Image processing: can be used in image processing to identify regions of 
  similar intensity or color, which can be useful for segmentation and 
  classification tasks.
- Social network analysis: Spanning trees and minimum spanning trees can 
  be used in social network analysis to identify important connections and 
  relationships among individuals or groups.
