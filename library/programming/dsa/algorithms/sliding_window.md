# Sliding Window Algorithm
Is a method used to solve problems that involve defining a window or range
in the input data and then moving that window across the data to perform 
some operation within the window. This technique is commonly used in 
algorithms like finding subarrays with a specific sum, finding the longest
substring with unique characters, or solving problem that require a 
fixed-size window to process elements efficiently.

## Example
Say we have an array of size N and also an integer K. Now, we have to 
calculate the maximum sum of a subarray having size exactly K.
One approach would be to take each subarray of size K from the array and 
find out the maximum sum of these subarrays.
The sliding window algorithm takes only one K size subarray from 0 to K-1 
index and calculates its sum, it then shifts the range one by one along the
edges of the subarray and updates the result.

## Types of sliding window
1. Fixed Size:
    1. Find the size of the window required, say K.
    2. Compute the result for 1st window.
    3. Use a loop do slide the window by 1 and keep computing the result 
       window by window.
2. Variable Size:
    1. Increase the right pointer one by one till our condition is true.
    2. At any step if our condition does not match, we shrink the size of 
       our window by increasing left pointer.
    3. Again, when our condition satisfies, we start increasing the right 
       pointer and follwo step 1.
    4. Follow these steps until we reach to the end of the array.

## How to identify sliding window problems
- Problem generally require finding maximum/minimum subarray, substrings 
  which satisfy some specific condition.
- The size of the subarray or substring "K" will be given in some of the 
  problems.

## Practical example
Given an array of integers of size 'n'. Calculate the maximum sum of 'k' 
consectuves elements in the array.

```C
#include <stdio.h>

int calculateMaxSumSubArray(int input[], int inputSize, int subArraySize) {
  if (inputSize < subArraySize)
    return 0;

  int windowUpperBound = 0;
  int windowLowerBound = subArraySize - 1;
  // compute sum of first window of size k.
  int window_sum = 0;
  for (int i = windowUpperBound; i < windowLowerBound; i++) {
    window_sum += input[i];
  }

  int max = window_sum;
  while (windowLowerBound < inputSize) {
    // next sums are calculated by subtracting the first element of the
    // previous subarray and addin the last element of the next subarray.
    // with that we avoid a n^2 running time and get a O(n) running time as
    // we loop over each elent one time only.
    window_sum += input[++windowLowerBound] - input[windowUpperBound++];
    if (window_sum > max) {
      max = window_sum;
    }
  }

  return max;
}

int main(void) {
    int input[4] = {100, 200, 300, 400};
    int k = 2;

    int maxSum = calculateMaxSumSubArray(input, 4, k); // Output: 700
}
```
