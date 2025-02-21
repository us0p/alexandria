#include <stdio.h>

int main(void) {
  // Initialized array:
  int initilized_prices[5] = {1, 2, 3, 4, 5};

  // Empty array;
  int prices[5];

  for (int index = 0; index < 5; index++) {
    prices[index] = index * 30;
  }

  // The variable name of the array, prices in the above example, is a pointer
  // to the first element of the array, and as such can be used like a normal
  // pointer.

  // Other thing about C arrays is that all elements of an array are 
  // sequentially stored in memory, one right after another.

  for (int index = 0; index < 5; index++) {
    printf("Initialized prices at %d: %d\n", index, initilized_prices[index]);
    printf("Prices at %d: %d\n\n", index, prices[index]);
  }
}
