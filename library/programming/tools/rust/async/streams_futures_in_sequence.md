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