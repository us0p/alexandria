[Exercise Link](https://leetcode.com/problems/count-binary-substrings/description/?envType=problem-list-v2&envId=two-pointers)
## Solution
```C
int min(int n1, int n2) {
    return n1 <= n2 ? n1 : n2;
}

int countBinarySubstrings(char* s) {
    int currGroup = 1;
    int prevGroup = 0;
    int groups = 0;
    for (int i = 1; s[i]; i++) {
        if (s[i] != s[i - 1]) {
            groups += min(prevGroup, currGroup);
            prevGroup = currGroup;
            currGroup = 1;
            continue;
        }
        currGroup++;
    }
    groups += min(prevGroup, currGroup);
    return groups;
}
```
## Explanation
The problem asks us to count the number of non-empty substrings that have the same number of zeroes and ones grouped consecutively.

In order to understand the solution we need to understand the pattern that exists while counting those groups.

Given the following sample string `000110011`.
1. The first group is `0011`, and it can be represented as 2 zeroes and 2 ones, or `[2,2]`. The number of strings that have the same number of zeroes and ones is 2 (`0011`, and `01`)
2. The second groups is `1100`, and also have 2 groups.
3. The last groups is the same as the first.

Note that the first part `00011` wasn't considered as we don't have the same number of zeroes and ones in the respective groups.
This first part could be represented as a `[3,2] (3 zeroes, 2 ones)`. Note that the number of groups formed are still 2.
If instead we had `000111`, then it could be represented as `[3,3]` and it would be 3 groups formed.

So as you can see, the limiting factor in group formation is the group with the last elements.
## Intent
We will count the current numbers of consecutive numbers and the numbers in the previous group.
Whenever we start a new group, we increase the number of formed groups with the minimum between the two groups.
## Time and Space complexity
**Time**: O(n)
**Space**: O(1)
