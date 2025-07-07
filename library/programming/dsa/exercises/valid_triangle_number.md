[Exercise Link](https://leetcode.com/problems/valid-triangle-number/description/)
## Solution
```C
#include <stdio.h>

void merge(int* nums, int start, int middle, int end) {
    int leftLen = (middle + 1) - start;
    int rightLen = end - middle;

    int left[leftLen];
    int right[rightLen];

    for (int i = 0; i < leftLen; i++) {
        left[i] = nums[i + start];
    }

    for (int i = 0; i < rightLen; i++) {
        right[i] = nums[i + middle + 1];
    }

    int i = start, l = 0, r = 0;
    while(l < leftLen && r < rightLen) {
        if (left[l] <= right[r]){
            nums[i++] = left[l++];
            continue;
        }
        nums[i++] = right[r++];
    }

    while(l < leftLen) {
        nums[i++] = left[l++];
    }

    while(r < rightLen) {
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

int triangleNumber(int* nums, int numsSize) {
    sort(nums, 0, numsSize - 1); 

    int triangles = 0;
    for(int i = numsSize - 1; i >= 2; i--) {
        int l = 0, r = i - 1;
        while (l < r) {
            if (nums[l] + nums[r] > nums[i]) {
                triangles += r - l;
                r--;
                continue;
            }
            l++; 
        }
    }

    return triangles;
}
```
## Explanation
The problem wants to identify all triangles that can be formed in a given range.
Given that `left + right > i`, then all elements in that range would produce a valid triplet for the triangle in a **sorted array**.
At each iteration we want to find the **smallest number that would produce a triplet**. So every time a triplet is not produced, we increase `left`, when a triplet is produce we need to check for the next triplet limit so we decrease `right`.

Our base point is `i` as we always want to check against the maximum value possible to get the range of all possible values.
## Time and Space Complexity
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)