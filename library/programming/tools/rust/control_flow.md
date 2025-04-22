## If expressions
The condition in **if expressions** must be a `bool`.
```rust
fn main() {
	let number = 3;

	if number < 5 {
		println!("number is less than 5");
	} else if number == 6{
		println!("number is 6");
	} else {
		println!("number is bigger than 6");
	}
}
```
## Using if in a let statement
Because `if` is an expression, we can use it on the right side of a `let` statement to assign the outcome to a variable.

If the types are mismatched, as in the following example, we’ll get an error.
```rust
fn main() {
	let condition = true;
	let number = if condition { 5 } else { 6 };
	let number = if condition { 5 } else { "six" }; // Compile Error.

	println!("The value of number is: {number}");
}
```
## Loops
- `break`: Stops executing the loop. Can be used to return the value out of the loop.
- `continue`: Continues to the next iteration of the loop.
```rust
fn main() {
	// infinite loop
	loop {
		println!("again!");
	}

	let mut counter = 0;

	// Introducing break
	let result = loop {
		counter += 1;

		if counter == 10 {
			break counter * 2;
		}
	}

	println!("The result is {result}");

	// Introducting while loops
	let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");

	// For loops, used for collections
	let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```
### Loop labels
You can optionally specify a _loop label_ on a loop that you can then use with `break` or `continue` to specify that those keywords apply to the labeled loop instead of the innermost loop. Loop labels must begin with a single quote.
```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```