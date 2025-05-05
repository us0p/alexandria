A trait defined the functionality a particular type has and can share with other types.

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