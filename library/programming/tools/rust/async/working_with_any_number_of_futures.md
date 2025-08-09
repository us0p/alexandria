When we switched from `trpl::join` to `trpl::join3` in [Applying concurrency with async](applying_concurrency_with_async.md#Counting%20up%20on%20two%20tasks%20using%20message%20passing) we did it so we could await 3 futures.

If you have any **known** number of futures, you can use the macro:
```Rust
use trpl;

fn main() {
	// -- snip --
	trpl::join!(tx1_fut, tx_fut, rx_fut);
	// -- snip --
}
```

In real-world Rust, though, pushing futures into a collection and then waiting on some or all the futures of them to complete is a common pattern.

To check all the futures in some collection, we’ll need to iterate over and join on _all_ of them. The `trpl::join_all` function accepts any type that implements the `Iterator` trait.
```Rust
// -- snip --
    let futures = vec![tx1_fut, rx_fut, tx_fut];

    trpl::join_all(futures).await;
// -- snip --
```

Unfortunately, the code above doesn't compile, instead you'll get this error:
```plaintext
error[E0308]: mismatched types
  --> src/main.rs:45:37
   |
10 |         let tx1_fut = async move {
   |                       ---------- the expected `async` block
...
24 |         let rx_fut = async {
   |                      ----- the found `async` block
...
45 |         let futures = vec![tx1_fut, rx_fut, tx_fut];
   |                                     ^^^^^^ expected `async` block, found a different `async` block
   |
   = note: expected `async` block `{async block@src/main.rs:10:23: 10:33}`
              found `async` block `{async block@src/main.rs:24:22: 24:27}`
   = note: no two async blocks, even if identical, have the same type
   = help: consider pinning your async block and casting it to a trait object
```

This might be surprising. After all, none of the async blocks returns anything, so each one produces a `Future<Output = ()>`. Remember that `Future` is a trait, though, and that the compiler creates a unique enum for each async block.

Also, note the last few lines of the error message: **"no two async blocks, even if identical, have the same type"**.

To make this work, we need to use **trait objects**.

Using trait objects lets us treat each of the anonymous futures produced by these types as the same type, because all of them implement the `Future` trait.

```Rust
    let futures: Vec<Box<dyn Future<Output = ()>>> = vec![
	    Box::new(tx1_fut), 
	    Box::new(rx_fut),
	    Box::new(tx_fut)
	];

    trpl::join_all(futures).await;
```

We annotate the type of `futures` so the compiler can know that each box points to the same dynamic future.

But, we still receive compile errors from this code.

The the message tell us that the first async block does not implement the `Unpin` trait and suggests using `pin!` or `Box::pin` to resolve it.
```Rust
use std::pin::Pin;

// -- snip --
    let futures: Vec<Pin<Box<dyn Future<Output = ()>>>> = vec![
	    Box::pin(tx1_fut), 
	    Box::pin(rx_fut), 
	    Box::pin(tx_fut)
	];
// -- snip --
```

The code finally compiles and run as expected.

But, using `Pin<Box<T>>` adds a small amount of overhead from putting these futures on the heap with `Box` (we did it so that the types line up).

As noted, `Pin` is a wrapper type, so we can get the benefit of having a single type in `Vec` without doing a heap allocation.

However, we must still be explicit about the type of the pinned reference; otherwise, Rust will still not know to interpret these as dynamic trait objects, which is what we need them to be in the `Vec`.

```Rust
use std::pin::{Pin, pin};

// -- snip --
    let tx1_fut = pin!(async move {
        // --snip--
    });
    let rx_fut = pin!(async {
        // --snip--
    });
    let tx_fut = pin!(async move {
        // --snip--
    });
    let futures: Vec<Pin<&mut dyn Future<Output = ()>>> = vec![
	    tx1_fut, 
	    rx_fut,  
	    tx_fut
	];
```

You must note that all this examples only consider futures that have the same underlying return type.

If we need to join futures with different return types, we must use (`trpl::join`, `trpl::join3` or `trpl::join!`), but in that case we need to know the number of futures we're dealing with.
## Racing futures
Consider the code bellow using the `trpl::race()` call we saw in [Racing two URLs against each other](futures_and_async_syntax.md#Racing%20two%20URLs%20against%20each%20other).
```Rust
    let slow = async {
        println!("'slow' started.");
        trpl::sleep(Duration::from_millis(100)).await;
        println!("'slow' finished.");
    };
    let fast = async {
        println!("'fast' started.");
        trpl::sleep(Duration::from_millis(50)).await;
        println!("'fast' finished.");
    };
	// Ignore the Either instance returned
    trpl::race(slow, fast).await;
```

Notice that if you flip the order of the arguments to `race`, the order of the “started” messages changes, even though the `fast` future always completes first. That’s because the implementation of this particular `race` function is not fair.

Other implementations _are_ fair and will randomly choose which future to poll first.

Regardless of whether the implementation of race we’re using is fair, though, _one_ of the futures will run up to the first `await` in its body before another task can start.

Recall that at each await point, Rust gives a runtime a chance to pause the task and switch to another one if the future being awaited isn’t ready.

The inverse is also true: Rust _only_ pauses async blocks and hands control back to a runtime at an await point. Everything between await points is synchronous.

That means if you do a bunch of work in an async block without an await point, that future will block any other futures from making progress.

You may sometimes hear this referred to as one future _starving_ other futures.
## Yielding control to the runtime
```Rust
// Simulates a long running function
fn slow(name: &str, ms: u64) {
	// using thread::slepp to block thread for Duration
    thread::sleep(Duration::from_millis(ms));
    println!("'{name}' ran for {ms}ms");
}

let a = async {
    println!("'a' started.");
    slow("a", 30);
    slow("a", 10);
    slow("a", 20);
    trpl::sleep(Duration::from_millis(50)).await;
    println!("'a' finished.");
}
let b = async {
    println!("'b' started.");
    slow("b", 75);
    slow("b", 10);
    slow("b", 15);
    slow("b", 350);
    trpl::sleep(Duration::from_millis(50)).await;
    println!("'b' finished.");
}
trpl::race(a, b).await;
```

To begin, each future only hands control back to the runtime _after_ carrying out a bunch of slow operations.

As with our earlier example, `race` still finishes as soon as `a` is done.

There’s no interleaving between the two futures, though.

To allow both futures to make progress between their slow tasks, we need await points so we can hand control back to the runtime.

That means we need something we can await!
```Rust
// -- snip ---
    let a = async {
        println!("'a' started.");
        slow("a", 30);
        trpl::yield_now().await;
        slow("a", 10);
        trpl::yield_now().await;
        slow("a", 20);
        trpl::yield_now().await;
        println!("'a' finished.");
    };
    let b = async {
        println!("'b' started.");
        slow("b", 75);
        trpl::yield_now().await;
        slow("b", 10);
        trpl::yield_now().await;
        slow("b", 15);
        trpl::yield_now().await;
        slow("b", 350);
        trpl::yield_now().await;
        println!("'b' finished.");
    };
// -- snip --
```

We use `trpl::yield_now()` to handle control back to the runtime.

This means that async can be useful even for compute-bound tasks, depending on what else your program is doing, because it provides a useful tool for structuring the relationships between different parts of the program.

This is a form of _cooperative multitasking_, where each future has the power to determine when it hands over control via await points.

Each future therefore also has the responsibility to avoid blocking for too long.

While yielding control in this way is relatively inexpensive, it’s not free.

In many cases, trying to break up a compute-bound task might make it significantly slower, so sometimes it’s better for _overall_ performance to let an operation block briefly.
## Building our own async abstractions
We'll implement a `timeout` function with the async building blocks we already have.

Here's how it'll be used:
```Rust
    let slow = async {
        trpl::sleep(Duration::from_millis(100)).await;
        "I finished!"
    };
    match timeout(slow, Duration::from_millis(10)).await {
        Ok(message) => println!("Succeeded with '{message}'"),
        Err(duration) => {
            println!("Failed after {} seconds", duration.as_secs())
        }
    }
```

Let's think abou the API for `timeout`:
- It needs to be an async function itself so we can await it.
- Its first parameter should be a future to run. We can make it generic to allow it to work with any future.
- Its second parameter will be the maximum time to wait. If we use a `Duration`, that will make it easy to pass along to `trpl::sleep`.
- It should return a `Result`. If the future completes successfully, the `Result` will be `Ok` with the value produced by the future. If the timeout elapses first, the `Result` will be `Err` with the duration that the timeout waited for.

```Rust
async fn timeout<F: Future>(
    future_to_try: F,
    max_time: Duration,
) -> Result<F::Output, Duration> {
    // Here is where our implementation will go!
}
```

Now let’s think about the _behavior_ we need: we want to race the future passed in against the duration.

We can use `trpl::sleep` to make a timer future from the duration, and use `trpl::race` to run that timer with the future the caller passes in.

We also know that `race` is not fair, polling arguments in the order in which they are passed.

Thus, we pass `future_to_try` to `race` first so it gets a chance to complete even if `max_time` is a very short duration.
```Rust
use trpl::Either;

// --snip--

fn main() {
    trpl::run(async {
        let slow = async {
            trpl::sleep(Duration::from_secs(5)).await;
            "Finally finished"
        };

        match timeout(slow, Duration::from_secs(2)).await {
            Ok(message) => println!("Succeeded with '{message}'"),
            Err(duration) => {
                println!("Failed after {} seconds", duration.as_secs())
            }
        }
    });
}

async fn timeout<F: Future>(
    future_to_try: F,
    max_time: Duration,
) -> Result<F::Output, Duration> {
    match trpl::race(future_to_try, trpl::sleep(max_time)).await {
        Either::Left(output) => Ok(output),
        Either::Right(_) => Err(max_time),
    }
```