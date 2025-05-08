```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();

for val in v1_iter {
	println!("Got: {val}");
}
```
## The Iterator trait and the `next` method
All iterators implement a trait name `Iterator` that is defined in the standard library.
```rust
pub trait Iterator {
	type Item; // Associated type

	fn next(&mut self) -> Option<Self::Item>;

	// ...
}
```

Implementing the `Iterator` trait requires that you also define an `Item` type, and this `Item` type is used in the return type of the `next` method.

The `Iterator` trait only requires implementors to define the `next` method, which returns one item of the iterator at a time wrapped in `Some` and, when iteration is over, returns `None`.
```rust
#[test]
fn iterator_demonstration() {
	let v1 = vec![1, 2, 3];

	let mut v1_iter = v1.iter();

	assert_eq!(v1_iter.next(), Some(&1));
	assert_eq!(v1_iter.next(), Some(&2));
	assert_eq!(v1_iter.next(), Some(&3));
	assert_eq!(v1_iter.next(), None);
}
```

Note that we needed to make `v1_iter` mutable: calling the `next` method on an iterator changes internal state that the iterator uses to keep track of where it is in the sequence. In other words, this code _consumes_, or uses up, the iterator. Each call to `next` eats up an item from the iterator. We didn’t need to make `v1_iter` mutable when we used a `for` loop because the loop took ownership of `v1_iter` and made it mutable behind the scenes.

Also note that the values we get from the calls to `next` are immutable references to the values in the vector. The `iter` method produces an iterator over immutable references. If we want to create an iterator that takes ownership of `v1` and returns owned values, we can call `into_iter` instead of `iter`. Similarly, if we want to iterate over mutable references, we can call `iter_mut` instead of `iter`.

Methods that call `next` are called *consuming adapters*, because calling them uses up the iterator. One example is the `sum` method, which takes ownership of the iterator and iterates through the items by repeatedly calling `next`.
```rust
#[test]
fn iterator_sum() {
	let v1 = vec![1, 2, 3];

	let v1_iter = v1.iter();

	let total: i32 = v1_iter.sum();

	assert_eq!(total, 6);
}
```

We aren't allowed to use `v1_iter` after the call to `sum` because `sum` takes ownership of the iterator we call it on.

*Iterator adapters* are methods defined on the `Iterator` trait that don't consume the iterator. Instead, they produce different iterators by changing some aspect of the original iterator.
```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

The `map` method returns a new iterator that produces the modified items.

This code produces as warning as iterators are lazy, we need to consume the iterator.
```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1
	.iter()
	.map(|x| x + 1)
	.collect(); // Consumes the iterator and collects the resulting values into a collection data type.

assert_eq!(v2, vec![2, 3, 4]);
```
## Comparing Performance: Loops vs. Iterators
Iterators, although a high-level abstraction, get compiled down to roughly the same code as if you'd written the lower-level code yourself.

Using this abstraction imposes no additional runtime overhead.

Rust performs *Unrolling*. It's an optimization that removes the overhead of the loop controlling code and instead generates repetitive code for each iteration of the loop.

All of the coefficients get stored in registers, which means accessing the values is very fast. There are no bounds checks on the array access at runtime. All these optimizations that Rust is able to apply make the resulting code extremely efficient. Now that you know this, you can use iterators and closures without fear! They make code seem like it’s higher level but don’t impose a runtime performance penalty for doing so.