#include <stdio.h>

#define YEAR 1998 // This is a different way of declaring a const

int main(void) {
  // It's a good practice to use capitalized names for consts in C
  const int AGE = 24;

  // Differences between const and #define:
  // consts are handled by the compiler;
  // #defines are handled by the pre-processor;

  // Note that:
  // #define will have its type infered from the specified value at compile
  // time; 
  // const in the other hand is like a common variable so you can work
  // with its type as always;

  printf("Age: %d\n", AGE);
  printf("Year of birth: %d\n", YEAR);
}
