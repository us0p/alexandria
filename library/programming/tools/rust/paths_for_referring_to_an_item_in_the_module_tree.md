A path can take two forms:
- An absolute path is the full path starting from a crate root.
	- For code from an external crate, the absolute path begins with the crate name.
	- For code from the current crate, it starts with the literal `crate`.
- A relative path starts from the current module and users `self`, `super`, or an identifier in the current module.

Both absolute and relative paths are followed by one or more identifiers separated by double colons `::`.

```rust
mod front_of_house {
	pub mod hosting {
		pub fn add_to_waitlist() {}
	}
}

// front_of_house isn't public but eat_at_restaurand can refer to it because they're siblings.
pub fn eat_at_restaurant() {
	// Absolute path
	crate::front_of_house::hosting::add_to_waitlist();

	// Relative path
	front_of_house::hosting::add_to_waitlist();
}
```

Items in a parent module can't use the private items inside child modules, but items in child modules can use the items in their ancestor modules. This is because child modules wrap and hide their implementation details, but child modules can see the context in which they're defined.

Making a module public doesn't make its contents public.
## Starting Relative Paths with `super`
We can construct relative paths that begin in the parent module, rather than the current module or the crate root, by using `super` at the start of the path. This is like starting a file system path with the `..` syntax.
```rust
fn deliver_order() {}

mod back_of_house {
	fn fix_incorrect_order() {
		cook_order();
		super::deliver_order();
	}

	fn cook_order() {}
}
```
## Making Structs and Enums Public
If we use `pub` before a struct definition, we make the struct public, but the struct's fields will still be private. We can make each field public or not on a case-by-case basis.
```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not allowed
    // to see or modify the seasonal fruit that comes with the meal
    // meal.seasonal_fruit = String::from("blueberries");
}
```

Because the struct has a private field, it needs to provide a pub associated function that constructs an instance of `Breakfast` otherwise, we couldn't create an instance of `Breakfast` in `eat_at_restaurant` because we couldn't set the value of the private `seasonal_fruit` field in `eat_at_restaurant`

In contrast, if we make an enum public, all of its variants are then public.
```rust
mod back_of_house {
	pub enum Appetizer {
		Soup,
		Salad,
	}
}

pub fn eat_at_restaurant() {
	let order1 = back_of_house::Appetizer::Soup;
	let order2 = back_of_house::Appetizer::Salad;
}
```

Enums aren’t very useful unless their variants are public; it would be annoying to have to annotate all enum variants with `pub` in every case, so the default for enum variants is to be public. Structs are often useful without their fields being public, so struct fields follow the general rule of everything being private by default unless annotated with `pub`.