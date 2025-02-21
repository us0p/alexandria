# Merge Sort
The divide and conquer strategy is used in this algorithm.
Here we divide the sorting array in the middle and keep halving its parts
until we get to an array of only one element.
From here we start merging the left and right side of each division.
The ordering happens in the mergin section of the code.
Merge sort is a in-place sorting algorithm, thus to swap elements in the
original array without losing reference, an temporary array is necessary
to store the left and right side of the division, before merging them
together in the original array.

Merge Sort Steps:
1. Calculate the middle point between the start and end (inclusive) index
   received in the function call.
2. Recurse to left from start to the middle point.
3. Recurse to right from middle point + 1 to end.
4. The recursive step is repeated until start and end index overlap.
5. When the recursive step is done, you will have two arrays (left and
   right) with only one element.
6. To start the mergin process your need the current start, middle, and
   end index.
7. In the mergin step you need to create two temp arrays (left and right)
   each array must have the same number of elements as stated by the 
   respective calculations (left: middle - start + 1, right: end - middle).
8. Copy the elements of each side to its respective temp array.
9. Loop over both temp array and compare their positions, insert them in
   the correct order in the original array.
10. There might be cases when te division between left and right isn't 
    exact and one side might have more elements than the other. To include 
    the remaining elements, loop over the remaining elements from the left 
    side and add them to the remaining positions in the original array, 
    then loop over the remaining elements in the right side and add them 
    to the remaining positions in the original array.

Time Complexity: O(n log n)
Space Complexity: O(n)
    - Merge sort needs two temporary arrays to merge the left and right 
      side of the divisions, in the end the sum of the legth of those 
      arrays will be equal to the number of elements in the original array,
      so it needs, an n amount of memory to sort an array of size n;
