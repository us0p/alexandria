## String Slices
Is a [reference](references_and_borrowing.md) to part of a `String`, string literal or an Array.
```rust
let s = String::from("hello world");

let hello = &s[0..5];  // equal to [..5]
let world = &s[6..11]; // equal to [6..]
let complete_s = &s[..];
```

We create slices using a **range** (`Syntax: ..`) within brackets by specifying `[starting_index..ending_index]`, where `starting_index` is inclusive and `ending_index` is exclusive.

The slice data structure stores the starting position and the length of the slice, which corresponds to `ending_index` minus `starting_index`.

>String slice range indices must occur at valid `UTF-8` character boundaries. If you attempt to create a string slice in the middle of a multi-byte character, your program will exit with an error.

The following code represents how to represent slices as a return value of a function.
```rust
// By making our parameter as '&str' we allow this function to be used with any string.
fn first_word(s: &str) -> &str {
	let bytes = s.as_bytes();

	for (i, &item) in bytes.iter().enumerate() {
		if item == b' ' {
			return &s[..i];
		}
	}

	return &s[..];
}

// &[type] is the annotation for slices that references an array.
fn print_numbers(s: &[u32]) {
	for (i, &item) in s.iter().enumerate() {
		println!(item);
	}
}
```
## String literals as slices
Remember that string literals are stored inside the binary.
```rust
let s = "Hello, world!";
```

The type of `s` here is `&str`: it’s a slice pointing to that specific point of the binary. This is also why string literals are immutable; `&str` is an immutable reference.
```rust
fn main() {
	let my_string = String::from("hello world");
	
	// references to 'String' are equivalent to whole slices of that String.
	let word = first_word(&my_string);
	
	let my_string_literal = "hello world";
	
	// Because stringn literals are string slices already, this works without the slice syntax
	let word = first_word(my_string_literal);
}
```