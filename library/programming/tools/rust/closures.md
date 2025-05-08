# Closures: Anonymous functions that capture their environment
Are anonymous functions you can save in a variable or pass as arguments to other functions.

You can create the closure in one place and then call the closure elsewhere to evaluate it in a different context.

Unlike functions, closures can capture values from the scope in which they're defined.
## Capturing the environment with closures
```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
	Red,
	Blue,
}

struct Inventory {
	shirts: Vec<ShirtColor>,
}

impl Inventory {
	fn giveaway(&self, user_preference: Option<ShirtColor>) -> ShirtColor {
		user_preference
		.unwrap_or_else(|| self.most_stocked())
	}

	fn most_stocked(&self) -> ShirtColor {
		let mut num_red = 0;
		let mut num_blue = 0;

		for color in &self.shirts {
			match color {
				ShirtColor::Red => num_red += 1,
				ShirtColor::Blue => num_blue += 1,
			}
		}
		if num_red > num_blue {
			ShirtColor::Red
		} else {
			ShirtColor::Blue
		}
	}
}

fn main() {
	let store = Inventory {
		shirts: vec![ShirtColor::Blue, ShirtColor::Red, ShirtColor::Blue],
	};

	let user_pref1 = Some(ShirtColor::Red);
	let giveaway1 = store.giveaway(user_pref1);
	println!(
		"The user with preference {:?} gets {:?}",
		user_pref1, giveaway1
	);

	let user_pref2 = None;
	let giveaway2 = store.giveaway(user_pref2);
	println!(
		"The user with preference {:?} gets {:?}",
		user_pref2, giveaway2
	);
}
```

The `unwrap_or_else` method on `Option<T>` is defined by the standard library. It takes one argument, a closure without any arguments that returns a value `T`, the same type stored in the `Some` variant of the `Option<T>`.

The closure captures an immutable reference to the `self` `Inventory` instance and passes it with the code we specify to the `unwrap_or_else` method. Functions, on the other hand, are not able to capture their environments in this way.
## Closure type inference and annotation
Closures don't usually require you to annotate the types of the parameters or the return value like `fn` functions do.

Closures aren't used in a exposed interface like functions, they're stored in variables and used without naming them and exposing them to users or your library.

There are rare cases where the compiler needs closure type annotations too.

As with variables, we can add type annotations if we want to increase explicitness and clarity at the cost of being more verbose than is strictly necessary.
```rust
let expensive_closure = |num: u32| -> u32 {
	println!("calculating slowly...");
	thread::sleep(Duration::from_secs(2));
	num
};

// This illustrates how closure syntax is similar to function syntax except for the use of pipes and the amount of syntax that is optional.
fn  add_one_v1 (x: u32) -> u32 { x + 1 };
let add_one_v2 |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|           { x + 1 };
let add_one_v4 = |x|             x + 1  ;
```

Brackets are optional because the closure body has only one expression.

The `add_one_v3` and `add_one_v4` lines require the closures to be evaluated to be able to compile because the types will be inferred from their usage. This is similar to `let v = Vec::new()` needing either type annotations or values of some type to be inserted into the `Vec` for Rust to be able to infer the type.

For closure definitions, the compiler will infer one concrete type for each of their parameters and for their return value.
```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Note that we haven’t added any type annotations to the definition. Because there are no type annotations, we can call the closure with any type, which we’ve done here with `String` the first time. If we then try to call `example_closure` with an integer, we’ll get an error.

The first time we call `example_closure` with the `String` value, the compiler infers the type of `x` and the return type of the closure to be `String`. Those types are then locked into the closure in `example_closure`, and we get a type error when we next try to use a different type with the same closure.
## Capturing references or moving ownership
Closures can capture values from their environment in three ways, which directly map to the three ways a function can take a parameter, borrowing immutably/mutably, and taking ownership. The closure will decide which of these to use based on what the body of the function does with the captured values.
```rust
fn main() {
	let list = vec![1, 2, 3];
	println!("Before defining closure: {list:?}");

	// captures an immutable reference to the the vector.
	let only_borrows = || println!("From closure: {list:?}");

	println!("Before calling closure: {list:?}");
	only_borrows();
	println!("After calling closure: {list:?}");
}
```

This example also illustrates that a variable can bind to a closure definition, and we can later call the closure by using the variable name and parentheses as if the variable name were a function name.
```rust
fn main() {
	let mut list = vec![1, 2, 3];
	println!("Before defining closure: {list:?}");

	// captures a mutable reference to the vector.
	let mut borrows_mutably = || list.push(7);

	borrows_mutably();
	println!("After calling closure: {list:?}");
}
```

Note that there’s no longer a `println!` between the definition and the call of the `borrows_mutably` closure: when `borrows_mutably` is defined, it captures a mutable reference to `list`. We don’t use the closure again after the closure is called, so the mutable borrow ends.

If you want to force the closure to take ownership of the values it uses in the environment even though the body of the closure doesn't strictly need ownership, you can use the `move` keyword before the parameter list.

This technique is mostly useful when passing a closure to a new thread to move the data so that it's owned by the new thread.
```rust
use std::thread;

