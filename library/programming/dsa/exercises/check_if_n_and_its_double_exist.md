# Check if N and Its Double Exist
## Description
Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :
- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

**Example 1**
**Input:** `arr = [10,2,5,3]`
**Output:** `true`
**Explanation:** `For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]`

**Example 2:**
**Input:** `arr = [3,1,7,11]`
**Output:** `false`
**Explanation:** There is no i and j that satisfy the conditions.

**Constraints:**
- `2 <= arr.length <= 500`
- `-103 <= arr[i] <= 103`## Approach name 
## Sorting and Binary Search (Two pointers)
Except when `arr[i] == 0` `target` will always be bigger than `arr[i]`.

If we sort the array in ascending order we can use [Binary Search](binary_search_explanation.md) to effectively search the array for the `target`.

If `arr[i] == 0` then we must have another `0` in the array, index can't be the same.
```go
import (
    "sort"
)

func checkIfExist(arr []int) bool {
	// Orders array
    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
    arr_len := len(arr)
    for idx, num := range arr {
		// Performs binary search on sorted array for every element in arr
        for i, j := 0, arr_len - 1; i <= j; {
            mid := i + (j - i) / 2
			// Only matches if idx are different
            if idx != mid && arr[mid] == num * 2 {
                return true
            } 

            if arr[mid] > num * 2 {
                j = mid - 1
            } else {
                i = mid + 1
            }
        }
    }
    return false
}
```
### Time and Space complexity Analysis
- **Time Complexity**:
	- Sorting takes `O(log n)`
	- Binary search takes `O(log n)`
	- Going over the array takes `O(n)`
	- Since we perform Binary Search for every element in the array, `O(n log n`
- **Space Complexity**:
	- There's no additional space required for this algorithm, `O(1)`.