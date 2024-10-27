#include <stdio.h>

// Type definitions:
// The type created with typedef is usually uppercase;
// The typedef allows you to define new types:
typedef int NUMBER;

NUMBER one = 1;

// Enumerated Types:
// Using typedef and enum we can define a type that can have either one value or
// another.
// Every item in the enum definition is paired to an integer internally:
typedef enum {
  monday,    // 0
  tuesday,   // 1
  wednesday, // 2
  thursday,  // 3
  friday,    // 4
  saturday,  // 5
  sunday     // 6
} WEEKDAY;

// Structures:
// A structure is a collection of values of different types:
struct person {
  int age;
  char *name;
};

// You can declare variables that have as type that structure:
struct me {
  int age;
  char *name;
} luan;

// Or multiple ones:
struct family {
  int total_members;
  char *family_name;
} my_family[20], your_family[20];
// Here we declared two arrays of 20 family each;

// Declaring variables later on:
struct person mom;

// Another way of creating a struct is with typedef:
typedef struct {
  int age;
  char *name;
} PERSON;

// We don't need to declare variables with the struct keyword when the struct is
// created with typedef:
PERSON nem;

int main(void) {
  WEEKDAY day = tuesday;

  if (day == monday) {
    printf("It's monday!\n");
    return 0;
  }

  printf("It's not monday!\n");

  printf("\nStructures:\n\n");

  // Initializing structure at declaration time:
  struct person me = {24, "Luan"};

  // Accessing and managing structure data:
  printf("%s, age %d\n", me.name, me.age);

  me.age += 1;

  printf("This year i'm turning %d\n", me.age);
}
