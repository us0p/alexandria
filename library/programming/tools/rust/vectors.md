Allows you to store more than one value in a single data structure that puts all the values next to each other in memory.

Vectors can only store values of the same type.
```rust
let v: Vec<i32> = Vec::new();
```

Because we aren't inserting any values in this vector, we need to add a type annotation.

You can use the `vec!` macro, which will create a new vector that holds the values you give it.
```rust
let v = vec![1, 2, 3];
```
## Updating a Vector
As with any variable, if we want to be able to change its value, we need to make it mutable.
```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
```
## Reading elements of Vectors
There are two ways to reference a value stored in a vector:
	- Indexing.
	- The `get` method.

```rust
// Types were added for clarity
let v = vec![1, 2, 3, 4, 5];

// Note that the get the reference to that value
let third: &i32 = &v[2];
println!("The third element is {third}");

let third: Option<&i32> = v.get(2);
match third {
	Some(third) => println!("The third element is {third}"),
	None => println!("There is no third element."),
}
```

If you try to access an index value outside the range of existing elements your program will crash. You can choose to use `get` and use an `Option` to avoid panicking.

When the program has a valid reference, the borrow checker enforces the ownership and borrowing rules to ensure this reference and any other reference to the contents of the vector remain valid.
```rust
let mut v = vec![1, 2, 3, 4, 5];
let first = &v[0];
v.push(6);
println!("The first element is: {first}"); // crashes use of immutable reference after mutable borrow in the same scope.
```
## Iterating over the values in a Vector
```rust
let v = vec![100, 32, 57];

// loop to get immutable references to each element in a vector.
for i in &v {
	println!("{i}");
}

// loop to get mutable reference to each element in a mutable vector.
let mut v = vec![100, 32, 57];
for i in &mut v {
	*i += 50;
}
```

To change the value that the mutable reference refers to, we have to use the `*` dereference operator to get to the value in `i` before we can use the `+=` operator.

The reference to the vector that the `for` loop holds prevents simultaneous modification of the whole vector.
## Using an Enum to store multiple types
Vectors can only store values that are of the same type. Fortunately, the variants of an enum are defined under the same enum type.
```rust
enum SpreadsheetCell {
	Int(i32),
	Float(f64),
	Text(String),
}

let row = vec![
	SpreadsheetCell::Int(3),
	SpreadsheetCell::Text(String::from("blue")),
	SpreadsheetCell::Float(10.12),
]
```

Rust needs to know what types will be in the vector at compile time so it knows exactly how much memory on the heap will be needed to store each element.

If you don't know the exhaustive set of types a program will get at runtime to store in a vector, the enum technique won't work. Instead, you can use a trait object.
## Dropping a Vector drops its elements
Like any other `struct`, a vector is freed when it goes out of scope.
```rust
{
	let v = vec![1, 2, 3, 4];
	// do stuff with v
} // <- v goes out of scope and is freed here
```

When a vector gets dropped, all of its contents are also dropped.