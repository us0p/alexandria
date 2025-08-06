In a way, channels in any programming language are similar to single ownership, because once you transfer a value down a channel, you should no longer use that value. Shared-memory concurrency is like multiple ownership: multiple threads can access the same memory location at the same time.

[Smart pointers](smart_pointers.md) make multiple ownership possible. While multiple ownership can add complexity, Rust's type system and ownership rules greatly assist in getting this management correct.
## Using Mutexes to allow access to data from one thread at the time
[Mutexes](mutexes.md) have a reputation for being difficult to use because you have to remember two rules:
1. You must attempt to acquire the lock before using the data.
2. When you're done with the data the mutex's guarding, you must unlock the data so other threads can acquire the lock.
```Rust
use std::sync::Mutex;

fn main() {
	let m = Mutex::new(5);

	{
		let mut num = m
			.lock() // must be called,acquires the lock. blocks the current thread so it can't do any work until it's our turn to have the lock.
			.unwrap();
		*num = 6;
	}

	println!("m = {m:?}");
}
```

The call to `lock` would fail if another thread holding the lock panicked. In that case, no one would ever be able to get the lock. We're using `unwrap` for this thread to panic if we're in that situation.

The call to `Mutex::lock()` returns a smart pointer called `MutexGuard`, wrapped in a `LockResult` that we handled with `unwrap`.

The `MutexGuard` implements `Deref` and `Drop` that releases the lock automatically when a `MutexGuard` goes out of scope.
## Sharing `Mutex<T>` between multiple threads
```Rust
use std::sync::Mutex;
use std::thread;

fn main() {
	let counter = Mutex::new(0);
	let mut handles = vec![];

	for _ in 0..10 {
		// Error, using counter after was moved.
		let handle = thread::spawn(move || {
			let mut num = counter
				.lock().
				unwrap();

			*num += 1;
		});
		handles.push(handle);
	}


	for handle in handlers {
		handle
			.join()
			.unwrap();
	}

	println!("Result: {}", *counter.lock().unwrap());
}
```

If we try to use the `Rc<T>` smart pointer to allow multiple owners to the counter mutex:
```Rust
// -- snip ---
let counter = Rc<Mutex::new(0));

for _ in 0..10 {
	// Creating a clone to allow multiple owner over the mutex.
	let counter = Rc::clone(&counter);
	// same code
}
// -- snip --
```

The change in the code above still produces a compile error, `"Rc<Mutex<i32>> cannot be sent between threads safely. Trait 'Send' is not implemented for 'Rc<Mutex<i32>>'`.

`Send` is one of the traits that ensures the types we use with threads are meant for use in concurrent situations.
## Atomic Reference Counting with `Arc<T>`
`Arc<T>` is like `Rc<T>` but thread safe.

Atomic Reference-Counted Type (`Arc<T>`).

Atomics are an additional kind of concurrency primitive, but, right now, we just need to know that atomics work like primitive types but are safe to share across threads.

You can find more in the doc [std::sync::atomic](https://doc.rust-lang.org/std/sync/atomic/index.html)

Thread safe types come with a performance penalty, that's the reason default Rust primitive types aren't atomic by default.

`Arc<T>` uses the same interface as `Rc<T>`, so the code bellow compiles and runs.
```Rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
	let counter = Arc::new(Mutex::new(0));
	let mut handles = vec![];

	for _ in 0..10 {
		let counter = Arc::clone(&counter);
		let handle = thread::spawn(move || {
			let mut num = counter.lock().unwrap();

			*num += 1;
		});
		handles.push(handle);
	}


	for handle in handles {
		handle.join().unwrap();
	}

	println!("Result: {}", *counter.lock().unwrap());
}
```
## Similarities between `RefCell<T>/Rc<T>` and `Mutex<T>/Arc<T>`
`Mutex<T>` provides interior mutability, as the `Cell` family does.

In the same way we [used](interior_mutability_pattern.md) `RefCell<T>` to allow us to mutate contents inside an `Rc<T>`, we use `Mutex<T>` to mutate contents inside an `Arc<T>`.

[Recall](reference_cycles_can_leak_memory.md) that using `Rc<T>` came with the risk of creating reference cycles, where two `Rc<T>` values refer to each other, causing memory leaks. Similarly, `Mutex<T>` comes with the risk of creating _deadlocks_.