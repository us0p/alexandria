[Exercise Link](https://leetcode.com/problems/sort-array-by-parity-ii/description/?envType=problem-list-v2&envId=two-pointers)
## Solution 1
We're going to predict the next index where we're going to store the current out of order element.
Every time we find a element out of order we swap it with its type's next position.
- **even**: stores the next position of an even number.
- **odd**: stores the next position of an odd number.
- **i**: Anchor that loops over every element in the array.
```C
#include <stdbool.h>

bool isEven(int num) {
    return (num % 2 == 0);
}

int increaseTwoTheLimit(int size, int num) {
    return num + 2 >= size ? size - 1 : num + 2;
}

int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int even = 0;
    int odd = 1;
    int i = 0;
    while(i < numsSize) {
       if(isEven(nums[i])) {
            if (!isEven(i)) {
                int tmp = nums[i];
                nums[i] = nums[even];
                nums[even] = tmp;
                even = increaseTwoTheLimit(numsSize, even);
            } else { 
             i++;
            }
       }
       if(!isEven(nums[i])) {
            if (isEven(i)) {
                int tmp = nums[i];
                nums[i] = nums[odd];
                nums[odd] = tmp;
                odd = increaseTwoTheLimit(numsSize, odd);
            } else {
                i++;
            }
       } 
    }
    return nums;
}
```
## Solution 2
Because of problem's constraints:
- Array has a even number of elements.
- Half of the integers are odd and the other half are even.

Every time a number is out of position, there's will be a counter part that will also be in the wrong position. If we use two pointers that crosses each other, we find the elements that are out of order and swap their positions.
```C
#include <stdbool.h>

bool isEven(int num) {
    return (num % 2 == 0);
}

int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int even = 0;
    int odd = numsSize - 1;
    while(even < numsSize && odd >= 0) {
        if(!isEven(nums[even]) && isEven(nums[odd])) {
            int tmp = nums[even];
            nums[even] = nums[odd];
            nums[odd] = tmp;
            even += 2;
            odd -= 2;
            continue;
        }
        if(!isEven(nums[even])) {
            odd -= 2;
            continue;
        }
        if(isEven(nums[odd])) {
            even += 2;
            continue;
        }
        even += 2;
        odd -= 2;
    }
    return nums;
}
```
## Time and Space Complexity
- **Solution 1**:
	- **Time Complexity**: O(n)
		- This solution holds the anchor pointer until it finds a number that actually belongs to that index. If only the last number in the array satisfy this condition, it'll hold the anchor in a single position until in swaps all elements and then move the anchor until the end causing a more realistic O(2n) runtime.
	- **Space Complexity**: O(1)
- **Solution 2:**
	- **Time Complexity:** O(n)
		- This solution move both pointers simultaneously and finishes execution once one of the pointers reaches the other end of the array, resulting in an actual O(n) time complexity
	- **Space Complexity**: O(1)