fn main() {
	let list vec![1, 2, 3];
	println!("Before defining closure: {list:?}");

	thread::spawn(move || println!("From thread: {list:?}"))
		.join()
		.unwrap();
}
```

In this example, even though the closure body still only needs an immutable reference, we need to specify that `list` should be moved into the closure by putting the `move` keyword at the beginning of the closure definition.

The new thread might finish before the rest of the main thread finishes, or the main thread might finish first. If the main thread maintained ownership of `list` but ended before the new thread did and dropped `list`, the immutable reference in the thread would be invalid.

Therefore, the compiler requires that `list` be moved into the closure given to the new thread so the reference will be valid.
## Moving captured values out of closures and the `fn` traits
A closure body can do any of the following: move a captured value out of the closure, mutate the captured value, neither move nor mutate the value, or capture nothing from the environment to begin with.

The way a closure captures and handles values from the environment affects which traits the closure implements, and traits are how functions and structs can specify what kinds of closures they can use. Closures will automatically implement one, two, or all three of these `Fn` traits, in an additive fashion, depending on how the closure’s body handles the values:
1. `FnOnce` applies to closures that can be called once. All closures implement at least this trait, because all closures can be called. A closure that moves captured values out of its body will only implement `FnOnce` and none of the other `Fn` traits, because it can only be called once.
2. `FnMut` applies to closures that don’t move captured values out of their body, but that might mutate the captured values. These closures can be called more than once.
3. `Fn` applies to closures that don’t move captured values out of their body and that don’t mutate captured values, as well as closures that capture nothing from their environment. These closures can be called more than once without mutating their environment, which is important in cases such as calling a closure multiple times concurrently.
```rust
impl<T> Option<T> {
	// definition of the unwrap_or_else method on Option<T>.
	pub fn unwrap_or_else<F>(self, f: F) -> T
	where
		F: FnOnce() -> T
	{
		match self {
			Some(x) => x,
			None => f(),
		}
	}
}
```

The trait bound specified on the generic type `F` is `FnOnce() -> T`, which means `F` must be able to be called once, take no arguments, and return a `T`. Using `FnOnce` in the trait bound expresses the constraint that `unwrap_or_else` is only going to call `f` at most one time. In the body of `unwrap_or_else`, we can see that if the `Option` is `Some`, `f` won’t be called. If the `Option` is `None`, `f` will be called once. Because all closures implement `FnOnce`, `unwrap_or_else` accepts all three kinds of closures and is as flexible as it can be.

Note: If what we want to do doesn’t require capturing a value from the environment, we can use the name of a function rather than a closure. For example, we could call `unwrap_or_else(Vec::new)` on a `Option<Vec<T>>` value to get a new, empty vector if the value is `None`. The compiler automatically implements whichever of the `Fn` traits is applicable for a function definition.
```rust
#[derive(Debug)]
struct Rectangle {
	width: u32,
	height: u32,
}

fn main() {
	let mut list = [
		Rectangle { width: 10, height: 1 },
		Rectangle { width: 3, height: 5 },
		Rectangle { width: 7, height: 12 },
	];

	let mut sort_operations = vec![];
	let value = String::from("closure called");

	// sort_by_key uses FnMut.
	// Gets a reference to the current item in the slice being considered
	// Returns a value of type K that can be ordered.
	list.sort_by_key(|r| r.width);
	println!("{list:#?}");

	// Code doesn't compile, this closure implement FnOnce as it moves values out of its body but sort_by_key is called for every element in the vector.
	// The closure captures value then moves value out of the closure by transferring ownership of value to the sort_operations vector.
	list.sort_by_key(|r| {
		sort_operations.push(value);
		r.width
	});

	// This works because it is only capturing a mutable reference to the num_sort_operations counter and can therefore be called more than once.
	let mut num_sort_operations = 0;
	list.sort_by_key(|r| {
		num_sort_operations += 1;
		r.width
	});
}
```