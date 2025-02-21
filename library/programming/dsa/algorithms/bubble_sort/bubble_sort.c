#include <bits/time.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int *arr, int arrSize) {
    for (int i = 1; i <= arrSize; i++) {
	for(int j = 0; j < (arrSize - i); j++) {
	    if (arr[j] > arr[j+1]) {
		int tmp = arr[j];
		arr[j] = arr[j + 1];
		arr[j + 1] = tmp;
	    }
	}
    }
}

void fillArr(int *arr, int arrSize) {
    for (int i = 0; i < arrSize; i++) {
	arr[i] = rand();
    }
}

double getTimeMS(struct timespec s, struct timespec e) {
    double secDiff = e.tv_sec - s.tv_sec;
    double nSecDiff = e.tv_nsec - s.tv_nsec;
    return secDiff * 1000 + nSecDiff / 1000000;
}

void printArr(int *arr, int arrSize) {
    printf("[");
    for (int i = 0; i < arrSize; i++) {
	printf("%d", arr[i]);
	if (i + 1 < arrSize) {
	    printf(", ");
	}
    }
    puts("]");
}

int main(void) {
    srand(time(NULL));
    struct timespec start, end;

    int smallArr[] = {3, 5, 2, 6, 1, 8, 7, 9, 0, 4};
    puts("Sorting demonstration:");
    printf("Original array: ");
    printArr(smallArr, 10);
    bubbleSort(smallArr, 10);
    printf("Sorted array: ");
    printArr(smallArr, 10);

    printf("\n");

    puts("O(n²) time complexity demonstration:");
    int arr[10000];
    fillArr(arr, 10000);
    clock_gettime(CLOCK_MONOTONIC, &start);
    bubbleSort(arr, 10000);
    clock_gettime(CLOCK_MONOTONIC, &end);
    printf("10000 elements duration: %.2fms\n", getTimeMS(start, end));

    int arr2[20000];
    fillArr(arr2, 20000);
    clock_gettime(CLOCK_MONOTONIC, &start);
    bubbleSort(arr2, 20000);
    clock_gettime(CLOCK_MONOTONIC, &end);
    printf("20000 elements duration: %.2fms\n", getTimeMS(start, end));
}
