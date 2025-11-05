# Study Plan DSA
Solve problems in categories, focus on mastering one category at a time. This helps you recognize patterns and apply the right approach instinctively.

Start with core data structures they usually are the building blocks for advanced techniques:
	- arrays
	- linked lists
	- stacks
	- hash maps
Once you get good at basics, repeat them until it's second nature. Practice key techniques like binary search, DFS, BFS, and two-pointers methods multiple times, using different problems and variations.

>Every algorithm works on top of a determined data structure or groups of data structures that provides a specific benefit. Learning the data structure of a specific algorithm first will make it easier to understand, why it works originally.

- 30 minutes every day.
- Every Friday, review challenging exercises and solve them from scratch.
- Practice **6 easy** problems per category to solidify learning. Then practice **9 medium** and **3 hard** problems to make it second nature.
## Tips
- Always describe the time complexity of your code.
- Don't spend several hours trying to solve a problem you're stuck on. Look at the solution if you're not making progress after 15 - 20 minutes. If you can't understand the solution under 45 to 60 minutes, try an easier problem.
- If you can solve most medium problems that you haven't seen before, within 20 to 25 minutes, you can probably pass most interviews.
- Always bring up edge cases proactively. Common ones are: null values, empty arrays, duplicates, negative numbers, off-by-one issues.
- Don't blindly memorize algorithms without understanding why they work.
## Pattern recognition cheatsheet
It helps you determine the correct algorithm to use:
- Arrays/String inputs:
	- If the array is sorted: Binary Search, Two Pointers or Prefix Sums.
	- Optimization problems (Max/Min/Subarray): Sliding Window, Dynamic Programming, or Greedy.
	- Looking for duplicates, counts or frequencies: HashMap, HashSet, or Counting Array.
	- Substrings or fixed-size subarrays: sliding window with two pointers.
	- Frequent min/max in window: Monotonic Queue, Deque or Heap.
	- Generate subsets, permutations, combinations: Backtracking.
	- Matching/parsing characters: Stack, especially for balanced parenthesis, infix/postfix.
- Graph Inputs :
	- Shortest path in unweighted graph: Use Breadth-First Search (BFS)  
	- Weighted shortest path: Use Dijkstra, Bellman-Ford, or A\  
	- Connected components / cycle detection: Use DFS, Union-Find (DSU)  
	- Topological ordering: Use Kahn’s Algorithm or DFS + visited set  
	- Optimization like MST: Use Kruskal or Prim’s Algorithm  
- Tree Inputs (Often Binary Trees):
	- Traversals: Use Inorder, Preorder, Postorder, or Level-order (BFS)  
	- Balanced checks or diameter calculations: Use Postorder + height calculations  
	- Lowest Common Ancestor: Use Recursive DFS or Parent Map + Ancestor Set  
- Linked List Inputs:
	- Detecting cycles: Use Slow and Fast Pointers (Floyd’s Algorithm)  
	- Reversals / partial changes: Use pointer juggling: prev, curr, next  
	- Intersection or middle node: Use Two Pointers  
- Dynamic Programming Use-Cases:
	- Optimal choices / Overlapping subproblems: Use DP with Memoization (Top Down) or Tabulation (Bottom Up)  
	- Subset or knapsack problems: Use 1D/2D DP Arrays  
	- String matching or edits: Use DP Matrix (e.g., Edit Distance, LCS)
- Range Queries / Updates:
	- Many sum queries, no updates: Use Prefix Sums  
	- Many sum queries + updates: Use Segment Tree or Fenwick Tree (Binary Indexed Tree)  
- Bit Manipulation:
	- Set-based subsets or XOR logic: Use Bit Masks or XOR  
	- Need to check even/odd, set/unset bits: Use `&`, `|`, `^`, `>>`, `<<` operators  
- When Recursion is Banned or Stack Overflow Risk: Convert to Iterative using Stack.
- Top K / Least K Elements:
	- Use Heap  
	- For exact K-th value, use Quick Select  
- Special Techniques:
	- Sliding Window: For subarray with fixed or dynamic size  
	- Monotonic Stack: Next Greater / Smaller Element  
	- Greedy: Only when local optimum leads to global optimum  
	- Trie: For prefix-based string problems