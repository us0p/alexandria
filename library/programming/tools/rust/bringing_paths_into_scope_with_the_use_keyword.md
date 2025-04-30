We can create a shortcut to a path with the `use` keyword once, and then use the shorter name everywhere else in the scope.
```rust
mod front_of_house {
	pub mod hosting {
		pub fn add_to_waitlist() {}
	}
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
	hosting::add_to_waitlist();
}
```

Note that `use` only creates the shortcut for the particular scope in which the `use` occurs.
```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
		// error!
        hosting::add_to_waitlist();
    }
}
```

The idiomatic way to bring a function into scope with `use` is to specify the path until the function's parent module. This means we need to specify the function's parent module when calling the function. This makes it clear that the function isn't locally defined.

On the other hand, when bringing in structs, enums, and other items with `use`, it's idiomatic to specify the full path.
```rust
use std::collections::HashMap;

fn main() {
	let mut map = HashMap::new();
	map.insert(1, 2);
}
```
## Providing new names with the `as` keyword
If you need to bring two types of the same name into the same scope with `use`, you can specify `as` and a new local name, or *alias*, for the type.
```rust
use std::fmt::Result;
use std::io::Result as IoResult;

// ...
```
## Re-exporting names with `pub use`
When we bring a name into scope with `use`, the name available in the new scope is private. To enable code that calls our code to refer to that name as if it had been defined in that code's scope, we can combine `pub` and `use`.
```rust
mod front_of_house {
	pub mod hosting {
		pub fn add_to_waitlist() {}
	}
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
	hosting::add_to_waitlist();
}
```
## Using external packages
Adding external packages to `Cargo.toml` as dependencies tells Cargo to download the external package and any dependencies from [`crates.io`](https://crates.io/) and make that package available to your project.

Then to bring the package definitions into the scope of our package, we add a `use` line starting with the name of the crate and list the items we wanted to bring into scope.
```rust
use rand::Rng;

fn main() {
	let secret_number = rand::thread_rng().gen_range(1..=100);
}
```
## Using nested paths to clean up large `use` lists
We can use nested paths to bring items from a given module in one line.
```rust
use std::cmp::Ordering;
use std::io;

// becomes:
use std::{cmp::Ordering, io};


// combining use statements that share a subpath:
use std::io;
use std::io::Write;

// becomes:
use std::io::{self, Write};
```
## The Glob operator
If we want to bring all public items defined in a path into scope, we can specify that path followed by the `*`, glob operator:
```rust
use std::collections::*;
```