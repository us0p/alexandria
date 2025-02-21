# Quick Sort
Is an algorithm that sorts the array in place and has an simmilar idea to 
binary search. 
It halves the number of elements at each iteration, it does that by weakly 
sorting each side of the array at each iteration based on a pivot element,
every element at the pivot's left side is smaller and every element at the
pivot's right side is greather than the pivot, after that you split the
array and sort the wekly sorted halves until you have zero or one element.

for that you'll need:
- pivot: usually the last element of the current view of the array.
- next index to swap: starts at the begining of the current view of the array
  and represents the next index which should be swaped.
- current index: starts at the begining of the current view of the array and
  loops over every element of the current view but the pivot.

with these elements in place:
1. for each current index you'll compare its value with the pivot.
2. if the pivot is greater than the current index value, swap it with the next
   index to swap position, and increase the swap cout by 1.
3. after looping over every index, put the pivot in the next index to swap.
4. repeat the proccess by creating two partitions of the array, one for each
   side of the array, those partitions shouldn't include the pivot. You should
   repeat this until the start and end index overlap.

note that after partitioning the array, you'll always have a weak sorted array,
meaning that everything at the left of the pivot is smaller than the pivot and
everything at the right is greater than.

## Time Complexity
- Average Case: 𝜃(n log n).
- Worst Case: O(n²) - This occurs when the pivot selection is consistently poor.
  This occurs when the pivot is the smallest or greatest element. When the
  pivot is always the smallest or greatest of the set, the partitioning step
  will move only one element relative to the remaining elements. thus to sort
  an array of n itens you'll have to perform n partitions, leading to a O(n²)
  time complexity.
