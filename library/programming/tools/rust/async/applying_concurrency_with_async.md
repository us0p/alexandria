In many cases, the APIs for working with concurrency using async are very similar to those for using threads.

In other cases, they end up being quite different.

Even when the APIs _look_ similar between threads and async, they often have different behavior, and they nearly always have different performance characteristics.

Similar to how we [created a new thread with span](shared_state_concurrency.md#Atomic%20Reference%20Counting%20with%20`Arc<T>`) to count up on two separate threads. We'll do the same with `async`.
```Rust
use std::time::Duration;

fn main() {
	// creates runtime
    trpl::run(async {
		// create a new task simlar to how we create a new thread.
        trpl::spawn_task(async {
            for i in 1..10 {
                println!("hi number {i} from the first task!");
				// async version of thread::sleep.
                trpl::sleep(Duration::from_millis(500)).await;
            }
        });

        for i in 1..5 {
            println!("hi number {i} from the second task!");
            trpl::sleep(Duration::from_millis(500)).await;
        }
    });
}
```

The results from the exemple above are non-deterministic (they will produce different results each time they're run).

This code stops as soon as the `for` loop in the body of the main async block finishes (we'll most probably not see all the numbers in the first task), because the task spawned by `spawn_task` is shut down when the `main` function ends.

If you want to run all the way to the task's completion, you will need to use a join handle to wait for the first task to complete.

We can use `await` because the task handle itself is a future. Its `Output` type is a `Result`.
```Rust
// -- snip --
    let handle = trpl::spawn_task(async {
        for i in 1..10 {
            println!("hi number {i} from the first task!");
            trpl::sleep(Duration::from_millis(500)).await;
        }
    });
    for i in 1..5 {
        println!("hi number {i} from the second task!");
        trpl::sleep(Duration::from_millis(500)).await;
    }
    handle.await.unwrap();
// -- snip --
```

With this change, we'll se all the numbers in the first task.

It looks like `async` and `threads` give us the same basic outcomes, with different syntax.

The bigger difference is that we didn't need to spawn another operating system thread to do this.

In fact, because `async` blocks compile to anonymous futures, we can put each loop in an `async` block and have the runtime run them both to completion using `trpl::join`.

```Rust
// -- snip --
    let fut1 = async {
        for i in 1..10 {
            println!("hi number {i} from the first task!");
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };
    let fut2 = async {
	    for i in 1..5 {
	        println!("hi number {i} from the second task!");
	        trpl::sleep(Duration::from_millis(500)).await;
	    }
	};
	// Produces a single new future whose output is a tuple with the output of each future you passed in once they BOTH complete.
    trpl::join(fut1, fut2).await; // returns a tuple containing two unit values.
// -- snip --
```

By joining the futures together, now we see the **exact same order every time** (we have a deterministic result).

This is because `trpl::join` is **fair**, meaning it checks each future equally often, alternating between them, never lets one race ahead if the other is ready.

With Threads, the operating system decides which thread to check and how long to let it run.

With `async` Rust, the runtime decides which task to check. In practice, `async` runtime might use operating system threads under the hood as part of how it manages concurrency, so guaranteeing fairness can be more work for a runtime, but possible.

>Runtimes don't have to guarantee fairness for any operation, you usually can choose whether you want it or not.
## Counting up on two tasks using message passing
```Rust
// -- snip --
	let (tx, mut tx) = trpl::channel();

	let val = String::from("hi");
	tx.send(val).unwrap();

	let received = rx.recv().await.unwrap();
	println!("Got: {received}");
// -- snip --
```

Here we use an `async` version of the [MPSC](using_message_passing.md). The difference in the API is that the `async` version uses a **mutable** rather than an immutable receiver `rx`, and its `recv` method produces a future we need to await rather than producing the value directly.

The example produces the same output as everything happens in sequence.

The example bellow adds more messages and sleep between them:
```Rust
// -- snip --
	let (tx, mut rx) = trpl::channel();

	let vals = vec![
		String::from("hi"),
		String::from("from"),
		String::from("the"),
		String::from("future"),
	]

	for val in vals {
		tx.send(val).unwrap();
		trpl::sleep(Duration::from_milis(500)).await;
	}

	while let Some(value) = rx.recv().await {
		println!("received '{value}'");
	}
// -- snip --
```

The code sends and receives all the messages. Unfortunately, the messages do not arrive at half-seconds intervals. They arrive all at once 2 seconds after the program starts. Also, this program never exits, it waits forever for new messages.

To get the behavior we want, where the sleep delay happens between each message, we need to put the `tx` and `rx` operations in their own async blocks.

Then the runtime can execute each of them separately using `trpl::join`, just as in the counting example.

Once again, we await the result of calling `trpl::join`, not the individual futures.

If we awaited the individual futures in sequence, we would just end up back in a sequential flow—exactly what we’re trying _not_ to do.
```Rust
// -- snip --
	// moves tx to async block.
	// tx will be closed when async block end is reached which will stop the while loop becase a None value will be sent.
    let tx_fut = async move {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("future"),
        ];
        for val in vals {
            tx.send(val).unwrap();
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };
    let rx_fut = async {
        while let Some(value) = rx.recv().await {
            println!("received '{value}'");
        }
    };
    trpl::join(tx_fut, rx_fut).await;
// -- snip --
```

With this code, the messages get printed at 500 ms intervals, rather than all in a rush after 2 seconds.

Since `tx` is dropped when the `async move` block reaches to the end, the `while` loop also doesn't run forever in this example because when the `tx` is dropped, an `None` value is sent, which stops the loop.

This `async` channel is also a multiple-producer channel, so we can call `clone` on `tx` if we want to send messages from multiple futures.
```Rust
// -- snip --
    let (tx, mut rx) = trpl::channel();
    let tx1 = tx.clone();
    let tx1_fut = async move {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("future"),
        ];
        for val in vals {
            tx1.send(val).unwrap();
            trpl::sleep(Duration::from_millis(500)).await;
        }
    };
    let rx_fut = async {
        while let Some(value) = rx.recv().await {
            println!("received '{value}'");
        }
    };
    let tx_fut = async move {
        let vals = vec![
            String::from("more"),
            String::from("messages"),
            String::from("for"),
            String::from("you"),
        ];
        for val in vals {
            tx.send(val).unwrap();
            trpl::sleep(Duration::from_millis(1500)).await;
        }
    };
	// Switch from trpl::join to trpl::join3 to handle additional future.
	// also note, the important is not the order in which futures are created but rather the order they're awaited.
    trpl::join3(tx1_fut, tx_fut, rx_fut).await;
// -- snip --
```