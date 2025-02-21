# Tries
It can perform lookup in constant time.
A trie is always bounded by some limiter.

A good example for a trie is auto-completion, which means that the limiter of
our trie is the number of letters in the alphabet.

The typical structure of a trie is a node which contains:

- children: Array[x]<Node> (x is the bouded size of the array).
- check: boolean (checks if some condition is met, (e.g. if the set of 
  letters at this point is a word).

in the exemple of auto-completion:
- the root node has a children array of size 26.
- whenever you want to add a word to the trie, for each letter in the word
  you create a node for its respective index and in its children array you add
  the next letter index link and so forth.
- when you have a complete word, you mark the respective node as a word.

Traversing:
You can use depth-first search or breadth-first search here, it'll depend on
how you want your data to be retrieved.

Deletion:
For deletion you need to find the last node of the given word and delete the
nodes on your way back up.
You only remove the node itself when it doesn't have any children. Or else
you may remove a whole branch of your tree.
