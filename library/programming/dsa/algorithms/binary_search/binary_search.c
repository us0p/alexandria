#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int recursive_binary_search(
    int haystack[],
    int start,
    int end,
    int needle
) {
    int middle_index = (end + start) / 2;
    int curr = haystack[middle_index];
    if (start > end) {
	return -1;
    }
    if (curr == needle) {
	return middle_index;
    }
    if (curr < needle) {
	return recursive_binary_search(
	    haystack,
	    middle_index + 1,
	    end,
	    needle
	);
    }
    
    return recursive_binary_search(
	haystack,
	start,
	middle_index - 1,
	needle
    );
}

int iterative_binary_search(
    int haysatck[],
    int start,
    int end,
    int needle
) {
    for (int i = start, j = end; i <= j;) {
	int middle = (j + i) / 2;
	int curr = haysatck[middle];
	if (curr == needle) {
	    return middle;
	}
	if (curr < needle) {
	    i = middle + 1;
	    continue;
	}
        j = middle - 1;
    }
    return -1;
}

double get_time_ms(struct timespec s, struct timespec e) {
    double sDiff = e.tv_sec - s.tv_sec;
    double nSDiff = e.tv_nsec - s.tv_nsec;
    return sDiff * 1000 + nSDiff / 1000000;
}

void fill_haystack(int *haystack, int haystack_size) {
    for (int i = 0; i < haystack_size; i++) {
	haystack[i] = i;
    }
}

#define small_size 1000000
#define big_size 5000000

void perform_test(
    int *haystack,
    int end,
    int needle,
    int (*search)(int *haystack, int start, int end, int needle)
) {
    struct timespec s, e;
    double ms = 0;
    for (int i = 0; i < small_size; i++) {
	clock_gettime(CLOCK_MONOTONIC, &s);
	search(haystack, 0, end, needle);
	clock_gettime(CLOCK_MONOTONIC, &e);
	ms += get_time_ms(s, e);
    }
    printf(
        "%d elements search performed %d times avg duration: %fms\n",
        end,
	small_size,
	ms / small_size
    );
}

int main(void) {
    int *small_haystack = malloc(sizeof(int) * small_size);
    fill_haystack(small_haystack, small_size);

    int *big_haystack = malloc(sizeof(int) * big_size);
    fill_haystack(big_haystack, big_size);

    int needle = -1;

    puts("O(log n) time complexity demonstration");
    puts("haystack[i] >= 0, neede = -1");
    printf("\n");

    puts("Recursive Binary search:");
    perform_test(
	small_haystack,
	small_size,
	needle,
	recursive_binary_search
    );

    perform_test(
	big_haystack,
	big_size,
	needle,
	recursive_binary_search
    );

    printf("\n");

    puts("Iterative binary search:");
    perform_test(
	small_haystack, 
	small_size, 
	needle,
	iterative_binary_search
    );

    perform_test(
	big_haystack, 
	big_size, 
	needle,
	iterative_binary_search
    );

    free(small_haystack);
    free(big_haystack);
}
