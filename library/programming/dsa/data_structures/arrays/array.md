# Array

Is a contiguous memory space, in which contains a certain amount of bytes.
All elements of an array are of the same type.

char array[3] = {'a', 'b', 'c'};

Array of 3 bytes where each byte represents a character in the ASCII table.

int array[3] = {1, 2, 3};

Array of 12 bytes where each 4 bytes represents a unsigned int.

Array indexing:
To get a particular element inside an array we use the formula:

type_size * index + type_size.

Where:
1. type_size * index -> get the start point in the array.
2. + type_size -> get the offset.

Every operation in an array follows the previous formula thus the runing
time of indexing and updating in an array are all O(1).
