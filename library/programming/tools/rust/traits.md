A trait defines the functionality a particular type has and can share with other types.

Traits are similar to **interfaces** in other languages, although with some differences.
## Defining a Trait
A type's behavior consists of the methods we call on that type. Different types share the same behavior if we can call the same methods on all of those types. Trait definitions are a way to group method signatures together to define a set of behaviors necessary to accomplish some purpose.
```rust
pub trait Summary {
	fn summarize(&self) -> String;
}
```

Inside the curly brackets, we declare the method signatures that describe the behaviors of the types that implement this trait.

A trait can have multiple methods in its body, the method signatures are listed one per line, and each line ends in a semicolon.
## Implementing a Trait on a Type
```rust
pub struct NewsArticle {
	pub headline: String,
	pub location: String,
	pub author: String,
	pub content: String,
}

impl Summary for NewsArticle {
	fn summarize(&self) -> String {
		format!("{}, by {} ({})", self.headline, self.author, self.location)
	}
}

pub struct Tweet {
	pub usename: String,
	pub content: String,
	pub reply: bool,
	pub retweet: bool,
}

impl Summary for Tweet {
	fn summarize(&self) -> String {
		format!("{}: {}", self.username, serl.content)
	}
}
```

Users can call the trait methods on instances of `NewsArticle` and `Tweet` in the same way we call regular methods. The only difference is that the user must bring the trait into scope as well as the types.
```rust
use aggregator::{Summary, Tweet};

fn main() {
	let tweet = Tweet {
		username: String::from("horse_ebooks"),
		content: String::from("of course, as you probably already know, people"),
		reply: false,
		retweet: false,
	};

	println!("1 new tweet: {}", tweet.summarize());
}
```

One restriction to note is that we can implement a trait on a type only if either the trait or the type, or both, are local to our crate. For example, we can implement standard library traits like `Display` on a custom type like `Tweet` as part of our `aggregator` crate functionality because the type `Tweet` is local to our `aggregator` crate. We can also implement `Summary` on `Vec<T>` in our `aggregator` crate because the trait `Summary` is local to our `aggregator` crate.

But we can’t implement external traits on external types. For example, we can’t implement the `Display` trait on `Vec<T>` within our `aggregator` crate because `Display` and `Vec<T>` are both defined in the standard library and aren’t local to our `aggregator` crate. This restriction is part of a property called **coherence**, and more specifically the **orphan rule**, so named because the parent type is not present. This rule ensures that other people’s code can’t break your code and vice versa. Without the rule, two crates could implement the same trait for the same type, and Rust wouldn’t know which implementation to use.
## Default  implementation
Sometimes it's useful to have default behavior for some or all of the methods in a trait instead of requiring implementations for all methods on every type. Then, as we implement the trait on a particular type, we can keep or override each method's default behavior.
```rust
pub trait Summary {
	fn summarize(&self) -> String {
		String::from("(Read more...)")
	}
}

// Implementing default trait.
impl Summary for NewsArticle {};
```

The syntax for overriding a default implementation is the same as the syntax for implementing a trait method that doesn't have a default implementation.

Default implementations can call other methods in the same trait, even if those other methods don't have a default implementation.
```rust
pub trait Summary {
	fn summarize_author(&self) -> String;

	fn summarize(&self) -> String {
		format!("(Read more from {}...)", self.summarize_author())
	}
}
```
## Trait as Parameters
```rust
pub fn notify(item: &impl Summary) {
	println!("Breaking news! {}", item.summarize());
}
```

This parameter accepts any type that implements the specified trait.
## Trait Bound Syntax
The `impl Trait` syntax works for straightforward cases but is actually syntax sugar for a longer form known as a `trait bound`.
```rust
pub fn notify<T: Summary>(item: &T) {
	println!("Breaking new! {}", item.summarize());
}
```
## Specifying Multiple Trait Bounds
```rust
pub fn notify(item: &(impl Summary + Display)) { /*...*/}

// Or by using trait bound syntax
pub fn notify<T: Summary + Display>(item: &T) { /*...*/}
```

The function above specifies that the `item` parameter must implement both `Display` and `Summary`.
## Clearer Trait Bounds with `where` Clauses
Using too many trait bounds can make the signature difficult to read. For this reason, Rust has alternate syntax for specifying trait bounds inside a `where` clause after the function signature:
```rust
// long signature
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
	// ...
}

// short signature with `where` clause
fn some_function<T, U>(t: &T, u: &U) -> 32
where
	T: Display + Clone,
	U: Clone + Debug,
{
	// ...
}
```
## Returning types that implement Traits
```rust
fn returns_summarizable() -> impl Summary {
	// ...
}
```

Note however, you can only use `impl Trait` if you're returning a single type.
```rust
// This code won't compile as it tries to return different types.
// Even though they implement the same Trait.
fn returns_summarizable(switch: bool) -> impl Summary {
	if switch {
		NewsArticle {
			// ...
		}
	} else {
		Tweet {
			// ...
		}
	}
}
```
## Using Trait Bounds to conditionally implement methods
```rust
use std::fmt::Display;

struct Pair<T> {
	x: T,
	y: T,
}

// Applicable to all types under Pair
impl <T> Pair<T> {
	fn new(x: T, y: T) -> Self {
		Self {x, y}
	}
}

// This method is present only if the underlying type implements both traits.
impl<T: Display + PartialOrd> Pair<T> {
	fn cmp_display(&self) {
		if self.x >= self.y {
			println!("The largest member is x = {}", self.x);
		} else {
			println!("The largest member is y = {}", self.y);
		}
	}
}
```

We can also conditionally implement a trait for any type that implements another trait.

Implementations of a trait on any type that satisfies the trait bounds are called **blanked implementations**.
```rust
// Implements the trait `ToString` for any type that also implements `Diplay`.
impl<T: Display> ToString for T {
	// ...
}
```