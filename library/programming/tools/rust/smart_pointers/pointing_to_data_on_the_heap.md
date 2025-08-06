Boxes allows you to store data on the heap rather than the stack. What remains on the stack is the pointer to the heap data.

Boxes don't have performance overhead, other than storing their data on the heap instead of on the stack.

Most used when:
- You have a type whose size can’t be known at compile time and you want to use a value of that type in a context that requires an exact size
- You have a large amount of data and you want to transfer ownership but ensure the data won’t be copied when you do so
- You want to own a value and you care only that it’s a type that implements a particular trait rather than being of a specific type

>Transferring ownership of a large amount of data can take a long time because the data is copied around on the stack.

```Rust
fn main() {
	let b = Box::new(5); // stores i32 value on the heap.
	println!("b = {b}");
}
```

Just like any owned value, when a box goes out of scope, as `b` does at the end of `main`, it will be deallocated.
## Enabling Recursive Types with Boxes
A value of a _recursive type_ can have another value of the same type as part of itself.

Recursive types pose an issue because Rust needs to know at compile time how much space a type takes up. However, the nesting of values of recursive types could theoretically continue infinitely, so Rust can’t know how much space the value needs.

Because boxes have a known size, we can enable recursive types by inserting a box in the recursive type definition.

```Rust
// Doesn't compile, "List has infinite size"
enum List {
	Cons(i32, List),
	Nil
}
```

> "Infinite size" errors usually recommend adding an indirection to solve the problem. Indirection means that instead of storing a value directly, we should change the data structure to store the value indirectly by storing a pointer to the value instead.

```Rust
enum List {
	Const(
		i32, 
		Box<List> // Added indirection represent a pointer to the heap instead of actually holding the data.
	),
	Nil
}
```

Enums instances can hold only one value at the time, so the space needed for each instance of an enum is equal to the biggest space an enum instance can have.

In the case above, an instance of `List` will have always have an space of `i32 + Pointer size (Box)`.

>Boxes provide only the indirection and heap allocation; they don’t have any other special capabilities.