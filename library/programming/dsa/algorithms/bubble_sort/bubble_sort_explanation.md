# Bubble Sort
In bubble sort you’ll have to iterate over the array and swap adjacent 
elements if the previous one is larger than the next.
For each iteration of the whole array, the largest item will always be 
at the end, therefore, in next iterations you need not to look at the 
last item sorted as it’ll be already sorted.
Keep doing this until you have only one element to sort and you’re 
done, as an array of one element is always sorted.

Time Complexity: O(n²).

Pseudo code:
1. Run over every element in the array.
2. Starting in the current element, run over the array avoiding the last 
   element and the number of elements already iterated in the outer loop. 
3. At each iteration of the inner loop, check if the current element of the
   inner loop is greater than the next element. If the previuos element is 
   greater, swap positions.
