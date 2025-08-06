## Allowing transference of ownership between threads with `Send`
The `std::marker::Send` trait indicates that ownership of values of the type implementing `Send` can be transferred between threads.

Any type composed entirely of `Send` types is automatically marked as `Send` as well. Almost all primitive types are `Send`, aside from raw pointers.
## Allowing access from multiple threads with `Sync`
The `std::marker::Sync` indicates that it is safe for the type implementing `Sync` to be referenced from multiple threads.

In other words, any type `T` implements `Sync` if `&T` (an immutable reference to `T`) implements `Send`, meaning the reference can be sent safely to another thread.

Similar to `Send`, primitive types all implement `Sync`, and types composed entirely of types that implement `Sync` also implement `Sync`.
## Implementing `Send` and `Sync` Manually Is Unsafe
Because types composed entirely of other types that implement the `Send` and `Sync` traits also automatically implement `Send` and `Sync`, we don’t have to implement those traits manually. 

As marker traits, they don’t even have any methods to implement. They’re just useful for enforcing invariants related to concurrency.

Manually implementing these traits involves implementing unsafe Rust code.