`HashMap<K, V>` stores a mapping of keys of type `K` to values of type `V`.
Just like vectors, hash maps store their data on the heap.
Like vectors, hash maps are homogeneous, all of the keys must have the same type, and all of the values must have the same type.
```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
scores.insert(String::from("Blue"), 20); // updates "Blue" key value.

// .entry() takes the key you want to check as a parameter.
// The return value of the method is an enum 'Entry'. It represents a value that might or might not exist.
// or_insert() returns a mutable reference to the value for the corresponding Entry. If the key doesn't exist, it inserts the parameter as the new value and returns a reference to the new value.
scores.entry(String::from("Black")).or_insert(99);

// Updating a value based on the old value
let text = "hello world wonderful world?";
let mut map = HashMap::new();

// .split_whitespace() returns an interator over subslices, separated by whitespace.
for word in text.split_whitespace() {
	let count = map.entry(word).or_insert(0);
	*count += 1;
}

let team_name = String::from("Blue");

// The get method returns an Option<&V>.
// copied() is used to get an Option<i32> rather tahn an Option<&i32>.
// unwrap_or() returns 0 if option returns None.
let score = scores.get(&team_name).copied().unwrap_or(0);

// Iteraing over each key-value pair:
for (key, value) in &scores {
	println!("{key}: {value}");
}
```