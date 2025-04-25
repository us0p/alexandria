Methods are defined within the context of a struct (or an `enum` or a `trait` object) and their first parameter is always `self`.
```rust
struct Rectangle {
	width: u32,
	height: u32,
}

// Implementation block for 'Rectangle'.
impl Rectangle {
	fn area(&self) -> u32 {
		saelf.width * self.height
	}
}

fn main() {
	let rect1 = Rectangle {
		width: 30,
		height: 50,
	}

	println!(
		"The area of the rectangle is {} square pixels.",
		rect1.area()
	);
}
```

Everything within an `impl` block will be associated with the `Rectangle` type.

Each struct is allowed to have multiple `impl` blocks.

`&self` is short for `self: &Self`. Note that we still need to use the `&` in front of the `self` shorthand to indicate that this method borrows the `Self` instance. Methods can take ownership of `self` or borrow it  mutably or immutably.

Rust support getters. They aren't implemented automatically for struct fields.
```rust
impl Rectangle {
	// This could be implemented as a getter.
	fn width(&self) -> bool {
		self.width > 0
	}
}

fn main() {
	let rect = Rectangle {
		width: 30,
		height: 50,
	}

	println!(
		"The width of the Rectangle is:{}. Is it greather than zero: {}",
		rect.width, // Rust knows that we're referencing the field
		rect.width(), // It also knows that we're calling the method
	);
}
```

Rust has a feature called **automatic referencing and dereferencing**. Calling methods is one of the few places in Rust with this behavior.

When you call a method with `object.something()`, Rust automatically adds in `&`, `&mut`, or `*` so `object` matches the signature of the method. The following are the same:
```rust
p1.distance(&p2);
(&p1).distance(&p2);
```
## Associated functions
All functions defined within an `impl` block are called **associated functions**.

We can define associated functions that don't have `self` as their first parameter (and thus aren't methods). This type of functions are often used for constructors that will return a new instance of the struct.
```rust
impl Rectangle {
	fn square(size: u32) -> Self {
		Self{
			width: size,
			height: size,
		}
	}
}
```

The `Self` keyword is an alias to the type that appear after the `impl` keyword.

To call this associated function, we use the `::` syntax with the struct name.
```rust
fn main() {
	let sq = Rectangle::square(3);
}
```

The `::` syntax is used for both associated functions and namespaces created by modules.