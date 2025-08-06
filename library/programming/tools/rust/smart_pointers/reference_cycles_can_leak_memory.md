Rust’s memory safety guarantees make it difficult, but not impossible, to accidentally create memory leak.

We can see that Rust allows memory leaks by using `Rc<T>` and `RefCell<T>`: it’s possible to create references where items refer to each other in a cycle.

This creates memory leaks because the reference count of each item in the cycle will never reach 0, and the values will never be dropped.
## Creating a reference cycle
```Rust
use crate::List::{Cons, Nil}; // mock impl
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
    Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
    fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}

fn main() {
	let a = Rc::new(
		Cons(
			5, 
			RefCell::new(Rc::new(Nil))
		)
	);

    println!(
	    "a initial rc count = {}", // 1
	    Rc::strong_count(&a)
	);
	
    println!(
	    "a next item = {:?}", // Some(RefCell { value: Nil })
	    a.tail()
	);

    let b = Rc::new(
		Cons(
			10, 
			RefCell::new(Rc::clone(&a))
		)
	);

    println!(
	    "a rc count after b creation = {}", // 2
	    Rc::strong_count(&a)
	);
	
    println!(
	    "b initial rc count = {}", // 1
	    Rc::strong_count(&b)
	);
	
    println!(
	    // Some(
		//     RefCell { 
		// 	        value: Cons(
		// 		        5, 
		// 		        RefCell { value : Nil }
		// 		    ) 
		// 	   }
		// )
	    "b next item = {:?}", 
	    b.tail()
	);

    if let Some(link) = a.tail() {
        *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
	    "b rc count after changing a = {}",  // 2
	    Rc::strong_count(&b)
	);
	
    println!(
	    "a rc count after changing a = {}",  // 2
	    Rc::strong_count(&a)
	);

    // Uncomment the next line to see that we have a cycle;
    // it will overflow the stack because of Deref consecutive calls.
    // println!("a next item = {:?}", a.tail());
}
```

The reference count of the `Rc<List>` instances in both `a` and `b` is 2 after we change the list in `a` to point to `b`.

At the end of `main`, Rust drops the variable `b`, which decreases the reference count of the `b` `Rc<List>` instance from 2 to 1.

The memory that `Rc<List>` has on the heap won’t be dropped at this point, because its reference count is 1, not 0.

Then Rust drops `a`, which decreases the reference count of the `a` `Rc<List>` instance from 2 to 1 as well.

This instance’s memory can’t be dropped either, because the other `Rc<List>` instance still refers to it.

The memory allocated to the list will remain uncollected forever.

![[Pasted image 20250806122738.png]]

Creating reference cycles is not easily done, but it’s not impossible either.

If you have `RefCell<T>` values that contain `Rc<T>` values or similar nested combinations of types with interior mutability and reference counting, you must ensure that you don’t create cycles;
## Preventing reference cycles using `Weak<T>`
So far, we’ve demonstrated that calling `Rc::clone` increases the `strong_count` of an `Rc<T>` instance, and an `Rc<T>` instance is only cleaned up if its `strong_count` is 0.

You can also create a _weak reference_ to the value within an `Rc<T>` instance by calling `Rc::downgrade` and passing a reference to the `Rc<T>`.

Strong references are how you can share ownership of an `Rc<T>` instance.

Weak references don’t express an ownership relationship, and their count doesn’t affect when an `Rc<T>` instance is cleaned up.

They won’t cause a reference cycle because any cycle involving some weak references will be broken once the strong reference count of values involved is 0. `weak_count` doesn’t need to be 0 for the `Rc<T>` instance to be cleaned up.

When you call `Rc::downgrade`, you get a smart pointer of type `Weak<T>` which increases  the `weak_count` by 1.

Because the value that `Weak<T>` references might have been dropped,
you must make sure the value within `Weak<T>` still exists.

Do this by calling the `upgrade` method on a `Weak<T>` instance, which will return an `Option<Rc<T>>`.
```Rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
// Node owns its own children.
// We'll share the ownership with variables so we can access each `Node` in the tree directly.
// We also want to modify which nodes are children of another node, so we have RefCell<T> around Vec<Rc<Node>>.
struct Node {
	value: i32,
	children: RefCell<Vec<Rc<Node>>>,
}

fn main() {
	let leaf = Rc::new(Node {
		value: 3,
		children: RefCell::new(vec![]),
	});

	let branch = Rc::new(Node {
		value: 5,
		children: RefCell::new(vec![Rc::clone(&leaf)]),
	});
}
```

In the example above, `Node` in `leaf` has two owners, `leaf` and `branch`. We can get from `branch` to `leaf` through `branch.children`, but not the other way around.

We can add a `parent` to the node to get this two way relationship.

But, the parent can't be a `Rc<T>` because that would create a reference cycle with `leaf.parent` pointing to `branch` and `branch.children` pointing to `leaf`.

A parent should own its children, if parent is dropped, children should also be dropped, but not the other way around.

To represent this relationship we'll use `Weak<T>` instead of `Rc<T>` for the parent.
```Rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
	value: i32,
	parent: RefCell<Weak<Node>>,
	children: RefCell<Vec<Rc<Node>>>,
}

fn main() {
	let leaf = Rc::new(Node {
		value: 3,
		parent: RefCell::new(Weak::new()),
		children: RefCell::new(vec![]),
	});

	println!(
		"leaf parent = {:?}", // None
		leaf
			.parent
			.borrow()
			// Get a reference to the parent of leaf, in this case, None.
			.upgrade()
	);

	let branch = Rc::new(Node {
		value: 5,
		parent: RefCell::new(Weak::new()),
		children: RefCell::new(vec![Rc::clone(&leaf)]),
	});

	// Rc::downgrade() create a Weak<Node> reference to branch from the Rc<Node> in branch.
	*leaf.parent.borrow_mut() = Rc::downgrade(&branch);
	
	println!(
		"leaf parent = {:?}", // return reference to branch.
		leaf
			.parent
			.borrow()
			.upgrade()
	);
}
```
## Visualizing changes to `strong_count` and `weak_count`
Let’s look at how the `strong_count` and `weak_count` values of the `Rc<Node>` instances change by creating a new inner scope and moving the creation of `branch` into that scope.
```Rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    println!(
        "leaf strong = {}, weak = {}", // s = 1, w = 0
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

    {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

        println!(
	        // s = 1, 
	        // w = 1 (leaf.parent pointing to branch)
            "branch strong = {}, weak = {}", 
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

        println!(
	        // s = 2, (branch.children point to leaf)
	        // w = 0 (no Week references to leaf)
            "leaf strong = {}, weak = {}", 
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
    }
    // branch goes out of scope, it's strong_count goes to 0. Its node is droped.
    // Note that weak_count is still 1, but the node is droped anyway avoiding memory leaks.

    println!("leaf parent = {:?}", // None
	     leaf
			.parent
		    .borrow()
		    .upgrade()
	);
	
    println!(
        "leaf strong = {}, weak = {}", // s = 1, w = 0
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```