# Examples
The package also runs and verifies example code.  
Example functions may include a concluding line comment that begins with
`Output:` and is compared with the standard output of the function when the
test run.  

```go
func ExampleHello() {
    fmt.Println("hello")
    // Output: hello
}
```

The comment prefix `Unordered output:` is like `Output:`, but matches any 
line order.  

```go
func ExamplePerm() {
    for _, value := range Perm(5) {
        fmt.Println(value)
    }
    // Unordered output: 4
    // 2
    // 1
    // 3
    // 0
}
```

Example functions without output comments are compiled but not executed.  
The naming convention to declare examples for the package, a function F a 
type T and method M on type T are:  

```go
func Example() {...}
func ExampleF() {...}
func ExampleT() {...}
func ExampleT_M() {...}
```

Multiple example functions for a package/type/function/method may be 
provided by appending a distinct suffix to the name. The suffix must start 
with a lower-case letter.  

```go
func Example_suffix() {...}
func ExampleF_suffix() {...}
func ExampleT_suffix() {...}
func ExampleT_M_suffix() {...}
```

The entire test file is presented as the example when it contains a single
example function, at least one other function, type, variable, or constant
declaration, and no test or benchmark functions.  
