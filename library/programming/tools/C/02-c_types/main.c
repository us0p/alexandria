#include <stdio.h>

// a binary digit (0|1) is called a bit, this is the smallest unit of information in a system.
// a byte has 8 bits and it's also called a octect, you can have a byte of 4 bits called nibble or semi-octect.

// a sequence of consecutive bytes in memory can be interpreted in three different ways:
// 1. as a natural number (1, 2, 3, ...)
// 2. as an integer (..., -1, 0, 1, ...)
// 3. as a character

// natural numbers:
// the natural number of a binary sequency is the sum of the power of 2 corresponding to the bits equal to 1:
// the binary sequency 1101 = (2^3) + (2^2) + (2^0) = 13, we don't sum up (2^1) as in it's position we have a 0.
// the interval of natural number a binary sequency can have is (2^s) - 1, where s is the number of bits in the sequence.

// in signed integers the first bit is used to represent if the number is negative or not, 0 for positive 1 for negative that's
// why we subtract one from the number of bits this bit is also called the sign bit.

// integers:
// the integer can be yield by the same formula as natural numbers but you need to change the signal as the sign bit specifies.
// the interval of integers in a binary sequency can be determined as (-2 ^ (s - 1))..(2 ^ (s-1) -1)

// we subtract 1 of the positive ends because we start counting from 0.

// characters:
// every byte whose fisrt bit is 0 represents a character in the ASCII alphabet which is defined by the ASCII table.

// There are some control characters wich are not typographic symbols and are indicated by a special notation, a backslash followed by a digit
// or a letter.
// You need to pay attention to the null caracter (00000000 or \0), it's used to represent the end of a string and doesn't take space when displayed.

int main(void) {
  // Main primitive data types:
  int size_int = sizeof(int);       // 4 bytes
  int size_char = sizeof(char);     // 1 byte
  int size_float = sizeof(float);   // 4 bytes
  int size_double = sizeof(double); // 8 bytes
  void justAnExample(void);         // it's used to represent nothingness

  // Note: The long, short, signed and unsigned are datatype
  // modifier that can be used with some primitive data types
  // to change the size or length of the datatype.

  int size_short_int = sizeof(short int);             // 2 bytes
  int size_u_short_int = sizeof(unsigned short int);  // 2 bytes
  int size_u_int = sizeof(unsigned int);              // 4 bytes
  int size_u_ll_int = sizeof(unsigned long long int); // 8 bytes
  int size_ll_int = sizeof(long long int);            // 8 bytes
  int size_u_char = sizeof(unsigned char);            // 1 byte
  int size_l_double = sizeof(long double);            // 16 bytes

  printf("size int in bytes: %d\n", size_int);
  printf("size char in bytes: %d\n", size_char);
  printf("size float in bytes: %d\n", size_float);
  printf("size double in bytes: %d\n", size_double);
  printf("size short int in bytes: %d\n", size_short_int);
  printf("size unsigned short int in bytes: %d\n", size_u_short_int);
  printf("size unsigned int in bytes: %d\n", size_u_int);
  printf("size unsigned long long int in bytes: %d\n", size_u_ll_int);
  printf("size long long int in bytes: %d\n", size_ll_int);
  printf("size unsigned char in bytes: %d\n", size_u_char);
  printf("size long double in bytes: %d\n", size_l_double);
}
