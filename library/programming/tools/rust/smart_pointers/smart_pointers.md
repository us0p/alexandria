Data structures that act like a pointer but also have additional metadata and capabilities.

While references only borrow data, in many cases smart pointers own the data they point to.

`String` and `Vec<T>` are types that count as smart pointers because they own some memory and allow you to manipulate it. They also have metadata and extra capabilities or guarantees, for example, stores its capacity as metadata and has the extra ability to ensure its data will always be valid `UTF-8`.

Smart pointers are usually implemented using structs which must implement the `Deref` and `Drop` traits.

The `Deref` trait allows an instance of the smart pointer struct to behave like a reference so you can write your code to work with either references or smart pointer.

Most common smart pointers in the standard library are:
- `Box<T>` for allocating values on the heap.
- `Rc<T>` a reference counting type that enables multiple ownership
- `Ref<T>` and `RefMut<T>` accessed through `RefCell<T>` a type that enforces the borrowing rules at runtime instead of compile time.