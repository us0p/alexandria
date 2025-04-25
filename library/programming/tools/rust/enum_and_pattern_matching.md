## Defining an Enum
Enums give you a way of saying a value is one of a possible set of values.
```rust
enum IpAddrKind {
	V4,
	V6,
}

fn main() {
	let four = IpAddrKind::V4;
	let six = IpAddrKind::V6;
}
```

We can put data directly into each enum variant.
```rust
// Both V4 and V6 will have associated String values
enum IpAddr {
	V4(String),
	V6(String),
}

// Data is attached to each variant of the enum directly.
let home = IpAddre::V4(String::from("127.0.0.1"));
let loopback = IpAddr::V6(String::from("::1"));
```

From the above example you can see that the name of each enum variant that we define also becomes a function that constructs an instance of the enum.

`IpAddr::V4()` is a function call that takes a `String` argument and returns an instance of the `IpAddr` type.

Also, each variant can have different types and amounts of associated data.
```rust
enum IpAddr {
	V4(u8, u8, u8, u8),
	V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```
## Methods
```rust
enum Message {
	Quit,                       // No data associated
	Move {x: i32, y: i32},      // named fields like a struct does
	Write(String),              // includes a single String
	ChangeColor(i32, i32, i32), // includes three i32 values like a tuple does
}

impl Message {
	fn call(&self) {
		// definition
	}
}

let m = Message::Write(String::from("hello"));
m.call();
```
## The Option enum and its advantages over Null Values
The `Option` type encodes the very common scenario in which a value could be something or it could be nothing.

Rust doesn't have the null feature that many other languages have. Null is a value that means there is no value there.

The problem with null values is that if you try to use a null value as a not-null value, you’ll get an error of some kind. Because this null or not-null property is pervasive, it’s extremely easy to make this kind of error.

However, the concept that null is trying to express is still a useful one: a null is a value that is currently invalid or absent for some reason.

The problem isn’t really with the concept but with the particular implementation. As such, Rust does not have nulls, but it does have an enum that can encode the concept of a value being present or absent. This enum is `Option<T>`, and it is defined by the standard library:
```rust
enum Option<T> {
	None,
	Some(T), 
}
```

This enum is so useful that it's even included in the prelude. Its variants are also included in the prelude, you can use `Some` and `None` directly without the `Option::` prefix.
```rust
// Rust can infer the type of the variable by using the value provided to 'Some'.
let some_number = Some(5); // is type Option<i32>
let some_char  = Some('e'); // is type Option<char>

// It can't infer the value of None, thus we need to explicity define the type.
let absent_number: Option<i32> = None;
```

Why is having `Option<T>` any better than having null? 

In short, because `Option<T>` and `T` (where `T` can be any type) are different types, the compiler won’t let us use an `Option<T>` value as if it were definitely a valid value.
```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

// Error: cannot add `Option<i8>` to `i8`
let sum = x + y;
```