#include <stdio.h>
#include <stdlib.h>

// [ ] - Structure Alignment
// [ ] - Padding
// [ ] - Union

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
// The sintax of a structure is:
// struct [optional_ta] {
//     member_declarations;
// } [optional_instance];

// The following example creates a struct person with two members and must
// be referenced as `struct person`.
// This notation allows for the instantiation of new person structs.
struct person {
  int age;
  char *name;
};

// The following example creates an anonymous struct with an instance Car,
// you can't create new instances of this struct as there's no tag.
// Note that in anonymous structures you can't refer to the struct within
// itself (e.g. Linked List Nodes) as there's no structure tag.
struct {
  char *make;
  int year;
} Car;

// You can also use the two forms togheter, you can create new Employee
// structs with the `struct Employee` notation or you can reuse the
// `Employee` instance created after the struct definition.
struct Employee {
  char *name;
  int age;
} Employee;

// By using `typedef` keyword like in the example bellow, you can create a
// type alias, and thus you can create new instances of the anonymous
// structure by using the alias `Dev` rather `struct Dev`
typedef struct {
  char *area;
  int yearsOfExperience;
} Dev;

// Or multiple ones:
struct family {
  int total_members;
  char *family_name;
} my_family[20], your_family[20];
// Here we declared two arrays of 20 family each;

// Flexible Array Member (FAM)
// Introduced in C99 allows a structure to have a dynamically-sized array
// as its last member. Unlike regular arrays, the size of a flexible array
// is not specified in the structure definition. This allows dynamic memory
// allocation for the structure and the array in a single contiguous block
// of memory.
// When allocating memory for a structure with a flexible array member:
// 1. Allocate enough memory for the structure itself.
// 2. Add extra memory for the flexible array.

struct FAM {
  int count;
  // FAM, note that it must follow this notation and cannot use the int*
  // notation;
  int values[];

  // note that if you use the notation `int* values` you will probably get
  // an error of missaligned address.
  // FAM can only be used with the `int values[]` notation because the
  // notation `int*` declares the member as a pointer, which is independent
  // of the structure's memory layout, leading to the error of missaligned
  // addresses.
  // To use the pointer notation you would have to allocate the array and
  // assign it to the pointer in the structure, which would lead to the
  // array being allocated in another memory block.
};

struct FAM *createFAM() {
  int structureSize = sizeof(struct FAM);
  int dynamicArraySizeForTenElements = sizeof(int) * 10;
  struct FAM *f = malloc(structureSize + dynamicArraySizeForTenElements);

  // note that if the dynamic array is an array of pointers, you should
  // initialize all the elements of the array to NULL.

  return f;
}

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
