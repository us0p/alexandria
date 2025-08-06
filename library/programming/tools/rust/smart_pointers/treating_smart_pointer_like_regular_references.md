Implementing the `Deref` trait allows you to customize the behavior of the dereference operator `*`.

By implementing `Deref` in such a way that a smart pointer can be treated like a regular reference, you can write code that operates on references and use that code with smart pointers too.

The `Deref` trait, provided by the standard library, requires us to implement one method named `deref` that borrows `self` and returns a reference to the inner data.
```Rust
use std::ops::Deref;

struct MyBox<T>(T);

impl<T> Deref for MyBox<T> {
	// Defines an associated type for the trait to use.
	// It's a different way of declaring a generic parameter.
	type Target = T;

	fn deref(&self) -> &Self::Target {
		&self.0
	}
}

fn main() {
	let x = 5;
	let y = &x;
	let z = MyBox(5);

	assert_eq!(5, x); // pass
	assert_eq!(5, *y); // pass
	assert_eq!(5, *z); // pass
	assert_eq!(5, y); // fail, y is a reference
	assert_eq!(5, z); // fail, x and z are of different types
}
```

Without the `Deref` trait, the compiler can only dereference `&` references.
## Implicit `Deref` coercion with functions and methods
`Deref` coercion converts a reference to a type that implements the `Deref` trait into a reference to another type.

For example, `Deref` coercion can convert `&String` to `&str` because `String` implements the `Deref` trait such that it returns `&str`.

`Deref` coercion is a convenience Rust performs on arguments to functions and methods, and works only on types that implement the `Deref` trait.

It happens automatically when we pass a reference to a particular type’s value as an argument to a function or method that doesn’t match the parameter type in the function or method definition.

A sequence of calls to the `deref` method converts the type we provided into the type the parameter needs.

```Rust
fn hello(name: &str) {
	println!("Hello, {name}!");
}

fn main() {
	let m = MyBox(String::from("Rust"));

	// Deref coercion makes it possible to call hello with a reference to a value of type MyBox<String>.
	hello(&m);
}
```

Here we’re calling the `hello` function with the argument `&m`, which is a reference to a `MyBox<String>` value.

Because we implemented the `Deref` trait on `MyBox<T>`, Rust can turn `&MyBox<String>` into `&String` by calling `deref`. 

Rust calls `deref` again to turn the `&String` into `&str`, which matches the `hello` function’s definition.

When the `Deref` trait is defined for the types involved, Rust will analyze the types and use `Deref::deref` as many times as necessary to get a reference to match the parameter’s type.

The number of times that `Deref::deref` needs to be inserted is resolved at compile time, so there is no runtime penalty for taking advantage of `Deref coercion`.
## How `Deref` coercion interacts with mutability
Similar to how you use the `Deref` trait to override the `*` operator on immutable references, you can use the `DerefMut` trait to override the `*` operator on mutable references.

Rust does deref coercion when it finds types and trait implementations in three cases:
1. From `&T` to `&U` when `T: Deref<Target=U>`
2. From `&mut T` to `&mut U` when `T: DerefMut<Target=U>`
3. From `&mut T` to `&U` when `T: Deref<Target=U>`