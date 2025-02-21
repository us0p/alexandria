#include <sys/time.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void insertionSort(int *arr, int arrSize) {
    for (int i = 1; i < arrSize; i++) {
	int unorderedElement = arr[i];
	for (int j = i - 1; j >= 0; j--) {
	    int orderedElement = arr[j];
	    if (orderedElement < unorderedElement) break;
	    arr[j + 1] = orderedElement;
	    arr[j] = unorderedElement;
	}
    }
}

void printArr(int *arr, int arrSize) {
    printf("[");
    for (int i = 0; i < arrSize; i++) {
	printf("%d", arr[i]);
	if (i + 1 < arrSize) printf(",");
    }
    printf("]\n");
}

double getElapsedMS(struct timespec s, struct timespec e) {
    double secDiff = e.tv_sec - s.tv_sec;
    double nSecDiff = e.tv_nsec - s.tv_nsec;
    return secDiff * 1000 + nSecDiff / 1000000;
}

void fillArr(int *arr, int arrSize) {
    for (int i = 0; i < arrSize; i++) {
	arr[i] = rand();
    }
}

int main(void) {
    srand(time(NULL));
    struct timespec start, end;

    puts("Sorting demonstration:");
    int smallArr[5] = {23, 1, 10, 5, 2};
    printf("original arr: ");
    printArr(smallArr, 5);
    insertionSort(smallArr, 5);
    printf("sorted arr: ");
    printArr(smallArr, 5);

    printf("\n");
    puts("O(n²) time complexity demonstration:");

    int arr[10000];
    fillArr(arr, 10000);
    clock_gettime(CLOCK_MONOTONIC, &start);
    insertionSort(arr, 10000);
    clock_gettime(CLOCK_MONOTONIC, &end);
    printf("10000 elements duration: %.2fms\n", getElapsedMS(start, end));

    int arr2[20000];
    fillArr(arr2, 20000);
    clock_gettime(CLOCK_MONOTONIC, &start);
    insertionSort(arr2, 20000);
    clock_gettime(CLOCK_MONOTONIC, &end);
    printf("20000 elements duration: %.2fms\n", getElapsedMS(start, end));
}
