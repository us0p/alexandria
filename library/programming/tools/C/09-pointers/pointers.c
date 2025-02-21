#include <stdio.h>

int main(void) {
  int age = 37;

  printf("age memory address: %p\n", &age);
  // prints the address in memory of the variable;
  // the & operator is used to get the value of the address;

  int *point_to_age = &age;
  // this is not a integer but a POINTER to an INTEGER;

  printf("using pointer to reffer the age variable: %d\n", *point_to_age);
  // Using the point operator on a call like this will
  // get the VALUE that the pointer points to, in this
  // case 37;
  // Also known as deferring;

  printf("\nUsing pointers to alter the value of a variable:\n\n");

  int my_age; // unitialized variable;

  printf("unitialized my_age variable: %d\n", my_age);

  int *address = &my_age; // a pointer to my_age;
  printf("in memory address my_age variable: %p\n", address);

  *address = 24; // deferring;
  // using the pointer to initialize the previous declared variable;
  printf("using address to initialize my_age variable: %d\n", my_age);

  printf("\nUsing pointers to iterate over an Array\n\n");
  // As in C array elements are stored one right after another in
  // memory addresses whe can get the next element by adding 1 to
  // the current address we are on;

  int array[3] = {1, 2, 3};

  for (int *index = array; index < array + 3; index++) {
    int current_index = index - array;
    int *current_address = index;
    int current_value = *index;

    printf("Array address for index %d is %p with the value of: %d\n",
           current_index, current_address, current_value);
  }
}
