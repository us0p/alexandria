Rust groups errors into two major categories:
- **Recoverable**: Errors such as *file not found*, most likely just want to report the problem to the user.
- **Unrecoverable**: Errors that are always symptoms of bugs, such as trying to access a location beyond the end of an array, and so we want immediately stop the program.
## Unrecoverable Errors with `panic!`
There are two ways to cause a panic:
- Taking an action that causes the code to panic.
- Explicitly calling the `panic!` macro.

By default, these panics will print a failure message, unwind, clean up the stack, and quit.

**Unwinding** means Rust walks back up the stack and cleans up the data from each function it encounters. However, walking back and cleaning up is a lot of work. Rust therefore, allows you to choose the alternative of immediately aborting, which ends the program without cleaning up.

Memory that the program was using will then need to be cleaned up by the operating system.

You can switch from unwinding to aborting upon a panic by adding `panic = 'abort'` to the appropriate `[profile]` sections in your `Cargo.toml`.
```cargo.toml
[profile.release]
panic = 'abort'
```

```rust
fn main() {
	panic!("crash and burn");
}
```
We can set the `RUST_BACKTRACE` environment variable to get a backtrace of exactly what happened to cause the error
## Recoverable Errors with Results
```rust
enum Result<T, E> {
	Ok(T),
	Err(E),
}
```

`T` represents the type of the value that will be returned in a success case within the `Ok` variant.
`E` represents the type of the error that will be returned in a failure case within the `Err` variant.
```rust
use std::fs::File;

fn main() {
	let greeting_file_result = File::open("hello.txt"); 
	// Returns Result<stdd:fs::File, std::io::Error>

	let greeting_file = match greeting_file_result {
		Ok(file) => file,
		Err(error) => panic!("Problem opening the file: {error:?}"),
	}
}
```

The `Resul` enum was brought into scope by the prelude.
## Matching on Different Errors
```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
	let greeting_file_results = File::open("hello.txt");

	let greeting_file = match greeting_file_result {
		Ok(file) => file,
		Error(error) => match error.kind() {
			ErrorKind::NotFound => match File::create("hello.txt") {
				Ok(fc) => fc,
				Err(e) => panic!("Problem creating the file: {e:?}"),
			},
			other_error => {
				panic!("Problem opening the file: {other_error:?}");
			}
		},
	};
}
```
## Shortcuts for Panic or Error: `unwrap` and `expect`
The `unwrap` method is a shortcut method implemented just like the `match` expression. If the `Result` value is the `Ok` variant, `unwrap` will return the value inside the `Ok`. If the `Result` is the `Err` variant, it'll call the `panic!` macro.
```rust
use std::fs::File;

fn main() {
	let greeting_file = File::open("hello.txt").unwrap();
}
```

`expect` method lets us also choose the `panic!` error message.
```rust
use std::fs::File;

fn main() {
	let greeting_file = File::open("hello.txt")
	    .expect("hello.txt should be included in this project");
}
```
## Propagating Errors
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
	let username_file_result = File::open("hello.txt");

	let mut username_file = match username_file_result {
		Ok(file) => file,
		Err(e) => return Err(e),
	};

	let mut username = String::new();

	match username_file.read_to_string(&mut username) {
		Ok(_) => Ok(username),
		Err(e) => Err(e),
	}
}
```

This pattern of propagating errors is so common in Rust that it provides the `?` operator to make this easier.

The code bellow has the same behavior as the above, but it's implemented with the `?` operator:
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
	let mut username_file = File::open("hello.txt")?;
	let mut username = String::new();
	username_file.read_to_string(&mut username)?;
	Ok(username)
}
```

The `?` placed after a `Result` value is defined to work in almost the same way as the `match` expressions we defined to handle the `Result` values in the previous example. If the value of the `Result` is an `Ok`, the value inside the `Ok` will get returned from this expression, and the program will continue. If the value is an `Err`, the `Err` will be returned from the whole function as if we had used the `return` keyword so the error value gets propagated to the calling code.

Error values that have the `?` operator go through the `from` function, defined in the `From` trait in the standard library, which is used to convert values from one type into another. When this happens, the error type received is converted into the error type define din the return type of the current function. This is useful when a function returns one error type to represent all the ways a function might fail, even if parts might fail for many different reasons.
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
	let mut username = String::new();

	// making the example function even shorter with method chaining and ?.
	File::open("hello.txt")?.read_to_string(&mut username)?;

	Ok(username)
}

// The method fs::read_to_string() creates a new String, reads the contents of the file into that String and returns it.
fn read_username_from_file_shorter() -> Result<String, io::Error> {
	fs::read_to_string("hello.txt");
}
```

The `?` operator can only be used in functions whose return type is compatible with the value the `?` is used on.

We are only allowed to use the `?` operator in a function that returns `Result`, `Option`, or another type that implements `FromResidual`.

When called on an `Option<T>` if the value is `None`, the `None` will be returned early from the function at that point. If the value is `Some`, the value inside the `Some` is the resultant value of the expression.
```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
	text
	.lines() // returns an iterator over the lines in the string.
	.next()? // get the first value from the iterator, returns a Option<&str> or exit early if None.
	.chars() // returns an iterator of the characters.
	.last() // return the last item in the iterator returns an Option<char>
}
```

Note that you can use the `?` operator on a `Result` in a function that returns `Result`, and you can use the `?` operator on an `Option` in a function that returns `Option`, but you can’t mix and match. The `?` operator won’t automatically convert a `Result` to an `Option` or vice versa; in those cases, you can use methods like the `ok` method on `Result` or the `ok_or` method on `Option` to do the conversion explicitly.

The function `main()` can also return a `Result<(), E>`.
```rust
use std::error::Error;
use std::fs::File;

// Box<dyn Error> is a trait object. Represents any kind of error.
fn main() -> Result<(), Box<dyn Error>> {
	let greeting_file = File::open("hello.txt")?;

	Ok(())
}
```

When a `main` function returns a `Result<(), E>`, the executable will exit with a value of `0` if `main` returns `Ok(())` and will exit with a nonzero value if `main` returns an `Err` value. Executables written in C return integers when they exit: programs that exit successfully return the integer `0`, and programs that error return some integer other than `0`. Rust also returns integers from executables to be compatible with this convention.

The `main` function may return any types that implement the `std::process::Termination` trait, which contains a function `report` that returns an `ExitCode`.