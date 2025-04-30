strings are implemented as a collection of bytes, plus some methods to provide useful functionality when those bytes are interpreted as text.
## What is a String?
Rust has only one string type in the core language, which is the string slice `str` that is usually seen in its borrowed form `&str`.

The `String` type, is a growable, mutable, owned, `UTF-8` encoded string type.

When Rustaceans refer to "strings" in Rust, they might be referring to either the `String` or the string slice `&str` types, not just one of those. Both `Strin` and string slices are `UTF-8` encoded.
## Creating a new String
Many of the same operations available with `Vect<T>` are available with `String` because it's actually implemented as a wrapper around a vector of bytes with some extra guarantees, restrictions, and capabilities.