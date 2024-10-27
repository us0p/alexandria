// When we use brackets around the file we're telling the preprocessor to look
// up into the standard library;
#include <stdio.h>
// To include our own files we use quotes like this:
#include "calculate_age.h"

int main(void) { printf("%u\n", calculateAge(1998)); }

// To compile a programs composed by multiple files, you need to list them all
// in the command line: clang -o main.sh main.c calculate_age.c With more
// complex setups, a Makefile is necessary to tell the compiler how to compile
// the program;
