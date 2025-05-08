Is a syntax in the form `::<SomeType>`.

Some methods like `Iterator.collect()` can yield many different types like `Vec, HashMaps, HashSet`, etc. Sometimes the compiler isn't able to determine which return type you want from that operation and thus you must specify it explicitly.

You can do this by explicitly typing the variable that's going to receive the value
```rust
fn main() {
	let numbers: Vec<i32> = vec![
		1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	];

	// compile error, compiler doesn't know the return type
	let even_numbers = numbers
		.into_iter()
		.filter(|n| n % 2 == 0)
		.collect();

	// solves problem by explicity telling the expected type
	let even_numbers: Vec<i32> = numbers
		.into_iter()
		.filter(|n| n % 2 == 0)
		.collect();

	// Solves the problem by using turbofish syntax
	// This means, collect this iteratior into a Vec<i32>
	let even_numbers = numbers
		.into_iter()
		.filter(|n| n % 2 == 0)
		.collect::<Vec<i32>>();
		
	println!("{:?}", even_numbers);
}
```
## Where can it be used?
Turbofish notation can only be used with generic functions, that's why it can be used with `.collect()`.

If you encountered a function like `fn foo<A, B, C>()` then you would be able to call it like `foo::<String, i32, f32>()`.

The turbofish can also be applied to other things such as structs with `SomeStruct::<SomeType>::some_method()`. The struct also need to be generic.