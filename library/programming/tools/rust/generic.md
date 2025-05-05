Generics allow us to replace specific types with a placeholder that represents multiple types to remove duplication.
## In Functions
To parametrize the types in a generic you need to name the type parameter. You can use any identifiers as a type parameter name. But `T` is used by convention.
```rust
fn largest<T>(list: &[T]) -> &T {
	let mut largest = &list[0];

	for item in list {
		if item > largest{
			largest = item;
		}
	}

	largest
}

fn main() {
	let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

While the code above correctly represents the representation of a generic function, it won't compile.

For now, know that this error states that the body of largest won’t work for all possible types that T could be. Because we want to compare values of type T in the body, we can only use types whose values can be ordered. To enable comparisons, the standard library has the `std::cmp::PartialOrd` trait that you can implement on types
```rust
use std::cmp::PartialOrd

fn lasrget<T: PartialOrd>(list: &[T]) -> &T {
	// ...
}

// rest of the code
```

By restricting the types valid for `T` to only those that implement `PartialOrd` and this example will compile, because the standard library implements `PartialOrd` on both `i32` and `char`.
## In Structs
```rust
struct Point <T> {
	x: T,
	y: T,
}

// You can use multiple generics to use different types
struct Points<T, U> {
	x: T,
	y: U
}

fn main() {
	// The type if inferred in structs
	let integer = Point{x: 5, y: 10};
	let float = Point{x: 1.0, y: 4.0};

	let integer_and_float = Points{x: 5, y: 4.0};	
}
```
## In Enums
Let's look at some enums in the standard library
```rust
enum Option<T> {
	Some(T),
	None,
}

enum Result<T, E> {
	Ok(T),
	Err(E),
}
```

As you can se we use the same notation as in structs to represent generics and this is present in a lot of default types in the standard library.
## In Methods
```rust
struct Point<T> {
	x: T,
	y: T,
}

// We must use impl<T> to signal rust the Point<T> is a generic rather a concrete type.
impl<T> Point<T> {
	fn x(&self) -> &T {
		&self.x
	}
}

// This method will be implemented only in Points that uses the f32 type.
impl Point<f32> {
	fn distance_from_origin(&self) -> f32 {
		(self.x.powi(2) + self.y.powi(2)).sqrt()
	}
}

fn main() {
	let p = Point{x: 5, y: 10};

	println!("p.x = {}", p.x());
}
```

Generic type parameters in structs might not be the same as those you use in that struct's method signatures.
```rust
struct Point<X1, Y1> {
	x: X1,
	y: Y1,
}

impl<X1, Y1> Point<X1, Y1> {
	fn mixup<X2, Y2>(self, other: Point<XY, Y2>) -> Point<X1, Y2> {
		Point{
			x: self.x,
			y: other.y,
		}
	}
}

fn main() {
	let p1 = Point{x: 5, y: 10.4};
	let p2 = Point{x: "Hello", y: 'c'};

	let p3 = p1.mixup(p2);

	println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

The purpose of this example is to demonstrate a situation in which some generic parameters are declared with `impl` and some are declared with the method definition. Here, the generic parameters `X1` and `Y1` are declared after `impl` because they go with the struct definition. The generic parameters `X2` and `Y2` are declared after `fn mixup` because they’re only relevant to the method.
## Performance of code using generics
There's no runtime overhead of using generics in your code.

Rust accomplishes this by performing monomorphization of the code using generics at compile time.

_Monomorphization_ is the process of turning generic code into specific code by filling in the concrete types that are used when compiled.

In this process, the compiler does the opposite of the steps we use to create the generic function, the compiler looks at all the places where generic code is called and generates code for the concrete types the generic code is called with.
```rust
let integer = Some(5);
let float = Some(5.0);
```

When Rust compiles this code, it performs monomorphization. During that process, the compiler reads the values that have been used in `Option<T>` instances and identifies two kinds of `Option<T>`: one is `i32` and the other is `f64`. As such, it expands the generic definition of `Option<T>` into two definitions specialized to `i32` and `f64`, thereby replacing the generic definition with the specific ones.

The monomorphized version of the code looks similar to the following (the compiler uses different names than what we’re using here for illustration):
```rust
enum Option_i32 {
    Some(i32),
    None,
}

enum Option_f64 {
    Some(f64),
    None,
}

fn main() {
    let integer = Option_i32::Some(5);
    let float = Option_f64::Some(5.0);
}
```