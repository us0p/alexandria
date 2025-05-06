## The anatomy of a test function
A test in Rust is a function that's annotated with the `test` attribute. Attributes are metadata about pieces of Rust code.

To change a function into a test function, add `#[test]` on the line before `fn`.

When you run your tests with the `cargo test` command, Rust builds a test runner binary that runs the annotated functions and reports on whether each test function passes or fails.

Tests fail when something in the test function panics. Each test is run in a new thread, and when the main thread sees that a test thread has died, the test is marked as failed.
```rust
pub fn add(left: u64, right: u64) -> u64 {
	left + right
}

#[cfg(test)]
mod tests {
	// tests module is an inner module, we need to bring the code under test in the outer module into scope.
	use super::*;

	#[test] // indicates a test.
	fn it_works() {
		let result = add(2, 2);
		assert_eq!(result, 4); // macro used to perform assertion.
	}

	#[test]
	fn another() {
		panic!("Make this test fail");
	}
}
```
## Useful macros
- `assert!`: receives an argument that evaluates to a Boolean. If `true` nothing happens. If `false`, the macro calls `panic!` to cause the test to fail. You can negate a `false` value with `!`.
- `assert_eq`: receives two parameters and assert that both are equal. Uses `==` under the surface. Values being compared must implement the `PartialEq` and `Debug` traits.
- `assert_ne`: receives two parameters and assert that both aren't equal. Uses `!=` under the surface. Values being compared must implement the `PartialEq` and `Debug` traits.

You can also add a custom message to be printed with the failure message as optional arguments to the macros above. Any arguments specified after the required arguments are passed along to the `format!` macro so you can pass a format string that contains `{}` placeholders and values to go in those placeholders.
## Checking for panics with `should_panic`
The attribute `should_panic` makes the test pass if the code panics, the test fails if the code inside the function doesn't panic.
```rust
pub struct Guess {
	value: i32,
}

impl Guess {
	pub fn new(value: i32) -> Guess {
		if value < 1 || value > 100 {
			panic!("Guess value must be between 1 and 100, got {value}.");
		}

		Guess{ value }
	}
}

#[cfg(test)]
mod test {
	use super::*;

	#[test]
	#[should_panic]
	fn greater_than_100() {
		Guess::new(200);
	}
}
```

Tests that use `should_panice` can be imprecise. A `should_panic` test would pass even if the test panics for a different reason from the one we're expecting. To make it more precise, we can add an optional `expected` parameter to it. The test harness will make sure the failure message contains the provided text.
```rust
// ...

#[test]
#[should_panic(expected = "must be between 1 and 100")]
fn greather_than_100() {
	Guess::new(200);
}
```

The test will pass because the value we put in the `should_panic` attribute's `expected` parameter is a substring of the message that the `Guess::new` function panics with.
## Using `Result<T, E>` in tests
We can write tests that use `Result<T, E>` and return `Err` instead of panicking.
```rust
#[test]
fn it_works() -> Result<(), String> {
	let result = add(2, 2);

	if result == 4 {
		Ok(())
	} else {
		Err(String::from("two plus two does not equal four"))
	}
}
```

Writing tests so they return a `Result<T, E>` enables you to use the question mark operator in the body of tests, which can be a convenient way to write tests that should fail if any operation within them returns an `Err` variant.

You can't use the `#[should_panic]` attribute on tests that use `Result<T, E>`.

To assert that an operation returns an `Err` variant, don't use the question mark operator on the `Result<T, E>` value. Instead, use `assert!(value.is_err())`.