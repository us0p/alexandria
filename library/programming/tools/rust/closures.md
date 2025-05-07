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