Floyd's Fast and Slow Pointers

This algorithm is common used to detect cycles in a linked list.
It works by considering the fact that in a cycle if you have two points
moving at different speeds in the same direction, eventually they will
meet at some point eventually.
A good example are the pointer of a wall clock, in each minute, the
seconds pointer will meet the hours pointer.

Implementation:
1. Start two pointers, fast and slow, both at head;
2. Slow pointer will be moved one node at the time;
3. Fast pointer will be moved two nodes at the time;
4. If Fast pointer is equal to Slow pointer after the movement, then we
   have a loop.
5. If fast pointer reaches a NULL pointer, then the list doesn't have a
   loop.

Time complexity: O(n)
