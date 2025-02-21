#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// define advantages and disadvantages of each method, for example, which
// size each method generates the least collisions.

int get_key_value(char *key) {
  int key_value = 0;
  for (char *c = key; *c != '\0'; c++) {
    key_value += *c;
  }
  return key_value;
}

// - Simple and fast.
// - If the table size is a prime number, this method distribute keys more
//   uniformly, reducing clustering and collisions.
// - Non-prime table sizes, especially powers of two, can lead to patterns
//   or clustering.
// - If the keys aren't random (e.g; sequential numbers), clustering is
//   more likely.
// - This method yields more collisions when the table is small.
// - This method yields a more uniform distribution then the table size is
//   large, and avoid clustering if the table size is a prime number.
int hash_function_division_method(int key, int arrSize) {
  return key % arrSize;
}

// the number of digits to take from the middle is less than or equal to
// the maximum number of digits the last index of the table has.
// a table with size 10, has index 0..9, it needs only 1 digit from the
// middle. a table with size 1000, has indexes 0..999, it needs 1 to 3 digits
// from the middle.
// Note: your middle number must be consistent, if you need to take 1
// middle digit from the number 123, two is the only choice. but if you
// need to take 1 middle digit from the number 1234, you can pick 2 or 3,
// but your choice must be consistent.
// - Yield a more uniform distribution of indices, even for keys that have
//   similar values.
// - Not dependent of the table size being prime.
// - Slower than the division method.
// - It tends to perform bether than the division method in small sized tables.
// - It's still a good choice for large tables, but as the table size increases
//   its advantages over the division method diminishes.
uint64_t hash_function_mid_square_method(int key, int arrSize) {
  // minimum value must be 1 to avoid zero division.
  uint64_t last_index = arrSize > 1 ? arrSize - 1 : 1;

  uint64_t sqr = (uint64_t)key * key;

  // https://www.geeksforgeeks.org/program-count-digits-integer-3-different-methods/
  uint64_t number_of_digits = (uint64_t)log10(last_index) + 1;
  uint64_t number_of_digits_sqr = (uint64_t)log10(sqr) + 1;
  // avoid zero division.
  number_of_digits_sqr = number_of_digits_sqr == 0 ? number_of_digits_sqr : 1;

  // by making the root index having a minimum value of 2 and vary
  // accordingly to the number of digits required
  // our implementation can take more than a single middle digit, note that
  // it'll always have a preference for the left middle.
  uint64_t root_index = number_of_digits > 2 ? number_of_digits : 2;

  // https://www.geeksforgeeks.org/find-the-middle-digit-of-a-given-number/
  uint64_t first_half_sqr = sqr / pow(10, number_of_digits_sqr / root_index);
  uint64_t mod = (uint64_t)pow(10, number_of_digits);
  uint64_t mid_square = first_half_sqr % mod;

  return mid_square % arrSize;
}

// split the key into equal sized chunks
// sum the chunks
// apply mod
// 1234 -> 12 + 34 = 46 -> 46 % arrSize
// int hash_function_folding_method(int key, int arrSize) {
//  return 0;
//}

typedef struct Person {
  char *name;
  int age;
  char *job;
} Person;

int main(void) {
  int arrSize = 101;
  Person **arr = malloc(sizeof(Person) * arrSize);

  Person *p1 = malloc(sizeof(Person));
  p1->job = "Developer";
  p1->age = 61;
  p1->name = "jose";
  arr[hash_function_mid_square_method(get_key_value(p1->name), arrSize)] = p1;

  Person *p2 = malloc(sizeof(Person));
  p2->job = "Developer";
  p2->age = 58;
  p2->name = "maria";
  arr[hash_function_mid_square_method(get_key_value(p2->name), arrSize)] = p2;

  Person *p3 = malloc(sizeof(Person));
  p3->job = "Developer";
  p3->age = 27;
  p3->name = "pedro";
  arr[hash_function_mid_square_method(get_key_value(p3->name), arrSize)] = p3;

  for (int i = 0; i < arrSize; i++) {
    Person *p = arr[i];
    printf("%d: ", i);
    if (p) {
      printf("name: %s, ", p->name);
      printf("job: %s, ", p->job);
      printf("age: %d\n", p->age);
      continue;
    }
    puts("NULL");
  }
}
