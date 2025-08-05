## Creating a new Thread
```Rust
use std::thread;
use std::time::Duration;

fn main() {
	// Creates a new thread.
	// The closure is the function that this thread is going to execute.
	thread::spawn(|| {
		for i in 1..10 {
			println!("hi number {i} from the spawned thread!");
			// Forces the THREAD to stop its execution. Allowing other threads to run.
			thread::sleep(Duration::from_milis(1));
		}
	});

	for i in 1..5 {
		println!("hi number {i} from the main thread!");
		thread::sleep(Duration::from_milis(1));
	}
}
```

>When the main thread completes, all spawned threads are shut down.
## Waiting for all Threads to finish
```Rust
use std::thread;
use std::time::Duration;

fn main() {
	// handle is a JoinHandle<T>
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

	// Waits for its thread to finish.
    handle.join().unwrap();
}
```

Calling `JoinHandle::join()` blocks the thread currently running until the thread represented by the handle terminates.

Blocking a thread means that thread is **prevented from performing work or exiting**.

Since the join is after the main thread loop the threads still alternate but the main thread will the other to finish.

If we move the join on top of main thread's loop, the threads will not alternate anymore as the main thread will first wait the spawned thread to finish after continue its work.
## Using move closures with Threads
When we use the `move` keyword with closures passed to `thread::spawn` the function takes ownership of the values it uses from the environment effectively transferring the ownership from one thread to another.

If we try to move a borrowed value to a thread without moving it, the compiler won't know for how long the value will be valid inside the thread.
We could drop the value while the thread is still running and thus the reference would be invalid.
To avoid this, we move the references to the thread itself.
```Rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

	// because of move, v is no longer available in this context.
    let handle = thread::spawn(move || {
        println!("Here's a vector: {v:?}");
    });

    handle.join().unwrap();
}
```