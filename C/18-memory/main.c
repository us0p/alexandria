#include <stdio.h>
#include <stdlib.h>

void represent_memory_as_sequence_of_bytes() {
  printf("\n");
  int *p = malloc(sizeof(int));
  *p = 26;

  printf("The address is: %p\n", p);
  printf("The value is: %d\n", *p);
  puts("Memory is just a sequence of bytes, like an array.");
  puts(
      "It's also possible to use index notation to get the value of a pointer");
  printf("p[0] == *p: %s\n", p[0] == *p ? "true" : "false");
  free(p);
  printf("\n");
}

void data_types_dynamic_memory() {
  printf("\n");
  // 4 bytes;
  int *p = malloc(4);
  // an array of four characters, each character has 1 byte;
  char *p2 = (char *)p;
  *p = 1684234849;
  printf("%d is %c %c %c %c\n", *p, p2[0], p2[1], p2[2], p2[3]);
  free(p);
  printf("\n");
}

void increase_size_of_allocated_memory() {
  printf("\n");
  int arrSize = 4;
  int *pa = calloc(arrSize, sizeof(int));
  for (int i = 0; i < arrSize; i++) {
    pa[i] = i + 1;
  }
  printf("[ ");
  for (int i = 0; i < arrSize; i++) {
    printf("%d ", pa[i]);
  }
  printf("]\n");
  arrSize *= 2;
  pa = realloc(pa, arrSize * sizeof(int));
  for (int i = 0; i < arrSize; i++) {
    pa[i] = i + 1;
  }
  printf("[ ");
  for (int i = 0; i < arrSize; i++) {
    printf("%d ", pa[i]);
  }
  printf("]\n");
  printf("\n");
  free(pa);
}

void memory_leak_example() {
  printf("\n");
  int x = 5;
  printf("x address: %p, x value: %d\n", &x, x);
  int *p = malloc(sizeof(int));
  *p = 4;
  printf("p address: %p, p value: %d\n", p, *p);
  p = &x;
  printf("p address: %p, p value: %d\n", p, *p);
  // free(p); -> seg fault, &x weren't malloced;
  puts("Even if we free p now, our program would still leak memory as the "
       "reference to our allocated memory was lost");
  puts("You can check this by running the program through valgrind");
  printf("\n");
}

void memory_leak_function_example() {
  printf("\n");
  int *p = malloc(sizeof(int));
  *p = 4;
  printf("square of 4 is: %d\n", *p * *p);
  puts("Function doesn't free the allocated memory before returning");
  printf("\n");
}

int main(void) {
  represent_memory_as_sequence_of_bytes();
  data_types_dynamic_memory();
  increase_size_of_allocated_memory();
  memory_leak_example();
  memory_leak_function_example();
}
