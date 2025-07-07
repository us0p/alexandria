#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int start, int middle, int inclusive_end) {
  // if division is not equal it's possible to left and right side
  // to have different sizes.
  // In this case, when middle == start (first operation) or when division
  // is unnequal, we make left side bigger.
  int arr_left_size = middle - start + 1;
  int arr_right_size = inclusive_end - middle;

  int temp_left_arr[arr_left_size];
  int temp_right_arr[arr_right_size];

  // copy respective elements from original arr to temp left array;
  for (int i = 0; i < arr_left_size; i++) {
    temp_left_arr[i] = arr[start + i];
  }

  // copy respective elements from original arr to temp right array;
  // middle + 1 bc middle element is already covered by left side
  for (int i = 0; i < arr_right_size; i++) {
    temp_right_arr[i] = arr[middle + 1 + i];
  }

  int i = 0, j = 0, k = start;

  // merge left and right temp array in original array at their
  // respective positions;
  // i = temp left arr index
  // j = temp right arr index
  // k = original view index
  // note that after each interation, only the side that was
  // replaced is increased.
  while (i < arr_left_size && j < arr_right_size) {
    if (temp_left_arr[i] <= temp_right_arr[j]) {
      arr[k] = temp_left_arr[i];
      i++;
    } else {
      arr[k] = temp_right_arr[j];
      j++;
    }
    k++;
  }

  // if left and right temp array sizes are different, merge remaining
  // left elements in following positions;
  while (i < arr_left_size) {
    arr[k] = temp_left_arr[i];
    i++;
    k++;
  }

  // if left and right temp array sizes are different, merge remaining
  // right elements in following positions;
  while (j < arr_right_size) {
    arr[k] = temp_right_arr[j];
    j++;
    k++;
  }
}

void merge_sort(int arr[], int start, int inclusive_end) {
  if (start >= inclusive_end)
    return;

  int middle = start + (inclusive_end - start) / 2;

  merge_sort(arr, start, middle);
  merge_sort(arr, middle + 1, inclusive_end);

  merge(arr, start, middle, inclusive_end);
}

void print_arr(int *arr, int arrSize) {
  for (int i = 0; i < arrSize; i++) {
    printf("%d\n", arr[i]);
  }
}

int main(void) {
  int arr[] = {38, 27, 48, 10};
  print_arr(arr, 4);
  printf("----\n");
  merge_sort(arr, 0, 3);
  print_arr(arr, 4);
}
