#include <stdio.h>

// What's the difference between the loops?

int main(void) {
  printf("For loop\n");
  for (int i = 0, j = 10; i <= 10; i++, j--) {
    printf("i: %d, j: %d\n", i, j);
  }

  int x = 0;

  printf("\nWhile loop\n");
  while (x < 10) {
    if (x == 1) {
      printf("skipping x == 1\n");
      x++;
      continue;
    }
    printf("x: %d\n", x);

    x++;
  }

  int y = 0;

  printf("\nDo While loop\n");
  do {
    printf("y: %d\n", y);

    if (y == 2) {
      printf("Breaking in y == 2\n");
      break;
    }

    y++;
  } while (y < 10);
}
