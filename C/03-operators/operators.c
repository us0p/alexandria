#include <stdio.h>

int main(void) {
  int a = 1;
  int b = 1;

  // Arithmetic operators:

  // Binary operators;
  int addition = a + b, subtraction = a - b, multiplication = a * b,
      division = a / b, modulo = a % b;

  // Unary operators;
  int u_plus = +a; // 1 * a;
  int u_minus = -a; // -1 * a;

  // The difference between 1 and 2 is:
  // 1: increments after using it;
  // 2: increments before using it;
  int increment_1 = a++, increment_2 = ++a, decrement_1 = a--,
      decrement_2 = --a;

  int equality = a == b, not_equal = a != b, bigger_than = a > b,
      less_than = a < b, bigger_than_equal_to = a >= b,
      less_than_equal_to = a <= b;

  // Logical operators:
  // ! not;
  // && and;
  // || or;

  // Compound assignment:
  //  +=
  //  -=
  //  *=
  //  /=
  //  %=

  // Operator precedence (less to more important):
  // the = assignment operator
  // the + and - binary operators
  // the * and / operators
  // the + and - unary operators

  printf("Arithmetic operators:\n\n");
  printf("Binary operators:\n\n");
  printf("a = %d, b = %d\n", a, b);
  printf("addition: %d\n", addition);
  printf("subtraction: %d\n", subtraction);
  printf("multiplication: %d\n", multiplication);
  printf("division: %d\n", division);
  printf("modulo: %d\n\n", modulo);
  printf("Unary operators:\n\n");
  printf("a = %d, b = %d\n", a, b);
  printf("+a: %d\n", u_plus);
  printf("-a: %d\n", u_minus);
  printf("a++: %d\n", increment_1);
  printf("++a: %d\n", increment_2);
  printf("a--: %d\n", decrement_1);
  printf("--a: %d\n\n", decrement_2);
  printf("Equality operators:\n\n");
  printf("a = %d, b = %d\n", a, b);
  printf("equality: %b\n", equality);
  printf("not equal: %b\n", not_equal);
  printf("bigger than: %b\n", bigger_than);
  printf("less than: %b\n", less_than);
  printf("bigger than equal to: %b\n", bigger_than_equal_to);
  printf("less than equal to: %b\n", less_than_equal_to);
}
