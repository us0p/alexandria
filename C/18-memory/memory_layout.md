# Memory Layout
A typical memory representation of a C program consists of:
1. Text segment
2. Initialized data segment
3. Uninitialized data segment (bss)
4. Stack
5. Heap

![memory layout](https://media.geeksforgeeks.org/wp-content/uploads/memoryLayoutC.jpg "Typical memory layout of a running process")

## Text segment
Is one of the sections of a program in an object file or memory, which 
contains executable instructions.  
As a memory region, a text segment may be placed below the heap or stack in
order to prevent heaps and stack overflows from overwriting it.  
Usually, the text segment is sharable so that only a single copy needs to 
be in memory for frequently executed programs.  
Also, the text segment is often read-only, to prevent a program from 
accidentally modifying its instructions.  

## Initialized data segment
A data segment is a portion of the virtual address space of a program, 
which contains the global variables and static variables that are 
initialized by the programmer.  
Note that, the data segment is not read-only, since the values of the 
variables can be altered at run time.  
This segment can be further classified into the initialized read-only area
and the initialized read-write area.  

```C
    chas s[] = "hello world"; // read-write area;

    // string literal initialized in read-only
    // character pointer variable initialized to read-write area;
    // you can change the address `s2` points to, but you can change the 
    // content of its address;
    const char* s2 = "s2"; 

    int main(void) {
        // ...
    }
```

## Uninitialized segment
Often called `bss` segment, named after an assembler operator that stood 
for **block started by symbol**.  
Data in this segment is initialized by the compiler to 0 before the program
starts executing.  
It starts at the end of the data segment and contains all global variables
and static variables that are initialized to zero or do not have explicit 
initialization in source code.  

```C
    int main(void) {
        int j; // initialized to 0 in the uninitialized segment;
    }
```

## Stack
Traditionally, it adjoined the Heap area and grew in opposite directions, 
when the stack pointer met the heap pointer, free memory was exhausted.  
With modern large address spaces and virtual memory techniques they may be
placed almost anywhere, but they still typically grow in opposite 
directions.  
It contains the program stack, a `LIFO` structure, typically located in the
higher parts of memory. On the standard PC x86 computer architecture, it 
grows toward address zero; on some other architectures, it grows in the 
opposite direction. A “stack pointer” register tracks the top of the stack;
it is adjusted each time a value is “pushed” onto the stack. The set of 
values pushed for one function call is termed a “stack frame”; A stack 
frame consists at minimum of a return address.
It's where automatic variables are stored, along with information that is 
saved each time a function is called. Each time a function is called, the 
address of where to return to and certain information about the caller’s 
environment, such as some of the machine registers, are saved on the stack.
The newly called function then allocates room on the stack for its 
automatic variables. This is how recursive functions in C can work. Each 
time a recursive function calls itself, a new stack frame is used, so one 
set of variables doesn’t interfere with the variables from another instance
of the function.

## Heap
Heap is the segment where dynamic memory allocation usually takes place.  
The heap area begins at the end of the BSS segment and grows to larger 
addresses from there.  
The Heap area is managed by `malloc`, `calloc`, `realloc`, and `free`, 
which may use the `brk` and `sbrk` system calls to adjust its size.  
Note that the use of `brk/sbrk` and a single “heap area” is not required to
fulfill the contract of `malloc`/`calloc`/`realloc`/`free`; they may also 
be implemented using mmap to reserve potentially non-contiguous regions of
virtual memory into the process’ virtual address space.  
The Heap area is shared by all shared libraries and dynamically loaded 
modules in a process.  

