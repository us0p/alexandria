#include <bits/time.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int partition(int arr[], int start, int end) {
  int pivot_index = end - 1;
  int pivot = arr[pivot_index];
  int swap_index = start;
  for (int i = start; i < pivot_index; i++) {
    if (arr[i] <= pivot) {
      int tmp = arr[swap_index];
      arr[swap_index] = arr[i];
      arr[i] = tmp;
      swap_index++;
    }
  }
  arr[pivot_index] = arr[swap_index];
  arr[swap_index] = pivot;
  return swap_index;
}

void recursive_quick_sort(int arr[], int start, int end) {
  if (start >= end) {
    return;
  }
  int pivot_index = partition(arr, start, end);
  recursive_quick_sort(arr, start, pivot_index);
  recursive_quick_sort(arr, pivot_index + 1, end);
}

void iterative_quick_sort(int arr[], int arr_size) {
  int stack[arr_size];

  int top = -1;

  // Initializing stack
  stack[++top] = 0;
  stack[++top] = arr_size;

  // Keep popping from stack while is not empty
  while (top >= 0) {
    int end = stack[top--];
    int start = stack[top--];

    // Set pivot element at its correct position
    // in sorted array
    int pivot_index = partition(arr, start, end);

    // If there are elements on left side of pivot,
    // then push left side to stack
    // this step creates the left view of the array.
    if (pivot_index > start) {
      stack[++top] = start;
      stack[++top] = pivot_index;
    }

    // If there are elements on right side of pivot,
    // then push right side to stack
    // this step creates the right view of the array.
    if (pivot_index + 1 < end) {
      stack[++top] = pivot_index + 1;
      stack[++top] = end;
    }
  }
}

void fillArray(int *arr, int arrSize) {
  for (int i = 0; i < arrSize; i++) {
    arr[i] = rand();
  }
}

void printArray(int *arr, int arrSize) {
  printf("[");
  for (int i = 0; i < arrSize; i++) {
    printf("%d", arr[i]);
    if (i + 1 < arrSize)
      printf(", ");
  }
  puts("]");
}

double getDurationMS(struct timespec s, struct timespec e) {
  double secDiff = e.tv_sec - s.tv_sec;
  double nSecDiff = e.tv_nsec - s.tv_nsec;
  return secDiff * 1000 + nSecDiff / 1000000;
}

int main(void) {
  srand(time(NULL));
  struct timespec s, e;

  int smallArr1[5] = {23, 1, 10, 5, 2};
  puts("Sorting demonstration:");
  printf("Original array 1: ");
  printArray(smallArr1, 5);
  recursive_quick_sort(smallArr1, 0, 5);
  printf("Recursively sorted array 1: ");
  printArray(smallArr1, 5);

  printf("\n");

  int smallArr2[5] = {5, 2, 4, 3, 1};
  printf("Original array 2: ");
  printArray(smallArr2, 5);
  iterative_quick_sort(smallArr2, 5);
  printf("Recursively sorted array 2: ");
  printArray(smallArr2, 5);

  printf("\n");

  int arr1[10000];
  int arr2[20000];

  puts("O(log n) time complexity demonstration:");
  fillArray(arr1, 10000);
  clock_gettime(CLOCK_MONOTONIC, &s);
  recursive_quick_sort(arr1, 0, 10000);
  clock_gettime(CLOCK_MONOTONIC, &e);
  printf("Recursive implementation 10k elements duration: %.2fms\n",
         getDurationMS(s, e));

  fillArray(arr2, 20000);
  clock_gettime(CLOCK_MONOTONIC, &s);
  recursive_quick_sort(arr2, 0, 20000);
  clock_gettime(CLOCK_MONOTONIC, &e);
  printf("Recursive implementation 20k elements duration: %.2fms\n",
         getDurationMS(s, e));

  printf("\n");

  fillArray(arr1, 10000);
  clock_gettime(CLOCK_MONOTONIC, &s);
  iterative_quick_sort(arr1, 10000);
  clock_gettime(CLOCK_MONOTONIC, &e);
  printf("Iterative implementation 10k elements duration: %.2fms\n",
         getDurationMS(s, e));

  fillArray(arr2, 20000);
  clock_gettime(CLOCK_MONOTONIC, &s);
  iterative_quick_sort(arr2, 20000);
  clock_gettime(CLOCK_MONOTONIC, &e);
  printf("Iterative implementation 20k elements duration: %.2fms\n",
         getDurationMS(s, e));
}
