# The anatomy of a test function
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
# Controlling how tests are run
`cargo test` compiles your code in test mode and runs the resultant test binary. The default behavior of the binary produced by `cargo test` is to run all the tests in parallel and capture output generated during test runs, preventing the output from being displayed and making it easier to read the output related to the test results.

Use `--` to separate the commands of the compiler and commands of the binary.

Use `--test-threads` and the number of threads you want to use to the test binary.
```bash
# Makes the test run consecutively
cargo test -- --test-threads=1
```

By default, if a test passes, Rust's test library captures anything printed to standard output. If a test fails, we'll see whatever was printed to standard output with the rest of the failure message.
```bash
# Makes passing tests display their output
cargo test -- --show-output
```

We can pass the name of any test function to `cargo test` to run only that test.
```bash
# Runs only the function named test_function
cargo test test_function

# We can also use parts of a test name
# Will run all tests that include the keyword 'function'
cargo test function

# We can also run all tests in a module by filtering on the module's name.
cargo test mod_name
```
## Ignoring some tests unless specifically requested
You can annotate the time-consuming tests using the `ignore` attribute to exclude them
```rust
#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	#[ignore]
	fn it_works() { // this test will be ignored.
		// ...
	}
}
```

If you want to run only the ignored tests:
```bash
cargo test -- --ignored

# If you want to include all tests ignored or not
cargo test -- --include-ignored
```
# Test Organization
The Rust community thinks about tests in terms of two main categories: unit tests and integrations tests. Unit tests test one module in isolation and can test private interfaces. Integration tests are entirely external to your library using only the public interface and potentially exercising multiple modules per test.
## Unit tests
You'll put unit tests in the `src` directory in each file with the code that they're testing. The convention is to create a module named `tests` in each file to contain the test functions and to annotate the module with `cfg(test)`.
### The tests module and `#[cfg(test)]`
The `#[cfg(test)]` annotation on the `tests` module tells Rust to compile and run the test code only when you run `cargo test`.

Because integration tests go in a different directory, they don't need the `#[cfg(test)]` annotation.  However, because unit tests go in the same files as the code, you'll use `#[cfg(test)]` to specify that they shouldn't be included in the compiled result.

On the automatically generated `tests` module, the attribute `cfg` stands for _configuration_ and tells Rust that the following item should only be included given a certain configuration option. In this case, the configuration option is `test`, which is provided by Rust for compiling and running tests.

By using the `cfg` attribute, Cargo compiles our test code only if we actively run the tests with `cargo test`. This includes any helper functions that might be within this module, in addition to the functions annotated with `#[test]`.
### Testing Private Functions
Rust privacy rules do allow you to test private functions.
```rust
pub fn add_two(a: usize) -> usize {
	internal_adder(a, 2)
}

fn internal_adder(left: usize, right: usize) -> usize {
	left + right
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn internal() {
		let result = internal_adder(2, 2);
		assert_eq!(result, 4);
	}
}
```
## Integration Tests
To create integration tests, you first need a *tests* directory.

This creation *test* is created at the top level of your project directory, next to `src`. Cargo knows to look for integration test files in this directory. Cargo will compile each of the files as an individual crate.
```plaintext
adder 
├── Cargo.lock 
├── Cargo.toml 
├── src 
│   └── lib.rs 
└── tests 
	└── integration_test.rs
```

Contents of `tests/integration_test.rs`
```rust
use adder::add_two;

#[test]
fn it_add_two() {
	let result = add_two(2);
	assert_eq!(result, 4);
}
```

Each file in the *tests* directory is a separate crate, so we need to bring our library into each test crate's scope.

We don't need to annotate any code in `test/integration_test.rs` with `#[cfg(test)]`. Cargo treats the *tests* directory specially and compiles files in this directory only when we run `cargo test`.

Note that if any test in a section fails, the following sections will not be run. For example, if a unit test fails, there won't be any output for integration and doc tests because those tests will only be run if all unit tests are passing.

We can run a particular integration test function by specifying the test function's name as argument to `cargo test`. To run all the tests in a particular integration test file, use the `--test` argument of `cargo test` followed by the name of the line:
```bash
cargo test --test integration_test
```
## Submodule in integration tests
As you add more integration tests, you might want to make more files in the tests directory to help organize them. As mentioned earlier, each file in the tests directory is compiled as its own separate crate, which is useful for creating separate scopes to more closely imitate the way end users will be using your crate. 

However this means files in the tests directory don't share the same behavior as files in `src` do.

The different behavior of *tests* directory files is most noticeable when you have a set of helper functions to use in multiple integration test files and you try to extract them into a common module. For example, if we create `test/common.rs` and place a function named `setup` in it, we can add some code to `setup` that we want to call from multiple test functions in multiple test files:
```rust
pub fn setup() {
	// setup code specific to your library's tests would go here
}
```

To avoid having `common` appear in the test output, instead of creating `test/common.rs`, we'll create `test/common/mod.rs`. The project directory now looks like this:
```plaintext
├── Cargo.lock 
├── Cargo.toml 
├── src 
│   └── lib.rs 
└── tests 
	├── common 
	│   └── mod.rs 
	└── integration_test.rs
```

Naming the file this way tells Rust not to treat the `common` module as an integration test file. Files in subdirectories of the test directory don't get compiled as separate crates or have sections in the test output.

After we've created `test/common/mod.rs`, we can use it from any of the integration test files as a module. Here's an example of calling the `setup` function from the `it_adds_two` test in `tests/integration_test.rs`
```rust
use adder::add_two;

mod common;

#[test]
fn it_adds_two() {
	common::setup();

	let result = add_two(2);
	assert_eq!(result, 4);
}
```
## Integration tests for binary crates
If our project is a binary crate that only contains a `main.rs` file and doesn't have a `lib.rs` file, we can't create integration tests in the tests directory and bring functions defined in the `main.rs` file into scope with a `use` statement.

Only library crates expose functions that other crates can use, binary crates are meant to be run on their own.

This is one of the reasons Rust projects that provide a binary have a straightforward `src/main.rs` file that calls logic that lives in the `src/lib.rs` file. Using that structure, integration tests _can_ test the library crate with `use` to make the important functionality available. If the important functionality works, the small amount of code in the `src/main.rs` file will work as well, and that small amount of code doesn’t need to be tested.