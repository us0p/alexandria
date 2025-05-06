## Validating References with Lifetimes
Rather than ensuring that a type has the behavior we want, lifetimes ensure that references are valid as long as we need them to be.

Every references in Rust has a *lifetime*, which is the scope for which that reference is valid.

Most time, lifetimes are implicit and inferred, just like most of the time, types are inferred. We must annotate types only when multiple types are possible. In a similar way, we must annotate lifetimes when the lifetimes of references could be related in a few different ways.

Rust requires us to annotate the relationships using generic lifetime parameters to ensure the actual references used at runtime will definitely be valid.
## Preventing Dangling References with Lifetimes
The main aim of lifetimes is to prevent *dangling references*, which cause a program to reference data other than the data it's intended to reference.
```rust
fn main() {
	let r;

	{
		let x = 5;
		r = &x;
	}

	println!("r: {r}");
}
```

This code won't compile, the error message says that the variable `x` doesn't live long enough. The reason is that `x` will be out of scope when the inner scope ends on line 7. But `r` is still valid for the outer scope, because its scope is larger, we say that it lives longer.
## The borrow checker
The Rust compiler has a *borrow checker* that compares scopes to determine whether all borrows are valid.
```rust
fn main() {
	let r;              // ---------+-- 'a 
		                //          | 
	{                   //          | 
		let x = 5;      // -+-- 'b  | 
		r = &x;         //  |       | 
	}                   // -+       | 
	                    //          | 
	println!("r: {r}"); //          | 
}                       // ---------+
```

Here, we’ve annotated the lifetime of `r` with `'a` and the lifetime of `x` with `'b`. As you can see, the inner `'b` block is much smaller than the outer `'a` lifetime block. At compile time, Rust compares the size of the two lifetimes and sees that `r` has a lifetime of `'a` but that it refers to memory with a lifetime of `'b`. The program is rejected because `'b` is shorter than `'a`: the subject of the reference doesn’t live as long as the reference.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Here, `x` has the lifetime `'b`, which in this case is larger than `'a`. This means `r` can reference `x` because Rust knows that the reference in `r` will always be valid while `x` is valid.
## Generic Lifetimes in Functions
```rust
fn main() {
	let string1 = String::from("abcd");
	let string2 = "xyz";

	let result = longest(string1.as_str(), string2);
	println!("The longest string is {result}");
}

fn longest(x: &str, y: &str) -> &str {
	if x.len() > y.len() {
		x
	} else {
		y
	}
}
```

The code above won't compile! Rust can't tell whether the reference being returned refers to `x` or `y`.

When we're defining this function, we don't know the concrete values that will be passed into this function, so we don't know whether the `if` case or the `else` case will execute. We also don't know the concrete lifetimes of the references that will be passed in. The borrow checker can't determine this either, because it doesn't know how the lifetimes of `x` and `y` relate to the lifetime of the return value.

To fix this error, we'll add generic lifetime parameters that define the relationship between the references so the borrow checker can perform its analysis.
## Lifetime Annotations Syntax
This annotations don't change how long any of the references live. Rather, they describe the relationships of the lifetimes of multiple references to each other without affecting the lifetimes.

Functions can accept references with any lifetime by specifying a generic lifetime parameter.

Lifetime annotations must start with an apostrophe `'` and are usually all lowercase and very short, like generic types. We place lifetime parameter annotations after the `&` of a reference, using a space to separate the annotation from the reference's type.
```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```
## Lifetime Annotations in Function Signatures
To use lifetime annotations in function signatures, we need to declare the generic *lifetime* parameters inside angle brackets between the function name and the parameter list.
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
		// ...
}
```

The notation in the code above expresses that the returned reference will be valid as long as both the parameters are valid. This is the relationship of the parameters and the return value.

In practice, it means that the lifetime of the reference returned by the `longest` function is the same as the smaller of the lifetimes of the values referred to by the function arguments. These relationships are what we want Rust to use when analyzing this code.

Remember, when we specify the lifetime parameters in this function signature, we’re not changing the lifetimes of any values passed in or returned. Rather, we’re specifying that the borrow checker should reject any values that don’t adhere to these constraints.

When annotating lifetimes in functions, the annotations go in the function signature, not in the function body. The lifetime annotations become part of the contract of the function, much like the types in the signature.
## Thinking in terms of lifetimes
When returning a reference from a function, the lifetime parameter for the return type needs to match the lifetime parameter for one of the parameters.

If the reference returned does not refer to one of the parameters, it must refer to a value created within this function. However, this would be a dangling reference because the value will go out of scope at the end of the function.

In this case, the best fix would be to return an owned data type rather than a reference so the calling function is then responsible for cleaning up the value.
```rust
// Compiles, code return x which has the same lifetame as 'a.
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
	x
}

