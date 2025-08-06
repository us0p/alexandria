_Interior mutability_ is a design pattern in Rust that allows you to mutate data even when there are immutable references to that data;

normally, this action is disallowed by the borrowing rules. To mutate data, the pattern uses `unsafe` code inside a data structure to bend Rust’s usual rules that govern mutation and borrowing.

We can use types that use the interior mutability pattern only when we can ensure that the borrowing rules will be followed at runtime, even though the compiler can’t guarantee that. The `unsafe` code involved is then wrapped in a safe API, and the outer type is still immutable.
## Enforcing borrowing rules at runtime with `RefCell<T>`
Remember the [borrowing rules](references_and_borrowing.md). With `RefCell<T>`, these rules are enforced _at runtime_. 

With references, if you break these rules, you’ll get a compiler error. With `RefCell<T>`, if you break these rules, your program will **panic and exit**.

Most of the time, checking borrowing rules at compile time is the best approach as there's no runtime overhead and bugs are caught early in the development process.

The advantage of checking the borrowing rules at runtime instead is that certain memory-safe scenarios are then allowed, where they would’ve been disallowed by the compile-time checks.

>The `RefCell<T>` type is useful when you’re sure your code follows the borrowing rules but the compiler is unable to understand and guarantee that.

>`RefCell<T>` is only for use in single-threaded scenarios and will give you a compile-time error if you try using it in a multithreaded context.

Because `RefCell<T>` allows mutable borrows checked at runtime, you can mutate the value inside the `RefCell<T>` even when the `RefCell<T>` is immutable.

Mutating the value inside an immutable value is the _interior mutability_ pattern.

>Your code would incur a small runtime performance penalty as a result of keeping track of the borrows at runtime rather than compile time.

```Rust
pub trait Messenger {
	// method takes an immutable reference to `self` and the text of the message.
    fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(messenger: &'a T, max: usize) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

    pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max = self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger.send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent warning: You've used up over 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
                .send("Warning: You've used up over 75% of your quota!");
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    struct MockMessenger {
        sent_messages: Vec<String>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
			// fails because we have an immutable reference to self.
			// For this to be possible we would need a mutable reference.
			// the immutable reference comes from the trait signature.
			// we can't change the trait signature just for testing.
            self.sent_messages.push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

If we store the `sent_messages` within a `RefCell<T>`, the `send` method will be able to modify `sent_messages` to store the messages.
```Rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
		// Using RefCell to allow mutable borrow in an immutable reference
        sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self
	            .sent_messages
	            .borrow_mut() // gets mutable reference to the value inside RefCell<T>.
	            .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        // --snip--

        assert_eq!(
	        mock_messenger
		        .sent_messages
		        .borrow() // gets immutable reference to the value inside RefCell<T>.
		        .len(),
		     1
		);
    }
}
```
## Keeping track of borrows at runtime with `RefCell<T>`
The methods we studied are part of the safe API that belongs to `RefCell<T>`.
- `RefCell::borrow()` returns the smart pointer type `Ref<T>`.
- `RefCell::borrow_mut()` returns the smart pointer type `RefMut<T>`.

Both types implement `Deref`, so we can treat them like regular references.

The `RefCell<T>` keeps track of how many `Ref<T>` and `RefMut<T>` smart pointers are currently active.

Every time we call `borrow`, the `RefCell<T>` increases its count of how many immutable borrows are active.

When a `Ref<T>` value goes out of scope, the count of immutable borrows goes down by 1.

We can have many immutable borrows or one mutable borrow at any point in time.

If we try to create two **mutable borrows** active in the same scope we'll receive a compile time error.
```Rust
impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            let mut one_borrow = self
	            .sent_messages
	            .borrow_mut();

			// Panics, multiple mutable borrows in the same scope.
            let mut two_borrow = self
	            .sent_messages
	            .borrow_mut();

            one_borrow.push(String::from(message));
            two_borrow.push(String::from(message));
        }
    }
```
## Allowing multiple owners of mutable data with `Rc<T>` and `RefCell<T>`
A common way to use `RefCell<T>` is in combination with `Rc<T>`.

If you have an `Rc<T>` that holds a `RefCell<T>`, you can get a value that can have multiple owners _and_ that you can mutate.

The example on `Rc<T>` [here](reference_counter_smart_pointer.md) uses it to allow multiple lists to share ownership of another list.

Because `Rc<T>` holds only immutable values, we can't change any of the values in the list once we've created them.

We can add `RefCell<T>` to add mutability to values in the list.
```Rust
use crate::List::{Cons, Nil}; // mock impl
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
	Cons(Rc<RefCell<i32>>, Rc<List>),
	Nil,
}

fn main() {
	let value = Rc::new(RefCell::new(5));

	let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));

	let b = Cons(Rc::new(RefCell::new(3)), Rc::clone(&a));
	let c = Cons(Rc::new(RefCell::new(4)), Rc::clone(&a));

	*value.borrow_mut() += 10; // value = 15
	// also updates all the references to it.
	
	println!("a after = {a:?}");
	println!("b after = {b:?}");
	println!("c after = {c:?}");
}
```