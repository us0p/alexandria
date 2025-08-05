## Defining an Enum
Enums give you a way of saying a value is one of a possible set of values.
```rust
enum IpAddrKind {
	V4,
	V6,
}

fn main() {
	let four = IpAddrKind::V4;
	let six = IpAddrKind::V6;
}
```

We can put data directly into each enum variant.
```rust
// Both V4 and V6 will have associated String values
enum IpAddr {
	V4(String),
	V6(String),
}

// Data is attached to each variant of the enum directly.
let home = IpAddre::V4(String::from("127.0.0.1"));
let loopback = IpAddr::V6(String::from("::1"));
```

From the above example you can see that the name of each enum variant that we define also becomes a function that constructs an instance of the enum.

`IpAddr::V4()` is a function call that takes a `String` argument and returns an instance of the `IpAddr` type.

Also, each variant can have different types and amounts of associated data.
```rust
enum IpAddr {
	V4(u8, u8, u8, u8),
	V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```
## Methods
```rust
enum Message {
	Quit,                       // No data associated
	Move {x: i32, y: i32},      // named fields like a struct does
	Write(String),              // includes a single String
	ChangeColor(i32, i32, i32), // includes three i32 values like a tuple does
}

impl Message {
	fn call(&self) {
		// definition
	}
}

let m = Message::Write(String::from("hello"));
m.call();
```
## The Option enum and its advantages over Null Values
The `Option` type encodes the very common scenario in which a value could be something or it could be nothing.

Rust doesn't have the null feature that many other languages have. Null is a value that means there is no value there.

The problem with null values is that if you try to use a null value as a not-null value, you’ll get an error of some kind. Because this null or not-null property is pervasive, it’s extremely easy to make this kind of error.

However, the concept that null is trying to express is still a useful one: a null is a value that is currently invalid or absent for some reason.

The problem isn’t really with the concept but with the particular implementation. As such, Rust does not have nulls, but it does have an enum that can encode the concept of a value being present or absent. This enum is `Option<T>`, and it is defined by the standard library:
```rust
enum Option<T> {
	None,
	Some(T), 
}
```

This enum is so useful that it's even included in the prelude. Its variants are also included in the prelude, you can use `Some` and `None` directly without the `Option::` prefix.
```rust
// Rust can infer the type of the variable by using the value provided to 'Some'.
let some_number = Some(5); // is type Option<i32>
let some_char  = Some('e'); // is type Option<char>

// It can't infer the value of None, thus we need to explicity define the type.
let absent_number: Option<i32> = None;
```

Why is having `Option<T>` any better than having null? 

In short, because `Option<T>` and `T` (where `T` can be any type) are different types, the compiler won’t let us use an `Option<T>` value as if it were definitely a valid value.
```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

// Error: cannot add `Option<i8>` to `i8`
let sum = x + y;
```
# Option Combinators
## `Option::map()`
Lets you transform the `Some` value inside an Option using a function.

It's useful because it lets you work directly with the value inside an Option without unwrapping or doing explicit matching.

- If the Option is `Some(x)`, it applies the function to `x` and returns `Some(new_value)`.
- If the Option is None, it just returns None.
```Rust
let number = Some(4);

let squared = number.map(|x| x * x); // Some(16)

let nothing: Option<i32> = None;

let squared = nothing.map(|x| x * x); // None
```
## `Option::and_then()`
Using `Option::map()` in a function that returns an `Option<T>` results in the nested `Option<Option<T>>`.

`Option::and_then()` calls its function input with the wrapped value and returns the result. If the `Option` is None, then it returns None instead.
```Rust
enum Food { CordonBleu, Steak, Sushi }
enum Day { Monday, Tuesday, Wednesday }

// We don't have the ingredients to make Sushi.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// We have the recipe for everything except Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// To make a dish, we need both the recipe and the ingredients.
// We can represent the logic with a chain of `match`es:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// This can conveniently be rewritten more compactly with `and_then()`:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}
```
## Unpacking Options and defaults
There is more than one way to unpack an `Option` and fall back on a default if it's None. You should consider:
- Do we need eager or lazy evaluation?
- Do we need to keep the original empty value intact, or modify it in place?
### `Option::or()`
Is chainable and eagerly evaluates its argument.

Note that because `Option::or()`'s arguments are evaluated eagerly, the variable passed to `or` is moved.
```Rust
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let orange = Some(Fruit::Orange);
    let no_fruit: Option<Fruit> = None;

    // first_available_fruit: Some(Orange)
    let first_available_fruit = no_fruit
	    .or(orange)
	    .or(apple);
    println!("first_available_fruit: {:?}", first_available_fruit);

    // `or` moves its argument.
    // In the example above, `or(orange)` returned a `Some`, so `or(apple)` was not invoked.
    // But the variable named `apple` has been moved regardless, and cannot be used anymore.
 }
```
### `Option::or_else()`
Is also chainable but evaluates lazily.
```Rust
let get_kiwi_as_fallback = || {
	println!("Providing kiwi as fallback");
	Some(Fruit::Kiwi)
};
let get_lemon_as_fallback = || {
	println!("Providing lemon as fallback");
	Some(Fruit::Lemon)
};

// first_available_fruit: Some(Kiwi)
let first_available_fruit = no_fruit
	.or_else(get_kiwi_as_fallback)
	.or_else(get_lemon_as_fallback);
	
println!("first_available_fruit: {:?}", first_available_fruit);
```
### `Option::get_or_insert()`
Makes sure an Option has a value by modifying in place with a fallback value.

Note that it eagerly evaluates its parameter, so variables are moved.
```Rust
let mut my_fruit: Option<Fruit> = None;
let apple = Fruit::Apple;
let first_available_fruit = my_fruit.get_or_insert(apple);
println!("first_available_fruit is: {:?}", first_available_fruit);
println!("my_fruit is: {:?}", my_fruit);
// first_available_fruit is: Apple
// my_fruit is: Some(Apple)
//println!("Variable named `apple` is moved: {:?}", apple); -> ERROR
```
### `Option::get_or_insert_with()`
Same as `Option::get_or_insert()` but evaluates lazily.

It the Option has a value, the closure is not invoked and the value is left unchanged.
```Rust
let mut my_fruit: Option<Fruit> = None;
let get_lemon_as_fallback = || {
    println!("Providing lemon as fallback");
    Fruit::Lemon
};
let first_available_fruit = my_fruit
    .get_or_insert_with(get_lemon_as_fallback);
println!("first_available_fruit is: {:?}", first_available_fruit);
println!("my_fruit is: {:?}", my_fruit);
// Providing lemon as fallback
// first_available_fruit is: Lemon
// my_fruit is: Some(Lemon)
```