// Fails to compile, returns dangling reference.
fn longest<'a>(x: &str, y: &str) -> &'a str {
	let result = String::from("really long string");
	result.as_str()
}
```
## Lifetime annotations in struct definitions
We can add lifetimes annotations to define references in structs. This annotation must be added to **every reference** in the struct's definition.
```rust
struct ImportantExcerpt<'a> {
	part: &'a str,
}

fn main() {
	let novel = String::from("Call me Ishmale. Some year ago...");
	let first_sentence = novel.split('.').next().unwrap();
	let i = ImportantExcerp {
		part: first_sentence,
	};
}
```
## Lifetime Elision
The function bellow compiles without lifetime annotations.
```rust
fn first_word(s: &str) -> &str {
	let bytes = s.as_bytes();

	for (i, &item) in bytes.iter().enumerate() {
		if item == b' ' {
			return &s[0..i];
		}
	}

	&s[..]
}
```

In early versions of Rust, this code wouldn't have compiled because every reference needed an explicit lifetime.
```rust
fn first_word<'a>(s: &'a str) -> &'a str {
	// ...
}
```

After writing a lot of Rust code, the Rust team found that Rust programmers were entering the same lifetime annotations over and over in particular situations. These situations were predictable and followed a few deterministic patterns. The developers programmed these patterns into the compiler’s code so the borrow checker could infer the lifetimes in these situations and wouldn’t need explicit annotations.

It's possible that more deterministic patterns will emerge and be added to the compiler.

The patterns programmed into Rust’s analysis of references are called the _lifetime elision rules_. These aren’t rules for programmers to follow; they’re a set of particular cases that the compiler will consider, and if your code fits these cases, you don’t need to write the lifetimes explicitly.

Lifetimes on function or method parameters are called *input lifetimes*, and on return values are called *output lifetimes*.

The compiler uses three rules to figure out the lifetimes of the references when there aren’t explicit annotations. The first rule applies to input lifetimes, and the second and third rules apply to output lifetimes. If the compiler gets to the end of the three rules and there are still references for which it can’t figure out lifetimes, the compiler will stop with an error. These rules apply to `fn` definitions as well as `impl` blocks.
- The compiler assigns a lifetime parameter to each parameter that's a reference. A function with one parameter gets one lifetime, a function with two parameter gets two different lifetimes, and so on.
- If there's exactly one input lifetime parameter, that lifetime is assigned to all output lifetime parameters, `fn foo<'a>(x: &'a i32) -> &'a i32`.
- If there are multiple input lifetime parameters, but one of them is `&self` or `&mut self` because this is a method, the lifetime of `self` is assigned to all output lifetime parameters.
## Lifetime annotations in method definitions
Lifetimes for struct fields always need to be declared after the `impl` keyword and then used after the struct's name because those lifetimes are part of the struct's type.
```rust
// The lifetime parameter declaration after impl and its use after the type name are required because the structs uses a lifetime in one if its fields.
impl<'a> ImportantExcerpt<'a> {
	// We're not required to annotate the lifetime to self because of the first elision rule.
	fn level(&self) -> i32 {
		3
	}
}

impl<'a> ImportantExcerpt<'a> {
	// applies the first elision rule and give each parameter a different lifetime.
	// because one of the parameters is &self, the third elision rules applies and the return type gets the lifetime of &self.
	fn announce_and_return_part(&self, announcement: &str) -> &str {
		println!("Attention please: {announcement}");
		self.part
	}
}
```
## The static lifetime
The `'static` lifetime denotes that the affected reference can live for the entire duration of the program. All string literals have the `'static` lifetime.
```rust
let s: &'static str = "I have a static lifetime.";
```

You might see suggestions in error messages to use the `'static` lifetime. But before specifying it as the lifetime for a reference, think about whether the reference you have actually lives the entire lifetime of your program or not, and whether you want it to.
## Generic type parameters, trait bounds, and lifetimes together
```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
	x: &'a str,
	y: &'a str,
	ann: T,
) -> &'a str
where
	T: Display,
{
	println!("Announcement! {ann}");
	if x.len() > y.len() {
		x
	} else {
		y
	}
}
```