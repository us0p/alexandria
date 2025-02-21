# C memory management
C has two types of memory:
- Static memory
- Dynamic memory
- Stack memory

## Static memory
Memory that is reserved for variables before the program runs. Allocation 
of static memory is also known as compile time memory allocation.

## Dynamic memory
Memory that is allocated after the program starts running. Allocation of 
dynamic memory can also be referred to as runtime memory allocation.  
  
Unlike with static memory, you have full control over how much memory is 
being used at any time. You can write code to determine how much memory you
need and allocate it.  
  
Dynamic memory does not belong to a variable, it can only be accessed with
pointers.  
  
Dynamic memory is allocate by using `malloc()` or `calloc()` functions of 
`<stdlib.h>` header.  
  
Dynamic memory stays reserved until it is deallocated or until the program
ends.

> The size of a pointer is usually 8 bytes.

## Stack memory
Is a type of dynamic memory which is reserved for variables that are 
declared inside functions. Variables declared inside a function use stack 
memory rather than static memory.  
  
When a function is called, stack memory is allocated for the variables in 
the function. When the function returns the stack memory is freed.


> Any memory allocation method will return a NULL pointer if it was not 
able to allocate memory.

## Memory access
Dynamic memory does not have its own data type, it is just a sequence of 
bytes. The data in the memory can be interpreted as a type based on the 
data type of the pointer.

## Reallocate memory
If the amount of memory you reserved is not enough, you can reallocate it 
to make it larger.  
  
Reallocating reserves a different (usually larger) amount of memory while 
keeping the data that was stored in it.  
  
To reallocate memory use `realloc()` of `<stdlib.h>`.  

This function tries to resize the memory at ptr1 and return the same 
memory address. If it cannot resize the memory at the current address then
it will allocate memory at a different address and return the new address 
instead, the previous memory block will be released for you.  
  
It's a good practice to assign the new pointer to the previous variable 
so that the old pointer cannot be used accidentally.  
  
Note that if realloc isn't able to realloc more memory, it'll return a 
NULL pointer and the previous memory block won't be deallocated for you. 
With this in mind, the best practice is to store the pointer returned by 
realloc in a temporary variable and if it's not NULL, assign it to the 
pointer of the previous memory block.  
  
## Deallocate memory
When you no longer need a block of memory you should deallocate it. 
Deallocation is also referred to as "freeing" the memory.  
  
To deallocate memory use the `free()` function of `<stdlib.h>`.

> It is considered a good practice to set a pointer to NULL after freeing 
memory so that you cannot accidentally continue using it.
> If you continue using memory after it has been freed you may corrupt data
from other programs or even another part of your own program.

## Memory leaks
Happens when dynamic memory is allocated but never freed.  
There is a risk of a memory leak if a pointer to dynamic memory is lost 
before the memory can be freed.  
Some common cases where memory is leaked:
- Overwriting the pointer.
- Pointer exist only inside a function.
- The pointer gets lost when reallocation fails.
