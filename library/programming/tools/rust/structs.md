# Structs
```rust
struct User {
	active: bool,
	username: String,
	email: String,
	sing_in_count: u64,
}

fn main() {
	let mut user = User{
		active: true,
		username: String::from("us0p"),
		email: String::from("us0p@mail.com"),
		sign_in_count: 1,
	};

	println!("{}", user.username);

	user.email = String::from("us0p_newmail@mail.com");
}
```
## Field Init Shorthand
Creating and returning a struct from a function
```rust
fn build_user(email: String, username: String) -> User {
	User {
		active: true,
		username,
		email,
		sign_in_count: 1,
	}
}
```
## Creating instances from other instances with struct update syntax
```rust
fn main() {
	//...
	let user2 = User {
		active: user.active,
		username: user.username,
		email: String::from("another@mail.com"),
		sign_in_count: user.sign_in_count,
	}

	// update syntax, similar to JS destructuring
	let user3 = User {
		email: String::from("yet_another@mail.com"),
		..user2,
	}
}
```

Note that the `..user2` **must come last** to specify that any remaining fields should get their values from the corresponding fields in `user2`.

In this example, we can no longer use `user2` as a whole after creating `user3` because the `String` in the `username` field of `user2` was moved into `user3`.

If we had given `user3` new `String` values for both `email` and `username`, and thus only used the `active` and `sign_in_count` values from `user2`, then `user2` would still be valid after creating `user3`. Both `active` and `sign_in_count` are types that implement the `Copy`.

We can still use `user2.email` in this example, since its value was _not_ moved out.
## Creating different types of tuple with structs
Tuple structs are useful when you want to give the whole tuple a name and make the tuple a different type from other tuples, and when naming each field as in a regular struct would be verbose or redundant.
```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Note that the `black` and `origin` values are different types because they’re instances of different tuple structs. Each struct you define is its own type, even though the fields within the struct might have the same types.

You can use a `.` followed by the index to access an individual value.

Unlike tuples, tuple structs require you to name the type of the struct when you destructure them. For example, we would write `let Point(x, y, z) = point`.
## Unit like structs
Unit like structs are structs that don't have any field. These are called _unit-like structs_ because they behave similarly to `()`.

Unit-like structs can be useful when you need to implement a trait on some type but don’t have any data that you want to store in the type itself.
```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```