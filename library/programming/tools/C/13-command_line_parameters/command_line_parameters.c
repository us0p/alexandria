#include <stdio.h>

int main(int argc, char *argv[]) {
  // argc is a number that represents the quantity of params that where provided
  // in the command line.

  // argv is an array of string that is always going to have at least one item,
  // which is the name of the program;

  printf("%d, params where provided\n", argc);

  for (int index; index < argc; index++) {
    printf("%d parameter was: %s\n", index + 1, argv[index]);
  }
}
