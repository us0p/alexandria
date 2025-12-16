# Two Pointers
Is a technique that uses two pointers to track pairs in a structure and it should be used when you see a question that involves searching for a pair (or more!) of elements in an array that meet a certain criteria.

This technique is efficient because it focuses in **eliminating** unnecessary pairs from the search usually producing an O(n) running time.

At each iteration, look at the values at each pointer. From those values, think about how to move each pointer so that you can eliminate unnecessary pairs from the search.
## Sample Problem
In a **sorted array** of integers, if there's a **pair** of numbers that sum to the given target, return true.
```C
#include <stdbool.h>
#include <stdio.h>

int main() {
	int sampleArray[7] = {1, 3, 4, 6, 8, 10, 13};
	bool hasSum = hasPairSum(sampleArray, 7, 13);
	printf("Has a pair summing to 13? %b\n", hasSum);
}

bool hasPairSum(int* ar, int arLen, int target) {
	for (int start = 0, end = arLen - 1; start != end;) {
		int sum = ar[start] + ar[end];
		if (sum == target) return true;
		// increase start if sum is less than the sum bc of sorted array constraint.
		if (sum < target) start++;
		// decrease end if sum is bigger than the sum bc of sorted array constraint.
		if (sum > target) end--;
	}
	return false;
}
```
## Partitioning Arrays with Two pointers
This technique can also be used to solve problems that involve partitioning arrays into different regions. For these questions, each pointer represents where the next element belonging to that region should go.
## Sample Problem
Given an unsorted array `nums` with `n` integers that are **either** `0, 1, or 2`. Sort the array in-place in ascending order. **Solve this problem in one-pass without any extra space**.
## Intent explanation
We can start two pointer `start` and `end` that begin at opposite ends in the array.
The `start` pointer represents the position of the next `0`, and the `end` pointer represents the position of the next `2`.
We also start a new pointer `i` at the beginning of the array. This pointer represents the current element we are trying to sort, as well as the boundary of the `1` region.

At each iteration:
1. If `nums[i] == 0`, we swap `i` with the element at the `start` pointer, move left pointer forward and increment `i`.
2. If `nums[i] == 1`, we increment `i`.
3. If `nums[i] == 2`, we swap `i` with the element at the right pointer, move right pointer backward.
```C
int main() {
	int nums[6] = {2, 1, 2, 0, 1, 0};
	int sortedNums = sortNums(nums, 6);
}

void sortNums(int* nums, int numsLen) {
	int start = 0;
	int end = numsLen - 1;
	int i = 0;
	while (i < end) {
		if (nums[i] == 0) {
			nums[i] = nums[start];
			nums[start] = 0;
			start++;
			i++;
			continue;
		}
		if (nums[i] == 2) {
			nums[i] = nums[end];
			nums[end] = 2;
			end--;
			continue;
		}
		i++;
	}
}
```
## Patterns
### Triplets
For problems where you need to find triplets, and the rule for moving the pointers are the same, you can move one pair of pointers first and then move the other instead of trying to move all at once.