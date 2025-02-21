#include <stdio.h>

int linear_search(int *haystack, int haystack_size, int needle) {
    for (int *i = haystack; i < (haystack + haystack_size); i++) {
	int curr = *i;
	if (curr == needle) {
	    return i - haystack;
	}
    }
    return -1;
}

int main(void) {
    int haystack[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int haystack_size = sizeof(haystack) / sizeof(haystack[0]);
    int needle = 7;
    int needle_index = linear_search(haystack, haystack_size, needle);
    printf("The index of the needle %d is %d.\n", needle, needle_index);

    int missing_needle = 11;
    int missing_needle_index = linear_search(haystack, haystack_size, missing_needle);
    printf("The index of the needle %d is %d.\n", missing_needle, missing_needle_index);
}
