// The preprocessor parses our program and makes sure that the compiler gets all
// the things it needs before going on with the process;
// Every line that starts with a # is taken care by the preprocessor;
#include <stdio.h>

const int DEBUG = 0;

// Symbolic constant;
#define PI 3.14

// Macro;
// Macros can accept an argument and typically contains code;
// The parentheses around the arguments is a good practice to avoid issues when
// the macro is repaced in the precompilation process;
#define POWER(x) ((x) * (x))

// The difference with function is that macros do not specify the type of their
// arguments or return values, which might be handy in some cases.

int main(void) {
  // These kind of constants change how our program will be compiled, which
  // means that the code inside the condition will only be compiled if the
  // condition evaluate to true;
#if DEBUG == 0
  printf("I'm NOT debugging\n");
#else
  printf("I'm debugging");
#endif

  // We can check if a symbolic constant or a macro is defined:
#ifdef PI
  printf("PI is defined\n");
#else
  printf("PI is not defined\n");
#endif

  // We also have the oposite #ifndef to check if the macro is not defined;

  // Using the macro;
  printf("Macro POWER(4): %u\n", POWER(4));

  // There's also a number of symbolic constants that are pre-defined by the
  // preprocessor; They are identified by 2 anderscores before and after the
  // name, some examples:

  printf("line preprocessor: %d\n", __LINE__);
  printf("file preprocessor: %s\n", __FILE__);
  printf("date preprocessor: %s\n", __DATE__); // last date file was updated;
  printf("time preprocessor: %s\n", __TIME__); // last time file was updated;
}
