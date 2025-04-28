Allows you to compare a value against a series of patterns and then execute code based on which pattern matches. Patterns can be made up of literal values, variable names, wildcards, and many other things; The compiler confirms that all possible cases are handled, in another words, the arms' patterns must cover all possibilities for the code to compile.
```rust
enum Coin {
	Penny,
	Nickel,
	Dime,
	Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
	match coin {
		Coin::Penny => {
			println!("Lucky penny!");
			1
		}
		Coin::Nickel => 5,
		Coin::Dime => 10,
		Coin::Quarter => 25,
	}
}
```

When the `match` expression executes, it compares the resultant value against the pattern of each arm, in order. If a pattern matches the value, the code associated with that pattern is executed. If that pattern doesn’t match the value, execution continues to the next arm.

The code associated with each arm is an expression, and the resultant value of the expression in the matching arm is the value that gets returned for the entire `match` expression.

If you want to run multiple lines of code in a match arm, you must use curly brackets, and the comma following the arm is then optional.
## Patterns that bind to values
match arms can bind to the parts of the values that match the pattern. This is how we can extract values out of enum variants.

As an example, let’s change one of our enum variants to hold data inside it. From 1999 through 2008, the United States minted quarters with different designs for each of the 50 states on one side. No other coins got state designs, so only quarters have this extra value.
```rust
enum UsState {
	Alabama,
	Alaska,
	// --snip--
}

enum Coin {
	Penny,
	Nickel,
	Dime,
	Quarter(UsState),
}

fn value_in_cents(coin: Coin) -> u8 {
	match coin {
		Coin::Penny => 1,
		Coin::Nickel => 5,
		Coin::Dime => 10,
		Coin::Quarter(state) => {
			println!("State quarter from {state}!");
			25
		}
	}
}
```
## Catch-all patterns and the _ placeholder
Using enums, we can also take special actions for a few particular values, but for all other values take one default action.
```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

This code compiles, even though we haven’t listed all the possible values a `u8` can have, because the last pattern will match all values not specifically listed. This catch-all pattern meets the requirement that `match` must be exhaustive. Note that we have to put the catch-all arm last because the patterns are evaluated in order. If we put the catch-all arm earlier, the other arms would never run, so Rust will warn us if we add arms after a catch-all!

Rust also has a pattern we can use when we want a catch-all but don’t want to _use_ the value in the catch-all pattern: `_` is a special pattern that matches any value and does not bind to that value. This tells Rust we aren’t going to use the value, so Rust won’t warn us about an unused variable.
```rust
// Updating function to include a catch-all pattern that doesn't bind the value
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

// Using unit value to represent the absense of action in any other patter.
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}
```
## Concise control flow with `if let` and `let else`
The `if let` syntax lets you combine `if` and `let` into a less verbose way to handle values that match one pattern while ignoring the rest.
```rust
let config_max = Some(3u8);
maatch config_max {
	Some(max) => println!("The maximum is configured to be {max}"),
	_ => (),
}

// Can be shortened to:
if let Some(max) = config_max {
	println!("The maximum is configured to be {max}");
}
```

We can then use `max` in the body of the `if let` block in the same way we used `max` in the corresponding `match` arm. The code in the `if let` block only runs if the value matches the pattern.
## `let-else` syntax
Takes a pattern on the left side and an expression on the right, very similar to `if let`, but it doesn't have an `if` branch, only an `else` branch. If the pattern matches, it will bind the value from the pattern in the outer scope. If the pattern doesn't match, the program will flow into the `else` arm, which must return from the function.
```rust
fn describe_state_quarter(coin: Coin) -> Option<String> {
	let Coin::Quarter(state) = coin else {
		return None;
	}

	if state.existed_in(1900) {
		Some(format!("{state:?} is pretty old, for America!"))
	} else {
		Some(format!("{state:?} is relatively new."))
	}
}
```