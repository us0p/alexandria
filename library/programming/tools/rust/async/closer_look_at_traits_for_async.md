## The Future trait
Here's how Rust define it:
```Rust
use std::pin::Pin;
use std::task::{Context, Poll};

pub trait Future {
	// associated type
	// Represents the value to what the future resolves to
	type Output;

	fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>:
}
```

The Poll type returned by `Future::poll()` is defined as:
```Rust
enum Poll<T> {
	Ready(T),
	Pending,
}
```

>With most futures, the caller should not call `poll` again after the future has returned `Ready`. Many futures will panic if polled again after becoming ready.

When you see code that uses `await`, Rust compiles it under the hood to code that calls `poll`. If you look back into our first async [example](futures_and_async_syntax.md#Determining%20a%20Single%20page's%20title), where we printed out the page title for a single URL once it resolved, Rust compiles it into something kind of (although not exactly) like this:

```rust
let mut page_title_fut = page_title(url);
// while pending, keep pooling until it's complete.
loop {
	match page_title(url).poll() {
	    Ready(page_title) => match page_title {
	        Some(title) => println!("The title for {url} was {title}"),
	        None => println!("{url} had no title"),
	    }
	    Pending => {
	        // continue
	    }
	}
}
```

If Rust compiled it to exactly that code, though, every `await` would be blocking.

Instead, Rust makes sure that the loop can hand off control to something that can pause work on this future to work on other futures and then check this one again later.

As we’ve seen, that something is an async runtime, and this scheduling and coordination work is one of its main jobs.

>The basic mechanics of futures: a runtime _polls_ each future it is responsible for, putting the future back to sleep when it is not yet ready.
## The Pin and Unpin traits
The `cx` parameter and its `Context` type are the key to how a runtime actually known when to check any given future while still being lazy.

But, we'll focus on the type for `self`.

A type annotation for `self` works like type annotations for other function parameters, but with two key differences:
- It tells Rust what type `self` must be for the method to be called.
- It can't be just any type. It's restricted to the type on which the method is implemented, a reference or smart pointer to that type, or a `Pin` wrapping a reference to that type.

If we want to poll a future to check whether it is `Pending` or `Ready`, we need a `Pin`-wrapped mutable reference to the type.

> Directly await a future with `await` pins the future implicitly. That's why we don't need to use `pin!` everywhere we want to await futures.

`Pin` is a wrapper for pointer-like types such as `&`, `&mut`, `Box`, and `Rc`. (Technically, `Pin` works with types that implement the `Deref` or `DerefMut` traits, but this is effectively equivalent to working only with pointers.)

`Pin` is not a pointer itself and doesn’t have any behavior of its own like `Rc` and `Arc` do with reference counting; it’s purely a tool the compiler can use to enforce constraints on pointer usage.

So how exactly does `Pin` relate to `Unpin`, and why does `Future` need `self` to be in a `Pin` type to call `poll`?

[Remember](futures_and_async_syntax.md#Determining%20a%20Single%20page's%20title) that a series of await points in a future get compiled into a state machine, and the compiler makes sure that state machine follows all of Rust’s normal rules around safety, including borrowing and ownership.

To make that work, Rust looks at what data is needed between one await point and either the next await point or the end of the async block.

It then creates a corresponding variant in the compiled state machine.

Each variant gets the access it needs to the data that will be used in that section of the source code, whether by taking ownership of that data or by getting a mutable or immutable reference to it.

If we get anything wrong about the ownership or references in a given async block, the borrow checker will tell us.

When we want to move around the future that corresponds to that block—[like moving it into a `Vec` to pass to `join_all`](working_with_any_number_of_futures.md)—things get trickier.

When we move a future, whether by pushing it into a data structure to use as an iterator with `join_all` or by returning it from a function, that actually means moving the state machine Rust creates for us.

And unlike most other types in Rust, the futures Rust creates for async blocks can end up with references to themselves in the fields of any given variant

By default, though, any object that has a reference to itself is unsafe to move, because references always point to the actual memory address of whatever they refer to.

If you move the data structure itself, those internal references will be left pointing to the old location.

However, that memory location is now invalid.

If we could instead make sure the data structure in question _doesn’t move in memory_, we wouldn’t have to update any references.

`Pin` builds on that to give us the exact guarantee we need.

When we _pin_ a value by wrapping a pointer to that value in `Pin`, it can no longer move.

Thus, if you have `Pin<Box<SomeType>>`, you actually pin the `SomeType` value, _not_ the `Box` pointer.

![[Pasted image 20250809144715.png]]

In fact, the `Box` pointer can still move around freely.

Remember: we care about making sure the data ultimately being referenced stays in place.

If a pointer moves around, **but the data it points to is in the same place**, there’s no potential problem.

![[Pasted image 20250809144826.png]]

However, most types are perfectly safe to move around, even if they happen to be behind a `Pin` wrapper.

We only need to think about pinning when items have internal references.

You can move around a `Vec`, for example, without worrying (there's no internal reference).

Given only what we have seen so far, if you have a `Pin<Vec<String>>`, you’d have to do everything via the safe but restrictive APIs provided by `Pin`, even though a `Vec<String>` is always safe to move if there are no other references to it.

We need a way to tell the compiler that it’s fine to move items around in cases like this—and that’s where `Unpin` comes into play.

`Unpin` is a marker trait, [similar to the `Send` and `Sync` traits](extensible_concurrency.md), and thus has no functionality of its own.

`Unpin` informs the compiler that a given type **does not need to uphold any guarantees about whether the value in question can be safely moved**.

Just as with `Send` and `Sync`, the compiler implements `Unpin` automatically for all types where it can prove it is safe.

A special case, again similar to `Send` and `Sync`, is where `Unpin` is **not** implemented for a type.

The notation for this is `impl !Unpin for SomeType`, where `SomeType` is the name of a type that **does need to uphold those guarantees to be safe whenever a pointer to that type is used in a `Pin`**.

In other words, there are two things to keep in mind about the relationship between `Pin` and `Unpin`.

First, `Unpin` is the “normal” case, and `!Unpin` is the special case.

Second, whether a type implements `Unpin` or `!Unpin` **only**_ matters when you’re using a pinned pointer to that type like `Pin<&mut SomeType>`.
## The Stream trait
`Stream` has no definition in the standard library as of this writing, but there _is_ a very common definition from the `futures` crate used throughout the ecosystem.

Let’s review the definitions of the `Iterator` and `Future` traits before looking at how a `Stream` trait might merge them together.

From `Iterator`, we have the idea of a sequence: its `next` method provides an `Option<Self::Item>`.

From `Future`, we have the idea of readiness over time: its `poll` method provides a `Poll<Self::Output>`.

To represent a sequence of items that become ready over time, we define a `Stream` trait that puts those features together:
```Rust
use std::pin::Pin;
use std::task::{Context, Poll};

trait Stream {
	// Associated type
    type Item;

	// method to get next items.
	// it polls in the same way Future::poll does.
	// it produces a sequence of items in the same way Iterator::next does.
    fn poll_next(
        self: Pin<&mut Self>,
        cx: &mut Context<'_>
    ) -> Poll<Option<Self::Item>>;
	// The outer type is Poll, because it has to be checked for readiness, just as future does.

	// The inner type is Option, because it need to signal whether there are more messages, just as an iterator does.
}
```

In the example we saw in the section on [streaming](streams_futures_in_sequence.md), though, we didn’t use `poll_next` _or_ `Stream`, but instead used `next` and `StreamExt`.

We _could_ work directly in terms of the `poll_next` API by hand-writing our own `Stream` state machines, of course, just as we _could_ work with futures directly via their `poll` method.

Using `await` is much nicer, though, and the `StreamExt` trait supplies the `next` method so we can do just that:

```rust
trait StreamExt: Stream {
    async fn next(&mut self) -> Option<Self::Item>
    where
        Self: Unpin;

    // other methods...
}
```

The `StreamExt` trait is also the home of all the interesting methods available to use with streams.

`StreamExt` is automatically implemented for every type that implements `Stream`, but these traits are defined separately to enable the community to iterate on convenience APIs without affecting the foundational trait.