A **crate** is the smallest amount of code that the Rust compiler considers at a time. Even if you run `rustc` rather than `cargo` and pass a single source code file, the compiler considers that file to be a crate.

Crates can contain modules, and the modules may be defined in other files that get compiled with the crate.

A crate can come in one of two forms:
- Binary
- Library.

Binary crates are programs you can compile to an executable that you can run, such as a command-line program or a server. Each must have a function called `main` that defines what happens when the executable runs.

Library crates don't have a `main` function. and they don't compile to an executable. Instead, they define functionality intended to be shared with multiple projects.

The **crate root** is a source file that the Rust compiler starts from and makes up the root module of your crate.

A **package** is a bundle of one or more crates that provides a set of functionality. A package contains a `Cargo.toml` file that describes how to build those crates.

Cargo is actually a package that contains the binary crate for the command-line tools you've been using to build your code.

Cargo follows a convention that `src/main.rs` is the **crate root** of a binary crate with the same name as the package.

Likewise, Cargo knows that if the package directory contains `src/lib.rs`, the package contains a library crate with the same name as the package.

Cargo passes the crate root files to `rustc` to build the library or binary.

If a package contains `src/main.rs` and `src/lib.rs`, it has two crates, both with the same name as the package. A package can have multiple binary crates by placing files in the `src/bin` directory: each file will be a separate binary crate.

`src/main.rs` and `src/lib.rs` are called crate roots. The reason for their name is that the contents of either of these two files form a module named `crate` at the root of the crate's module structure, known as the `module tree`.