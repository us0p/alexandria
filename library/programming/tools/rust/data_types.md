## Data Types
Rust is a _statically typed_ language. The compiler can usually infer what type we want to use based on the value and how we use it. In cases when many types are possible, we must add a type annotation, like this:
```rust
// You'll get a compile error if you remove the type annotation
let guess: u32 = "42".parse().expect("Not a number!") 
```
## Scalar Types
A _scalar_ type represents a single value. Rust has four primary scalar types: integers, floating-point numbers, Booleans, and characters.
### Integer
Can be one of:
- `u`: Unsigned
- `i`: Signed

| Length  | Signed  | Unsigned |
| ------- | ------- | -------- |
| 8-bit   | `i8`    | `u8`     |
| 16-bit  | `i16`   | `u16`    |
| 32-bit  | `i32`   | `u32`    |
| 64-bit  | `i64`   | `u64`    |
| 128-bit | `i128`  | `u128`   |
| arch    | `isize` | `usize`  |
Each signed variant can store numbers from $-(2^{n - 1})$ to $2^{n - 1} - 1$ **inclusive**, where **n** is the number of bits that variant uses.

Unsigned variants can store numbers from $0$ to $2^{n - 1}$.

Additionally, the `isize` and `usize` types depend on the architecture of the computer your program is running on, which is denoted in the table as `“arch”`: `64 bits` if you’re on a `64-bit` architecture and `32 bits` if you’re on a `32-bit` architecture.

Number literals can also use `_` as a visual separator to make the number easier to read

| Number literals  | Example       |
| ---------------- | ------------- |
| Decimal          | `98_222`      |
| Hex              | `0xff`        |
| Octal            | `0o77`        |
| Binary           | `0b1111_0000` |
| Byte (`u8` only) | `b'A'`        |
>If you’re unsure, Rust’s defaults are generally good places to start: integer types default to `i32`. The primary situation in which you’d use `isize` or `usize` is when indexing some sort of collection.
### Floating
Rust’s floating-point types are `f32` and `f64`, which are 32 bits and 64 bits in size, respectively. The default type is `f64` because on modern CPUs, it’s roughly the same speed as `f32` but is capable of more precision. All floating-point types are signed.
```rust
fn main() {
	let x = 2.0; // f64
	let y: f32 = 3.0; // f32
}
```
### Numeric operations
| Sign | Operation  |
| ---- | ---------- |
| +    | Sum        |
| -    | Difference |
| *    | Product    |
| /    | Quotient   |
| %    | Remainder  |
### Boolean
Booleans are one byte in size.
```rust
fn main() {
    let t = true;

    let f: bool = false; // with explicit type annotation
}
```
### Character
Rust’s `char` type is four bytes in size and represents a Unicode Scalar Value.
```rust
fn main() {
	let c = 'z';
	let z: char = 'ℤ';
	let heart_eyed_cat = '😻';
}
```

>Note that we specify `char` literals with single quotes, as opposed to string literals, which use double quotes.
## Compound Types
Can group multiple values into one type. Rust has two primitive compound types: tuples and arrays.
### Tuple
A _tuple_ is a general way of grouping together a number of values with a variety of types into one compound type. Tuples have a fixed length: once declared, they cannot grow or shrink in size.
```rust
fn main() {
	let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

To get the individual values out of a tuple, we can use pattern matching to destructure a tuple value, like this:
```rust
fn main() {
    let tup = (500, 6.4, 1);
    let (x, y, z) = tup;
    println!("The value of y is: {y}");
}
```

We can also access a tuple element directly by using a period (`.`) followed by the index of the value we want to access.
```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);
    let five_hundred = x.0;
    let six_point_four = x.1;
    let one = x.2;
}
```

>The tuple without any values has a special name, _unit_. This value and its corresponding type are both written `()` and represent an empty value or an empty return type. Expressions implicitly return the unit value if they don’t return any other value.
### Array
Unlike a tuple, every element of an array must have the same type.  Arrays have a fixed length.

Arrays are useful when you want your data allocated on the stack, the same as the other types we have seen so far, rather than the heap.
```rust
fn main() {
	let a = [1, 2, 3, 4, 5];
	let a: [i32; 5] = [1, 2, 3, 4, 5]; // With type annotation
	let a = [1; 5] // [1, 1, 1, 1, 1]
	
	// Array indexing	
	let first = a[0];
}
```
#### Invalid Array Element Access
If you enter the number past the end of the array, you'll see an output like this:
```plaintext
thread 'main' panicked at src/main.rs:x:y:
index out of bounds: the len is 5 but the index is z
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

The program resulted in a _runtime_ error at the point of using an invalid value in the indexing operation.

When you attempt to access an element using indexing, Rust will check that the index you’ve specified is less than the array length. If the index is greater than or equal to the length, Rust will panic. This check has to happen at runtime, especially in this case, because the compiler can’t possibly know what value a user will enter when they run the code later.