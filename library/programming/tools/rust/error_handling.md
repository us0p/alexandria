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

The `Result` enum was brought into scope by the prelude.
## Using Result in `main`
Typically we don't need to explicitly provide the return type for the `main` function.

However, `main` is also able to have a return type of `Result`.

If an error occurs within the `main` function, it will return an error code and print a debug representation of the error (using the **Debug trait**).
```Rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
	let number_str = "10";
	let number = match number_str.parse::<i32>()?;
	println!("{number}");
	Ok(())
}
```

When a `main` function returns a `Result<(), E>`, the executable will exit with a value of `0` if `main` returns `Ok(())` and will exit with a nonzero value if `main` returns an `Err` value. Rust keeps this pattern to be compatible with the C convention.

The `main` function may return any types that implement the `std::process::Termination` trait, which contains a function `report` that returns an `ExitCode`.
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

Error values that have the `?` operator go through the `from` function, defined in the `From` trait in the standard library, which is used to convert values from one type into another. When this happens, the error type received is converted into the error type defined in the return type of the current function. This is useful when a function returns one error type to represent all the ways a function might fail, even if parts might fail for many different reasons.
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
## Combinators for Result
[Option's map, and_then](enum_and_pattern_matching.md#Option%20Combinators), and many other combinators are also implemented for Result.
```Rust
use std::num::ParseIntError;

// As with `Option`, we can use combinators such as `map()`.
fn multiply(
	first_number_str: &str, 
	second_number_str: &str
) -> Result<i32, ParseIntError> {
    first_number_str
	    .parse::<i32>()
	    .and_then(|first_number| {
	        second_number_str.parse::<i32>()
		        .map(|second_number| {
			        first_number * second_number
				})
	    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let twenty = multiply("10", "2");
    print(twenty);

    let tt = multiply("t", "2");
    print(tt);
}
```
## Pulling Results out of Options
There will be cases where you can have Options and Results that must be mixed. In that case we want our code to handle such types as a single composable type.

The most basic way of handling mixed error types if to just embed them into each other.
```Rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
	vec.first().map(|first| {
		first.parse::<i32>().map(|n| 2 * n)
	})
}
```

For times when we want to stop processing on errors but keep going when the Option is None. We can swap the Result and Option with `Option::transpose()`.
```Rust
use std::num::ParseIntError;

fn double_first(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
	let opt = vec.first().map(|first| {
		first.parse::<i32>().map(|n| 2 * n)
	})

	opt.transpose()
}
```

We can also use `ok_or` (eager) and `ok_or_else` (lazy) to convert Options to Results.

Those methods wrap the provided value in an `Err(...)` value.
```Rust
use std::error;

fn it_is_not_an_option(val: &Option<String>) -> Result<String, &str> {
	// Eager, value moved
	val.ok_or("Emptiness is not an option") 
	
	// val.ok_or_else(|| "Emptiness is not an option") - Lazy
}
```
## Defining an error type
Rust allow us to define our own error types.

Typically, you define your custom error type as an `enum`, especially when there are multiple kinds of errors your code might produce.

But you can also use another types like `struct`.

You also need to implement the `std::fmt::Display` trait which is required for implementing the `std::error::Error` trait which lets your custom error integrate with the broader Rust error ecosystem.

If you want to use the `?` operator in your error, you also need to implement the `From` trait.
```Rust
use std::{fs, io, num::ParseIntError, fmt, error::Error};

#[derive(Debug)]
enum MyError {
    Io(io::Error),
    Parse(ParseIntError),
    Custom(String),
}

impl fmt::Display for MyError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MyError::Io(e) => write!(f, "IO error: {}", e),
            MyError::Parse(e) => write!(f, "Parse error: {}", e),
            MyError::Custom(msg) => write!(f, "Custom error: {}", msg),
        }
    }
}

impl Error for MyError {
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        match self {
            MyError::Io(e) => Some(e),
            MyError::Parse(e) => Some(e),
            MyError::Custom(_) => None,
        }
    }
}

impl From<io::Error> for MyError {
    fn from(err: io::Error) -> MyError {
        MyError::Io(err)
    }
}

impl From<ParseIntError> for MyError {
    fn from(err: ParseIntError) -> MyError {
        MyError::Parse(err)
    }
}

fn read_and_parse_file(path: &str) -> Result<i32, MyError> {
    let content = fs::read_to_string(path)?;
    let number: i32 = content.trim().parse()?;
    Ok(number)
}
```
## Boxing Errors
The standard library allows us to box our errors with `Box` which implement conversion from any type that implements the `Error` trait into the trait object `Box<Error>`, via `From`.

The drawback is that the underlying error type is only known at runtime and not statically determined.
```Rust
use std::error;
use std::fmt;

// Change the alias to use Box<dyn error::Error>
type Result<T> = std::result::Result<T, dyn error::Error>>;

#[derive(Debug, Clone)]
struct EmptyVec;

impl fmt::Display for EmptyVec {
	// ...
}

impl error::Error for EmptyVec {}

fn double_first(vec: Vec<&str>) -> Result<i32> {
	vec.first()
		.ok_or_else(|| EmptyVec.into()) // Converts to Box
		.and_then(|s| {
			s.parse::<i32>()
				.map_err(|e| e.into()) // Converts to Box
				.map(|i| 2 * i)
		})
}
```
## Wrapping errors
An alternative to boxing errors is to wrap them in your own error type.
```Rust
use std::error;
use std::error::Error;
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    // We will defer to the parse error implementation for their error.
    // Supplying extra info requires adding more data to the type.
    Parse(ParseIntError),
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "please use a vector with at least one element"),
            // The wrapped error contains additional information and is available
            // via the source() method.
            DoubleError::Parse(..) =>
                write!(f, "the provided string could not be parsed as int"),
        }
    }
}

impl error::Error for DoubleError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            DoubleError::EmptyVec => None,
            // The cause is the underlying implementation error type. Is implicitly
            // cast to the trait object `&error::Error`. This works because the
            // underlying type already implements the `Error` trait.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

// Implement the conversion from `ParseIntError` to `DoubleError`.
// This will be automatically called by `?` if a `ParseIntError`
// needs to be converted into a `DoubleError`.
impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = vec.first().ok_or(DoubleError::EmptyVec)?;
    // Here we implicitly use the `ParseIntError` implementation of `From` (which
    // we defined above) in order to create a `DoubleError`.
    let parsed = first.parse::<i32>()?;

    Ok(2 * parsed)
}
```
## Iterating over Results
While we map over the elements of an iterator, we can have some of those operations failing and producing errors.
```Rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<i32>()) // this might fail
        .collect(); // this fails the entire operation
    println!("Results: {:?}", numbers);
}
```

There are a couple of ways we can handle this:
### Ignore failed items with `filter_map()`
```Rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
        .into_iter()
        .filter_map(|s| s.parse::<i32>().ok()) // returns only successfull operations
        .collect();
    println!("Results: {:?}", numbers);
}
```
### Collect failed items with `map_err()` and `filter_map()`
```Rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
	let mut errors = vec![];
    let numbers: Vec<_> = strings
        .into_iter()
        .map(|s| s.parse::<i32>()) // produce a vec of mixed numbers and errors
		.filter_map(
			|r| r.map_err( // if the value is an error
				|e| errors.push(e) // add it to the errors vec
			).ok() // returns only values that aren't errors.
		)
        .collect();
    println!("Results: {:?}", numbers);
}
```
### Collect all valid values and partitions with `partition()`
Every record is wrapped in a Result
```Rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
	
	// produces two vectors
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
        .into_iter()
        .map(|s| s.parse::<i32>())
        .partition(Result::is_ok);

	// from the numbers, get all Ok values.
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
	
	// from the errors, get all Err values.
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
	
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```