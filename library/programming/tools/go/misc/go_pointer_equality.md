# Pointer Equality
Determined by whether two pointers reference the same memory address.
## How it works
- **Same memory address**: If two pointers point to the exact same variable in memory, they are considered equal.
- **Nil pointers**: If both pointers are `nil`, they are also considered equal.
- **Different memory address**: If two pointers point to different variables, even if those variables hold identical values, the pointers themselves are not equal.