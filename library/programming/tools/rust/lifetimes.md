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