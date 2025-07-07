[Exercise Link](https://leetcode.com/problems/3sum/description/)
## Solution
```C
#include <stdlib.h>

void merge(int* nums, int start, int middle, int end) {
    int lLen = middle - start + 1;
    int rLen = end - middle;

    int left[lLen];
    int right[rLen];

    for(int i = 0; i < lLen; i++) {
        left[i] = nums[i + start];
    }

    for(int i = 0; i < rLen; i++) {
        right[i] = nums[i + middle + 1];
    }

    int l = 0, r = 0, i = start;
    while(l < lLen && r < rLen) {
        if (left[l] <= right[r]) {
            nums[i++] = left[l++];
            continue;
        }
        nums[i++] = right[r++];
    }

    while(l < lLen) {
        nums[i++] = left[l++];
    }

    while(r < rLen) {
        nums[i++] = right[r++];
    }
}

void sort(int* nums, int start, int end) {
    if (start >= end) return;

    int middle = start + (end - start) / 2;

    sort(nums, start, middle);
    sort(nums, middle + 1, end);

    merge(nums, start, middle, end);
}

void updateTripletGroup(int** arr, int returnSize, int l, int r, int i) {
    int* tmpArr = malloc(3 * sizeof(int));
    tmpArr[0] = l;
    tmpArr[1] = r;
    tmpArr[2] = i;
    arr[returnSize - 1] = tmpArr;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    int** arr = malloc(numsSize * numsSize * sizeof(int*));
    int* returnColSize = malloc(numsSize * numsSize * sizeof(int));
    sort(nums, 0, numsSize - 1);

    for(int i = numsSize - 1; i >= 2; i--) {
        int l = 0, r = i - 1;
        while(l < r) {
            int sum = (nums[l] + nums[r] + nums[i]);
            if(sum == 0) {
                *returnSize += 1;
                updateTripletGroup(
                    arr, 
                    *returnSize, 
                    nums[l],
                    nums[r], 
                    nums[i]
                );
                returnColSize[*returnSize - 1] = 3;
                l++;
                r--;
                while(l < r && nums[l - 1] == nums[l] ) {
                    l++;
                }
                while(l < r && nums[r + 1] == nums[r]) {
                    r--;
                }
                continue;
            }
            if(sum < 0) {
                l++;
                continue;
            }
            r--;
        }
        while(nums[i - 1] == nums[i] && i >= 2) {
            i--;
        }
    }
    *returnColumnSizes = returnColSize;
    return arr;
}
```
## Explanation
In a sorted array if we have our pointers set at the edges of the array, this means that we're always summing the maximum possible values to check if sum is 0.
- If the sum is less than 0, then the negative part is to high and needs to be increased, so we increase the left pointer.
- If the sum is more than 0, then the positive part is to high and need to be decreased, so we decrease the right pointer.
- If the sum is zero, than for that anchor (`i`), both left and right pointers need to be moved.

To avoid duplicated triplets, whenever we find a valid tripled we move the left and right pointers until they point to a number different than the one that produced the match.
The same behavior is applied once left and right cross and we need to move our anchor, we move it until we find a different number.

To avoid memory reallocation overhead, we create a return array that has the square number of elements of the original array.
## Time and Space Complexity
- **Time Complexity**: O(n²) + O log(n)
- **Space Complexity**: O(n²)