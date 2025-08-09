# TL;DR
When thinking about which method to use when, consider these rules of thumb:

- If the work is _very parallelizable_, such as processing a bunch of data where each part can be processed separately, threads are a better choice.
- If the work is _very concurrent_, such as handling messages from a bunch of different sources that may come in at different intervals or different rates, async is a better choice.

And if you need both parallelism and concurrency, you don’t have to choose between threads and async. You can use them together freely, letting each one play the part it’s best at.

# Futures tasks and threads
[Threads](using_threads.md) provide one approach to concurrency.

Using [async with futures and streams](futures_and_async_syntax.md) provides another.

When choosing between the two you must consider the use case. But, it's quite common to have to use both.

Many operating systems have supplied threading-based concurrency models for decades now, and many programming languages support them as a result. However, these models are not without their tradeoffs. On many operating systems, they use a fair bit of memory for each thread, and they come with some overhead for starting up and shutting down. Threads are also only an option when your operating system and hardware support them. Unlike mainstream desktop and mobile computers, some embedded systems don’t have an OS at all, so they also don’t have threads.

The async model provides a different—and ultimately complementary—set of tradeoffs. In the async model, concurrent operations don’t require their own threads. Instead, they can run on tasks, as when we used `trpl::spawn_task` to kick off work from a synchronous function in the streams section. A task is similar to a thread, but instead of being managed by the operating system, it’s managed by library-level code: the runtime.

In the [previous section](streams_futures_in_sequence.md#Merging%20Stream), we saw that we could build a stream by using an async channel and spawning an async task we could call from synchronous code. We can do the exact same thing with a thread.
```Rust
fn get_intervals() -> impl Stream<Item = u32> {
    let (tx, rx) = trpl::channel();

    // This is *not* `trpl::spawn` but `std::thread::spawn`!
    thread::spawn(move || {
        let mut count = 0;
        loop {
            // Likewise, this is *not* `trpl::sleep` but `std::thread::sleep`!
            thread::sleep(Duration::from_millis(1));
            count += 1;

            if let Err(send_error) = tx.send(count) {
                eprintln!("Could not send interval {count}: {send_error}");
                break;
            };
        }
    });

    ReceiverStream::new(rx)
}
```

The code above produces the same output, with little to no change at all.

Despite their similarities, these two approaches behave very differently.

We could spawn millions of async tasks on any modern personal computer.

If we tried to do that with threads, we would literally run out of memory!

However, there’s a reason these APIs are so similar.

Threads act as a boundary for sets of synchronous operations; concurrency is possible _between_ threads.

Tasks act as a boundary for sets of _asynchronous_ operations; concurrency is possible both _between_ and _within_ tasks, because a task can switch between futures in its body.

Finally, futures are Rust’s most granular unit of concurrency, and each future may represent a tree of other futures.

The runtime—specifically, its executor—manages tasks, and tasks manage futures.

In that regard, tasks are similar to lightweight, runtime-managed threads with added capabilities that come from being managed by a runtime instead of by the operating system.

This doesn’t mean that async tasks are always better than threads.

Concurrency with threads is in some ways a simpler programming model than concurrency with `async`.

Threads are somewhat “fire and forget”; they have no native equivalent to a future, so they simply run to completion without being interrupted except by the operating system itself.

That is, they have no built-in support for _intratask concurrency_ the way futures do.

Threads in Rust also have no mechanisms for cancellation.

Tasks, then, give us _additional_ control over futures, allowing us to choose where and how to group them.

And it turns out that threads and tasks often work very well together, because tasks can (at least in some runtimes) be moved around between threads.

Many runtimes use an approach called _work stealing_ to transparently move tasks around between threads, based on how the threads are currently being utilized, to improve the system’s overall performance.

That approach actually requires threads _and_ tasks, and therefore futures.
