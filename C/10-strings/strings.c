#include <stdio.h>

int main(void) {
  char name[5] = {'L', 'u', 'a', 'n'};

  char full_name[11] = "Luan Lopes";
  // Do you notice how the array length is 1 value higher than the string actual
  // length? This is because the last character in a string must be a 0 value,
  // the string terminator, and we must make space for it.

  printf("name: %s\n", name);
  printf("full name: %s\n", full_name);
}
