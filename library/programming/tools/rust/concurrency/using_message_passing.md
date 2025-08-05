To accomplish message-sending concurrency. Rust provides an implementation of channels.

A channel is a general programming concept by which data is sent from one thread to another.

A channel has two halves:
- **Transmitter**: Puts message in the channel. There can be many transmitters.
- **Receiver**: Receives the messages in the other side. There can be only a single receiver.

Your code calls methods on the transmitter with the data you want to send, and another part checks the receiving end for arriving messages.

A channel is said to be closed if either the transmitter or the receiver half is dropped.
```Rust
// Multiple Producer Single Consumer (MPSC)
use std::sync::mpsc;
use std::thread;

fn main() {
	let (
		tx, // transmitter end
		rx // receiver end
	) = mpsc::channel();

	thread::spawn(move || {
		let val = String::from("hi");
		// the thread needs to own tx to be able to send messages.
		// Also, sending values in a channel moves the value to the other thread.
		// Trying to access val after this call would be an error.
		tx.send(val).unwrap();
	})

	// receive values from the channel.
	// blocks the thread execution until a value is received.
	// For no-blocking operation see try_recv.
	let received = rx.recv().unwrap();
	println!("Got: {received}");
}
```
## Sending and receiving multiple values
```Rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

	// Iterates on receiver blocking at each iteration.
    for received in rx {
        println!("Got: {received}");
    }
}
```
## Creating multiple producers
```Rust
    // --snip--
    let (tx, rx) = mpsc::channel();

	// gives a new transmitter
    let tx1 = tx.clone();

	// thread 1
    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

	// thread 2
    thread::spawn(move || {
        let vals = vec![
            String::from("more"),
            String::from("messages"),
            String::from("for"),
            String::from("you"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

	// waiting on both threadsd
    for received in rx {
        println!("Got: {received}");
    }

    // --snip--
```