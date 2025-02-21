#include <stdio.h>

void selection_sort(int *haystack, int haystack_size) {
    int *len = haystack + haystack_size;
    for (int *i = haystack; i < len; i++) {
	int *min_add = i;
	for (int *j = i + 1; j < len; j++) {
	    int min = *min_add;
	    int curr = *j;
	    if (curr < min) {
		min_add = j;
	    }
	}
	if (min_add != i) {
	    int tmp = *i;
	    *i = *min_add;
	    *min_add = tmp;
	}
    }
}

void print_haystack(int haystack[]) {
    for (int i = 0; i < 5; i++) {
	printf("%d\n", haystack[i]);
    }
}

int main(void) {
    int haystack[] = {64, 25, 12, 22, 11};
    int haystack_size = sizeof(haystack) / sizeof(int);
    print_haystack(haystack);
    selection_sort(haystack, haystack_size);
    printf("-----\n");
    print_haystack(haystack);
}
