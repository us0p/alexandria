#include <stdio.h>

int main(void) {
  int a = 1;

  if (a == 1) {
    printf("a: %d\n", a);
  } else if (a != 1) {
    // do something else;
  } else {
    // do something else again;
  }

  switch (a) {
  case 1:
    printf("switch a: %d\n", a);
    break;
  case 2:
    // do something else;
    break;
  default:
    // will be executed if no other case is matched;
    break;
  }
}
