In the majority of cases, ownership is clear: you know exactly which variable owns a given value.

However, there are cases when a single value might have multiple owners.

For example, in graph data structures, multiple edges might point to the same node, and that node is conceptually owned by all of the edges that point to it.

A node shouldn’t be cleaned up unless it doesn’t have any edges pointing to it and so has no owners.

You can enable multiple ownership explicitly by using the Rust type `Rc<T>`, which is an abbreviation for _reference counting_.

The `Rc<T>` type keeps track of the number of references to a value to determine whether or not the value is still in use.

If there are zero references to a value, the value can be cleaned up without any references becoming invalid.

We use the `Rc<T>` type when we want to allocate some data on the heap for multiple parts of our program to read and we can’t determine at compile time which part will finish using the data last

>Note that `Rc<T>` is only for use in single-threaded scenarios.

>`Rc<T>` allows you to share data between multiple parts of your program for reading only.

```Rust
enum List {
    Cons(i32, Box<List>), // Cons own the list
    Nil,
}

use crate::List::{Cons, Nil}; // mock code

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
    let b = Cons(3, Box::new(a)); // a is moved here
    let c = Cons(4, Box::new(a)); // error, a was moved
}

// now using Reference Count
use crate::List::{Cons, Nil};
use std::rc::Rc;

enum List {
	Const(i32, Rc<List>), // Rc<T> points to a List.
	Nil,
}

fn main() {
	let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
	
	// Note that we don't take ownership of a anymore.
	// Istead, we clone the Rc<List> a is holding.
	// This increases the number of references from 1 to 2.
	// a and b share ownership of data in the Rc<List>.
    let b = Cons(3, Rc::clone(&a));

	// Increases number of references from 2 to 3.
	// a, b and c share ownership of Rc<List>.
    let c = Cons(4, Rc::clone(&a));
}
```

The implementation of `Rc::clone` doesn’t make a deep copy of all the data like most types’ implementations of `clone` do.

The call to `Rc::clone` only increments the reference count, which doesn’t take much time.

We can use `Rc::strong_count(rc)` to get the current number of references count to that owned value.