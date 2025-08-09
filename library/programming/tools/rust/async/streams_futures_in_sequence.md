Remember how we used `trpl::recv` to communicate between futures in [Applying concurrency with async](applying_concurrency_with_async.md#Counting%20up%20on%20two%20tasks%20using%20message%20passing)

There are two differences between iterators and the async channel receiver.

The first difference is time: iterators are synchronous, while the channel receiver is asynchronous.

The second is the API. When working directly with `Iterator`, we call its synchronous `next` method.

With the `trpl::Receiver` stream in particular, we called an asynchronous `recv` method instead.

Otherwise, these APIs feel very similar, and that similarity isn’t a coincidence.

A stream is like an asynchronous form of iteration.

Whereas the `trpl::Receiver` specifically waits to receive messages, though, the general-purpose stream API is much broader: it provides the next item the way `Iterator` does, but asynchronously.

The similarity between iterators and streams in Rust means we can actually create a stream from any iterator.

As with an iterator, we can work with a stream by calling its `next` method and then awaiting the output.
```Rust
// -- snip --
    let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let iter = values.iter().map(|n| n * 2);
    let mut stream = trpl::stream_from_iter(iter);
    while let Some(value) = stream.next().await {
        println!("The value was: {value}");
    }
// -- snip --
```

The code, doesn't compile. It reports that there's no `next` method available.

We need the right trait in scope to be able to use the `next` method.

Given our discussion so far, you might reasonably expect that trait to be `Stream`, but it’s actually `StreamExt`. Short for _extension_, `Ext` is a common pattern in the Rust community for extending one trait with another.

The `Stream` trait defines a low-level interface that effectively combines the `Iterator` and `Future` traits.

`StreamExt` supplies a higher-level set of APIs on top of `Stream`, including the `next` method as well as other utility methods similar to those provided by the `Iterator` trait.

The fix to the compiler error is to add a `use` statement for `trpl::StreamExt`.

```Rust
use trpl::StreamExt;

fn main() {
    trpl::run(async {
        let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        let iter = values.iter().map(|n| n * 2);
        let mut stream = trpl::stream_from_iter(iter);

        while let Some(value) = stream.next().await {
            println!("The value was: {value}");
        }
    });
}
```

Now that we have `StreamExt` in scope, we can use all of its utility methods, just as with iterators.

For example, we use the `filter` method to filter out everything but multiples of three and five.
```Rust
use trpl::StreamExt;

fn main() {
    trpl::run(async {
        let values = 1..101;
        let iter = values.map(|n| n * 2);
        let stream = trpl::stream_from_iter(iter);

		// applying filtering here
        let mut filtered = stream.
	        filter(|value| value % 3 == 0 || value % 5 == 0);

        while let Some(value) = filtered.next().await {
            println!("The value was: {value}");
        }
    });
}
```
## Composing streams
```Rust
use str::{pin::pin, time::Duration};
use trpl::{ReceiverStream, Stream, StreamExt};

fn main() {
	trpl::run(async {
		// Using pin! because timeout helper produces a stream that need to be pinned to be polled
		let mut messages = pin!(
			get_messages()
				// from StreamExt
				// is applied to each element of the stream, separately
				// it doesn't prevent messages from arriving in the end.
				// we still get all of our messages 
				// this happens because returned channel is unbounded.
				// it can hold as many messages it can fit in memory.
				// if the message doesn't arrive before timeout, we'll error it out
				// but when it polls the stream again, the message MAY have arrived
				.timeout(Duration::from_millis(200))
		);

		while let Some(message) = messages.next().await {
			match result {
				// Indicates a message arrived in time
				Ok(message) => println!("{message}"),
				// Timeout elapsed before any message arrived
				Err(reason) => eprintln!("Problem: {reason:?}"),
			}
		}
	})
}

fn get_messages() -> impl Stream<Item = String> {
	let (tx, rx) = trpl::channel();

	// create separate task to sleep between messages without blocking.
	trpl::spawn_task(async move {
		let messages = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
		for (index, message) in message.into_iter().enumerate() {
			// apply delay to simulate real world.
			// With timeout of 200, this should affect half of the messages.
			let time_to_sleep = if index % 2 == 0 { 100 } else { 300 };
			trpl::sleep(Duration::from_millis(time_to_sleep)).await;
			
			tx.send(format!("Message: '{message}'")).unwrap();
		}
	});
	
	// Converts the rx receiver from trpl::channel into a Stream with a next() method.
	ReceiverStream::new(rx)
}
```

We can't make `get_messages` into an async function, because then we'd return a `Future<Output = Stream<Item = String>>` instead of a `Stream<Item = String>>`.

The caller would have to await `get_messages` to get access to the stream which would require it to send all the messages, including the sleep delay between each message, before returning to the stream.

>`spawn_task` in this way works because we already set up our runtime; had we not, it would cause a panic. Other implementations choose different tradeoffs. Make sure you know what tradeoff your runtime has chosen.
## Merging Stream
```Rust
fn get_intervals() -> impl Stream<Item = u32> {
	let (tx, rx) = trpl::channel();

	trpl::spawn_task(async move {
		let mut count = 0;
		loop {
			trpl::sleep(Duration::from_millis(1)).await;
			count += 1;
			tx.send(count).unwrap();
		}
	});

	ReceiverStream::new(rx)
}
```

Because this is all wrapped in the task created by `spawn_task`, all of it, including the infinite loop, will get cleaned up along with the runtime.

This kind of infinite loop, which ends only when the whole runtime gets torn down, is fairly common in async Rust, many programs need to keep running indefinitely. With async, this doesn't block anything else, as long as there is at least one await point in each iteration through the loop.

We can attempt to merge the `messages` and `intervals` streams:
```Rust
fn main() {
	// -- snip

	let messages = get_messages().timeout(Duration::from_millis(200));;
	let intervals = get_intervals()
		.map(|count| format!("Interval: {count}"))
		// Add throttling so it doesn't overwhelm messages stream.
		.throttle(Duration::from_millis(100))
		// need to match timeout from from messages.
		// this stream doesn't need a timeout so we can just create a timeout that is longer than the others.
		.timeout(Duration::from_secs(10));
	// Combines multiple streams into one stream that produces items from any of the source stream as soon as the items are available.
	// It doesn't impose any ordering.
	let merged = messages.merge(intervals)
		// Limit the number of items we will accept from a stream. stops the streams after that.
		// applied to the merged stream because we want to limit the final output, not just one stream or the other.
		.take(20);	
	// need to make it mutable so we can call next() on it.
	// also need to pin to be safe to do so.
	let mut stream = pin!(merged);
	// -- snip
}
```

To merge these two streams, we need to transform one of them to match the other.

We reworked the intervals stream, because messages is already in the basic format we want and has to handle timeout errors.

Note that neither `messages` nor `intervals` need to be pinned or mutable, because both will be combined into the single `merged` stream.

The `throttle` call produces a new stream that wraps the original stream so that the original streams gets polled **only** at the throttle rate, not its own "native" rate.

A stream only do something when we await on it ([futures are lazy](futures_and_async_syntax.md)).

This means that the original stream will only produce new values at the throttle rate, because we wait on it based on the throttle rate.

It doesn't keep running in the background while we take a peek on the values every now an then.

Final snippet shows how we can handle errors effectively by breaking out the loop in case one of the streams is closed.
```Rust
fn get_messages() -> impl Stream<Item = String> {
    let (tx, rx) = trpl::channel();

    trpl::spawn_task(async move {
        let messages = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];

        for (index, message) in messages.into_iter().enumerate() {
            let time_to_sleep = if index % 2 == 0 { 100 } else { 300 };
            trpl::sleep(Duration::from_millis(time_to_sleep)).await;

			// Added proper error handling
            if let Err(send_error) = tx.send(format!("Message: '{message}'")) {
                eprintln!("Cannot send message '{message}': {send_error}");
                break;
            }
        }
    });

    ReceiverStream::new(rx)
}

fn get_intervals() -> impl Stream<Item = u32> {
    let (tx, rx) = trpl::channel();

    trpl::spawn_task(async move {
        let mut count = 0;
        loop {
            trpl::sleep(Duration::from_millis(1)).await;
            count += 1;

			// Added proper error handling
            if let Err(send_error) = tx.send(count) {
                eprintln!("Could not send interval {count}: {send_error}");
                break;
            };
        }
    });

    ReceiverStream::new(rx)
}
```