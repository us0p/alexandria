#include <stdio.h>
int increment_age();
int incremente_static_age();

int main(void) {
  // inside function you can initialize a static variable
  // using the static keyword.
  // Note that global variables are static by default.

  // A static variable is initialized to 0 if no initial value is specified, and
  // it retains the value across function calls.

  // Same behaviour as a variable declaration, but every element of the array
  // will be initialized to 0;
  static int ages[3];
  printf("increment_age: %d\n", increment_age());
  printf("increment_age: %d\n", increment_age());
  printf("increment_age: %d\n", increment_age());

  printf("\nNow with static variable\n\n");

  printf("increment_static_age: %d\n", incremente_static_age());
  printf("increment_static_age: %d\n", incremente_static_age());
  printf("increment_static_age: %d\n", incremente_static_age());
}

// This fn will always give us the same return value;
int increment_age() {
  int age = 0;
  age++;
  return age;
}

// This fn will always give us the age + 1 as a return value;
int incremente_static_age() {
  // Static variables are automatically initialized to 0;
  static int age;
  age++;
  return age;
}
