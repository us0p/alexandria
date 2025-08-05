Memory is managed through a system of ownership with a set of rules that the compiler checks. If any of the rules are violated, the program won't compile. None of the features of ownership will slow down your program while it's running.

Keeping track of what parts of code are using what data on the [heap](stack_and_heap.md#Heap), minimizing the amount of duplicate data on the heap, and cleaning up unused data on the heap so you don’t run out of space are all problems that ownership addresses.

Once you understand ownership, you won’t need to think about the [stack](stack_and_heap.md#Stack) and the heap very often, but knowing that the main purpose of ownership is to manage heap data can help explain why it works the way it does.
## Ownership Rules
- Each value in Rust has an owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.
## The String type
We'll concentrate on parts of `String` that relate to ownership. These aspects also apply to other complex data types, whether they are provided by the standard library or created by you.

This type manages data allocated on the heap and as such is able to store an amount of text that is unknown to us at compile time.
```rust
// Creates a String from a string literal.
let s = String::from("hello");

// literal string are immutable, but the String type can be mutated.
s.push_str(", world!");

println!("{s}"); // hello, world!
```
## Memory and Allocation
With the `String` type, in order to support a mutable, growable piece of text, we need to allocate an amount of memory on the heap, unknown at compile time, to hold the contents. This means:
- The memory must be requested from the memory allocator at runtime.
- We need a way of returning this memory to the allocator when we’re done with our `String`.

In Rust the memory is automatically returned once the variable that owns it goes out of scope.
```rust
{
	let s = String::from("hello"); // s is valid from this point forward
	
	// do stuff with s
} // this scope is over, and s is no longer valid
```

When a variable goes out of scope, Rust calls `drop`. Rust calls `drop` automatically at the closing curly bracket.
## Double Free
```rust
let s1 = String::from("hello");
let s2 = s1;

println!("{s1}, world!");
```

When `s2` and `s1` go out of scope, they will both try to free the same memory. This is known as a _double free_ error. Freeing memory twice can lead to memory corruption, which can potentially lead to security vulnerabilities.

To ensure memory safety, after the line `let s2 = s1;`, Rust considers `s1` as no longer valid. Therefore, Rust doesn’t need to free anything when `s1` goes out of scope. If you try to run the code above you'll get an error because Rust prevents you from using the invalidated reference:
```plaintext
...
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |
5 |     println!("{s1}, world!");
  |               ^^^^ value borrowed here after move
  |
...
help: consider cloning the value if the performance cost is acceptable
  |
3 |     let s2 = s1.clone();
  |                ++++++++
...
```

If you’ve heard the terms _shallow copy_ and _deep copy_ while working with other languages, the concept of copying the pointer, length, and capacity without copying the data probably sounds like making a shallow copy. But because Rust also invalidates the first variable, instead of being called a shallow copy, it’s known as a **move**.

In addition, there’s a design choice that’s implied by this: Rust will never automatically create “deep” copies of your data. Therefore, any _automatic_ copying can be assumed to be inexpensive in terms of runtime performance.
## Scope and Assignment
When you assign a completely new value to an existing variable, Rust will call `drop` and free the original value’s memory immediately.
```rust
let mut s = String::from("hello");
s = String::from("ahoy");

println!("{s}, world!");
```

The string thus immediately goes out of scope. Rust will run the `drop` function on it and its memory will be freed right away.
## Variables and Data Interacting with Clone
If we _do_ want to deeply copy the heap data of the `String`, not just the stack data, we can use a method called `clone`.
```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("s1 = {s1}, s2 = {s2}");
```

In this example the heap data _does_ get copied. When you see a call to `clone`, you know that some arbitrary code is being executed and that code may be expensive.
## Stack-Only Data: Copy
```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

This code seems to contradict what we just learned: we don’t have a call to `clone`, but `x` is still valid and wasn’t moved into `y`.

The reason is that types such as integers that have a known size at compile time are stored entirely on the stack, and you don't need to return them to the allocator.

Rust has a special annotation called the `Copy` trait that we can place on types that are stored on the stack, as integers are. If a type implements the `Copy` trait, variables that use it do not move, but rather are trivially copied, making them still valid after assignment to another variable.

Rust won’t let us annotate a type with `Copy` if the type, or any of its parts, has implemented the `Drop` trait.

As a general rule, any group of simple **scalar values** can implement `Copy`, and nothing that requires allocation or is some form of resource can implement `Copy`.
- Special case: `Tuples`. If they only contain types that also implement `Copy`. For example, `(i32, i32)` implements `Copy`, but `(i32, String)` does not.
## Ownership and Functions
The mechanics of passing a value to a function are similar to those when assigning a value to a variable. Passing a variable to a function will move or copy, just as assignment does.
```rust
fn main() {
    let s = String::from("hello");  // s comes into scope

    takes_ownership(s);             // s's value moves into the function...
                                    // ... and so is no longer valid here

    let x = 5;                      // x comes into scope

    makes_copy(x);                  // because i32 implements the Copy trait,
                                    // x does NOT move into the function,
    println!("{}", x);              // so it's okay to use x afterward

} // Here, x goes out of scope, then s. But because s's value was moved, nothing
  // special happens.

fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{some_string}");
} // Here, some_string goes out of scope and `drop` is called. The backing
  // memory is freed.

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{some_integer}");
} // Here, some_integer goes out of scope. Nothing special happens.
```

If we tried to use `s` after the call to `takes_ownership`, Rust would throw a compile-time error. These static checks protect us from mistakes.
## Return Values and Scope
Returning values can also transfer ownership.
```rust
fn main() {
    let s1 = gives_ownership();         // gives_ownership moves its return
                                        // value into s1

    let s2 = String::from("hello");     // s2 comes into scope

    let s3 = takes_and_gives_back(s2);  // s2 is moved into
                                        // takes_and_gives_back, which also
                                        // moves its return value into s3
} // Here, s3 goes out of scope and is dropped. s2 was moved, so nothing
  // happens. s1 goes out of scope and is dropped.

fn gives_ownership() -> String {             // gives_ownership will move its
                                             // return value into the function
                                             // that calls it

    let some_string = String::from("yours"); // some_string comes into scope

    some_string                              // some_string is returned and
                                             // moves out to the calling
                                             // function
}

// This function takes a String and returns one
fn takes_and_gives_back(a_string: String) -> String { // a_string comes into
                                                      // scope

    a_string  // a_string is returned and moves out to the calling function
}
```