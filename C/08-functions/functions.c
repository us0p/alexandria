#include <stdio.h>

// You can't create functions inside a function in C;
// And as C compiler read files top to bottom, this means that to our main
// function be able to call our function, we should declare our functions before
// main;
// But the main fn is the place where all the logic is connected, so it's a
// little odd to first see the functions and then the main fn, to keep things
// more organized you can declare the function prototype at the top of the file
// and declare the function itself later on the file. With this you're telling
// the compiler that the function exists before main is called;
int sum(int a, int b);
int deep_sum(int *a, int *b);

int main(void) {
  // C functions cannot return more than one value;
  // You can’t define a default value for a parameter.
  // Variable declared inside function are created at the point of invocation of
  // the function and are destroyed when the function ends, and it's not visible
  // from the outside;

  int a = 1, b = 2;

  int c = sum(a, b);

  printf("sum a + b: %d\n", c);

  printf("a: %d\n", a);

  int d = deep_sum(&a, &b);

  printf("deep sum a + b: %d\n", d);

  printf("a: %d\n", a);

  // this won't raise an error when building with GCC!!!;
  // this_fn_will_be_called_before_declaration();
}

// Parameters are passed by copy. This means that if you modify a,
// its value is modified locally, and the value outside of the function,
// where it was passed in the invocation, does not change.
// If you pass a pointer as a parameter, you can modify that variable value
// because you can now access it directly using its memory address.
int sum(int a, int b) {
  a++; // the a declared outside the function remains unchanged!;
  return a + b;
}

int deep_sum(int *a, int *b) {
  *a += 1; // the variable declared outside the function is altered!;
  return *a + *b;
}

// Make sure you define the function before calling it, or the compiler will
// raise a warning and an error. Since C does not “see” the function
// declaration before the invocation, it must make assumptions. And it assumes
// the function to return int. The function however returns void, hence the
// error.
// If you change the function definition to return a int type, you won't get
// an error, so be careful.
int this_fn_will_be_called_before_declaration(void) { return 0; }
