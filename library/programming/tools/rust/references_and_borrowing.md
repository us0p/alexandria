# References and Borrowing
A _reference_ is like a pointer in that it’s an address we can follow to access the data stored at that address; that data is owned by some other variable.

- At any given time, you can have _either_ one mutable reference _or_ any number of immutable references.
- References must always be valid.

Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference.
```rust
fn main() {
	let s1 = String::from("hello");

	let len = calculate_length(&s1);

	println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize { // s is a reference to a String
    s.len()
} // Here, s goes out of scope. But because s does not have ownership of what
  // it refers to, the value is not dropped.
```

In the code above the `calculate_length` function has a reference to an object as a parameter instead of taking ownership of the value.

>Ampersands are used to represent *references* and allow you to reference some value without taking ownership.

When functions have references as parameters instead of the actual values, we won’t need to return the values in order to give back ownership, because we never had ownership.

We call the action of creating a reference **borrowing**. As in real life, if a person owns something, you can borrow it from them. When you’re done, you have to give it back.

References are immutable by default. It's not possible to change the underlying values of the reference in the code above. To do so, both the reference and the owner must be annotated as mutable:
```rust
fn main() {
	let mut s1 = String::from("hello");

	let len = calculate_length(&mut s1);

	println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &mut String) -> usize { // s is a reference to a String
	s.push_str(", world!");
    s.len()
} // Here, s goes out of scope. But because s does not have ownership of what
  // it refers to, the value is not dropped.
```

This makes very clear that the function will mutate the value it borrows.

If you have one mutable reference to a value, you can have no other references to that value. The benefit of having this restriction is that Rust can prevent data races at compile time.

A _data race_ is similar to a race condition and happens when these three behaviors occur:

- Two or more pointers access the same data at the same time.
- At least one of the pointers is being used to write to the data.
- There’s no mechanism being used to synchronize access to the data.

Data races cause undefined behavior and can be difficult to diagnose and fix when you’re trying to track them down at runtime;
```rust
let mut s = String::from("hello");

let r1 = &mut s; // ok
let r2 = &mut s; // error

println!("{}, {}", r1, r2); // error

// If you really need to create two mutable references:
{
	let r1 = &mut s;
}// r1 goes out of scope
let r2 = &mut s;
```

A similar rule is enforced to combine immutable and mutable references. Users of an immutable reference don’t expect the value to suddenly change out from under them.

A reference’s scope starts from where it is introduced and continues through the last time that reference is used. The scopes must not overlap.

The compiler can tell that the reference is no longer being used at a point before the end of the scope.
```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
let r3 = &mut s; // BIG PROBLEM

println!("{}, {}, and {}", r1, r2, r3); // overlaping scopes of mutable and immutable references

// Same example, without overlaping scopes
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
println!("{r1} and {r2}");
// variables r1 and r2 will not be used after this point

let r3 = &mut s; // no problem
println!("{r3}");
```
## Dangling References
Is a pointer that references a location in memory that may have been given to someone else by freeing some memory while preserving a pointer to that memory.

In Rust, the compiler guarantees that references will never be dangling references.
```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
} // Here, s goes out of scope, and is dropped. Its memory goes away.
  // Danger!

// This example works because ownership is moved out
fn no_dangle() -> String {
	let s = String::from("hello");

	s
}
```