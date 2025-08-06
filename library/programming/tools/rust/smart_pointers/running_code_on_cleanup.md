The `Drop` trait lets you customize what happens when a value is about to go out of scope.

This trait is almost always used when implementing a smart pointer.

The `Drop` trait requires you to implement one method named `drop` that takes a mutable reference to `self`.

The `Drop` trait is included in the prelude, so we don’t need to bring it into scope.

```Rust
struct CustomSmartPointer {
	data: String,
}

impl Drop for CustomSmartPointer {
	fn drop(&mut self) {
		println!(
			"Dropping CustomSmartPointer with data: {}",
			self.data
		);
	}
}

fn main() {
	let c = CustomSmartPointer {
		data: String::from("My stuff"),
	};

	let d = CustomSmartPointer {
		data: String::from("other stuff"),
	};

	println!("CustomSmartPointers created.");
}
```

Variables are dropped in the reverse order of their creation, so `d` was dropped before `c`.

>Rust doesn’t let you call the `Drop` trait’s `drop` method manually because it would still automatically call `drop` on the value at the end of `main`. This would cause a _double free_ error; instead, you have to call the `std::mem::drop` (is in prelude) function provided by the standard library if you want to force a value to be dropped before the end of its scope.

```Rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c); // manually dropping c
    println!("CustomSmartPointer dropped before the end of main.");
}
```