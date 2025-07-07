[Exercise Link](https://leetcode.com/problems/valid-palindrome-ii/?envType=problem-list-v2&envId=two-pointers)
## Solution
```C
#include <string.h>

bool continuePalindromeCheck(char* s, int left, int right) {
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

bool validPalindrome(char* s) {
    int start = 0, end = strlen(s) - 1;
    while (start < end) {
        if (s[start] != s[end])  {
            return continuePalindromeCheck(
                s,
                start + 1, 
                end
            ) || continuePalindromeCheck(
                s, 
                start, 
                end - 1
            );
        }
        start++;
        end--;
    }
    return true;
}
```
## Explanation
The code uses the two-pointer approach to check the existence of a palindrome in a string in O(n) time.

It calls `continuePalindromeCheck` on different characters to skip a character on the left and right side respectively.

This is approach divides the code structure in two branches `left` and `right`, a structure similar to a Binary Tree.