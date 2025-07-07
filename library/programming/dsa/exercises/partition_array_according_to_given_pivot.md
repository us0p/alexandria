[Exercise Link](https://leetcode.com/problems/partition-array-according-to-given-pivot/)
## My solution
```C
#include <stdlib.h>

int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    *returnSize = numsSize;
    int* newNums = malloc(numsSize * sizeof(int));

    int l = 0, h = numsSize - 1, p = h;
    for(int a = 0; a < numsSize; a++) {
        if(nums[a] < pivot) {
            newNums[l++] = nums[a];
            continue;
        }
        if(nums[a] > pivot) {
            if(newNums[h] == pivot) {
                newNums[p] = newNums[h];
            }
            newNums[h--] = nums[a];
            p--;
            continue;
        }
        newNums[p--] = nums[a];
    }
    int i = numsSize - (numsSize - h - 1), j = numsSize - 1;
    while(i < j) {
        int tmp = newNums[i];
        newNums[i] = newNums[j];
        newNums[j] = tmp;
        i++;
        j--;
    }
    return newNums;
}
```
### Explanation
Maintain three pointers
- `l (low)`: Tracks values smaller than pivot.
- `h (high)`: Tracks values higher than pivot.
- `p (pivot)`: Tracks where pivot occurrences should go next, opt for right side.
`a (anchor)` iterates over the original array.
When a value higher than the pivot is found and there's already a pivot in its place, we move the pivot to it's next occurrence and put the new high in its place while updating both pointers `h` and `p`.

After the initial pass, the elements that are higher than the pivot are going to be in reverse order, so we need to reverse the end of the array. The final loop iterates the number of times that we moved the high pointer.
## Editorial Solution
```C
#include <stdlib.h>

int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    *returnSize = numsSize;
    int* newNums = malloc(numsSize * sizeof(int));

    int l = 0, h = numsSize - 1;
    for(int i = 0, j = numsSize - 1; i < numsSize; i++, j--) {
        if(nums[i] < pivot) {
            newNums[l++] = nums[i];
        }
        if(nums[j] > pivot) {
            newNums[h--] = nums[j];
        }
    }
    while(l <= h) {
        newNums[l++] = pivot;
    }
    return newNums;
}
```
### Explanation
This approach uses a similar paradigm, we'll be adding numbers to the response array as in their respective ends by following the `low` and `high` pointers.

But rather than following only one direction, this implementation follows 2 directions simultaneously and append elements at both ends of the response array at the same time, avoiding the problem of reversed elements in the end.

It also uses the information provided by the function of the pivot and the known fact that they're going to always be in the middle of the array. So after the first run it just fill the gap between `l` and `h` with the known `pivot`.
## Time and Space Complexity for both solutions
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)