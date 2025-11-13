# Array
Is a contiguous memory space, in which contains a certain amount of bytes. All elements of an array are of the same type.

```C
// Array of 3 bytes where each byte represents a character in the ASCII table.
char array[3] = {'a', 'b', 'c'};

// Array of 12 bytes where each 4 bytes represents a unsigned int.
int array[3] = {1, 2, 3};
```
## Array indexing
To get a particular element inside an array we use the formula:
$$
typeSize * index + typeSize
$$

Where
1. $typeSize * index$: get the start point in the array.
2. $+ typeSize$: get the offset.

Every operation in an array follows the previous formula thus the running time of indexing and updating in an array are all O(1).