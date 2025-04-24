# Functions
Functions are created with the `fn` keyword.

The `main` function is the entry point of many programs.

Rust code uses _snake case_ as the conventional style for function and variable names.
```rust
fn main() {
	println!("Hello, workd!");

	another_function();
}

fn another_function() {
	println!("Another function.");
}
```

Note that we defined `another_function` _after_ the `main` function in the source code; we could have defined it before as well. Rust doesn’t care where you define your functions, only that they’re defined somewhere in a scope that can be seen by the caller.
## Parameter
```rust
fn main() {
	another_function(5);
}

fn another_function(x: i32) {
	println!("The value of x is: {x}");
}
```

In function signatures, you _must_ declare the type of each parameter.

When defining multiple parameters, separate the parameter declarations with commas, like this:
```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```
## Statements and Expressions
- **Statements**: Instructions that perform some action and to not return a value.
- **Expressions**: Evaluate to a resultant value.

In some languages, you can write `x = y = 6` and have both `x` and `y` have the value `6`; that is not the case in Rust.
```rust
fn main() {
    let y = {
        let x = 3; // 3 here is an expression
        x + 1 // (x + 1) is an expression that results to 4
    }; // This scope block is an expression

    println!("The value of y is: {y}"); // this macro call is an expression
}
```

>Note that the `x + 1` line doesn’t have a semicolon at the end, which is unlike most of the lines you’ve seen so far. Expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement, and it will then not return a value. Keep this in mind as you explore function return values and expressions next.
## Function with Return Values
We don’t name return values, but we must declare their type after an arrow (`->`). In Rust, the return value of the function is synonymous with the value of the final expression in the block of the body of a function. You can return early from a function by using the `return` keyword and specifying a value, but most functions return the last expression implicitly.
```rust
fn five() -> i32 {
    5 // Return expression, matches the return type annotation.
}

fn plus_one(x: i32) -> i32 {
    x + 1; // Doesn't return any expression, note the semicolon
}

fn main() {
    let x = five();

	let y = plus_one(5); // Compile error!

    println!("The value of x is: {x}");
}
```

It's also possible to return multiple values from a function in Rust:
```rust
fn multiple_return_fn(n1: u32, n2: u32) -> (u32, u32) {
	if n2 == 0 {
		return (n1 * n2, 0);
	};
	
	(n1 * n2, n1 / n2)
}
```