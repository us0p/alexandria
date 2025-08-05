## Variables and mutability
Variables are immutable by default but you still have the option to make your variables mutable.

Variables are defined using the `let` keyword. To make a variable mutable we add the `mut` keyword after `let`.
```Rust
fn main() {
	let x = 6; // Immutable
	let mut y = 7; // Mutable

	// x = 7 -> Cannot assign twice to immutable variable.
	y = 6 // Works as expected.
}
```
## Constants
Variables bound to a *name* and are **not allowed** to change.

You can't use `mut` with constants.

You declare constants using the `const` keyword instead of the `let` keyword, and **the type of the value must be annotated**.

Constants can be declared in any scope.

Constants may be set only to a constant expression, not the result of a value that could only be computed at runtime.
```Rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

Rust’s naming convention for constants is to use all uppercase with underscores between words.
## Shadowing
You can declare a new variable with the same name as a previous variable.

We say that the first variable is shadowed by the second, which means that the second variable is what the compiler will see when you use the name of the variable.

We can shadow a variable by using the same variable’s name and repeating the use of the `let` keyword as follows:
```Rust
fn main() {
	let x = 5;

	let x = x + 1;

	{
		let x = x + 2;
		println!("The value of x in the inner scope is: {x}"); // 8
	}
	
	println!("The value of x is: {x}"); // 6
}
```

Shadowing is different from marking a variable as `mut` because we’ll get a compile-time error if we accidentally try to reassign to this variable without using the `let` keyword. By using `let`, we can perform a few transformations on a value but have the variable be immutable after those transformations have been completed.

The other difference between `mut` and shadowing is that because we’re effectively creating a new variable when we use the `let` keyword again, we can change the type of the value but reuse the same name.
```rust
let spaces = "  "; // string type
let spaces = spaces.len(); // number type
```

If we try to change the type of a `mut` variable we get a compile error.