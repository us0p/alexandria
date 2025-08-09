They key elements of asynchronous programming in Rust are futures and Rust's `async` and `await` keywords. 

A _future_ is a value that may not be ready now but will become ready at some point in the future.

Rust provides a `Future` trait as a building block so that different async operations can be implemented with different data structures but with a common interface.

In Rust, futures are types that implement the `Future` trait.

You can apply the `async` keyword to blocks and functions to specify that they can be interrupted and resumed

Within an async block or async function, you can use the `await` keyword to _await a future_.

Any point where you await a future within an async block or function is a potential spot for that async block or function to pause and resume. In other words, every place where the code uses the `await` keyword, represents a place where control is handed back to the runtime.

The process of checking with a future to see if its value is available yet is called **polling**.

>`tokio` is the most widely used async runtime in Rust today, especially for web applications.

>`trpl` (The Rust Programming Language). It re-exports all types, traits , and functions you'll need, primarily the `futures` and `tokio` crates. The `futures` crate is an official home for Rust experimentation for async code, and it's actually where the `Future` trait was originally designed.
## Exemplifying async with a little web scrapper
```Rust
use trpl::Html;

async fn page_title(url: &str) -> Option<String> {
	let response = trpl::get(url).await;
	let response_text = response.text().await;
	Html::parse(&response_text)
		.select_first("title")
		.map(|title_element| title_element.inner_html())
}
```

Rust futures are **lazy**, they don't do anything until you ask them to with the `await` keyword.

Using `await` at the end of the expression makes method chaining easier, another way of writing `response_text` could be as
```Rust
// -- snip --
let response_text = tpl::get(url).await.text().await;
// -- snip --
```

When Rust sees a block marked with the `async` keyword, it compiles it into a unique, anonymous data type that implements the `Future` trait.

When Rust sees a function marked with `async`, it compiles it into a non-async function whose body is an async block.

An async function’s return type is the type of the anonymous data type the compiler creates for that async block.

To the compiler, a function definition such as the `async fn page_title` is equivalent to a non-async function defined like this:
```Rust
use std::future::Future;
use trpl::Html;

fn page_title(url: &str) -> impl Future<Output = Option<String>> {
	// This whole block is the expression returned from the function.
	async move {
		let text = trpl::get(url).await.text().await;
		Html::parse(&text)
			.select_first("title")
			.map(|title| title.inner_html())
	}
}
```
## Determining a Single page's title
```Rust
// error, main can't be async.
async fn main() {
	let args: Vec<String> = std::env::args().collec();
	let url = &args[1];
	// error: await can only be used inside async functions
	match page_title(url).await {
		Some(title) => println!("The title for {url} was {title}"),
		None => println!("{url} had no title"),
	}
}
```

The reason `main` can't be marked `async` is that async code needs a runtime.

Every Rust program that executes async code has at least one place where it sets up a runtime and executes the futures.

> `trpl::run(future)` runs a future to completion and returns the future's value. Behind the scenes, calling `run` sets up a runtime.

```Rust
fn main() {
	let args: Vec<String> = std::env::args().collec();

	trpl::run(async {
		let url = &args[1];
		match page_title(url).await {
			Some(title) => println!("The title for {url} was {title}"),
			None => println!("{url} had no title"),
		}
	})
}
```

To make the change of control to and from the runtime when we call `await`, Rust needs to keep track of the state involved in the `async` block so that the runtime can kick off some other work and then come back when it's ready to try advancing the first one again.

This is an invisible state machine, much like an enum like this to save the current state at each await point:
```Rust
enum PageTitleFuture<'a> {
	Initial { url: &'a str },
	GetAwaitPoint { url: &'a str },
	TextAwaitPoint { response: trpl::Response },
}
```

Writing the code to transition between each state by hand would be tedious and error-prone. Fortunately, the Rust compiler creates and manages the state machine data structures for async code automatically.

Ultimately, something has to execute this state machine, and that something is a runtime. (This is why you may come across references to _executors_ when looking into runtimes: an executor is the part of a runtime responsible for executing the async code.)
## Racing two URLs against each other
```Rust
use ::trpl::{Either, Html};

fn main() {
	let args: Vec<String> = std::env::args().collect();

	trpl::run(async {
		let title_fut_1 = page_title(&args[1]);
		let title_fut_2 = page_title(&args[2]);

		// returns a Either type, with the value of the future that finishes first.
		// it has two cases, Left or Right, it indicates one or the other.
		let (url, maybe_title) = match trpl::race(
			title_fut_1, 
			title_fut_2
		).await {
			Either::Left(left) => left,
			Either::Right(right) => right,
		};

		println!("{url} returned first");
		match maybe_title {
			Some(title) => println!("Its page title is: '{title}'");,
			None => println!("Its title could not be parsed."),
		}
	})
}

async fn page_title(url: &str) -> (&str, Option<String>) {
	let text = trpl::get(url).await.text().await;
	let title = Hrml::parse(&text)
		.select_first("title")
		.map(|title| title.inner_html());
	(url, title)
}
```