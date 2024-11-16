# Subtests and Sub-benchmarks
The Run methods of `T` and `B` allow defining subtests and sub-benchmarks,
without having to define separate functions for each. This enables uses 
like table-driven benchmarks and creating hierarchical tests. It also 
provides a way to share common setup and tear-down code:  

```go
func TestFoo(t *testing.T) {
    // <setup code>
    t.Run("A=1", func(t *testing.T) { ... })
    t.Run("A=2", func(t *testing.T) { ... })
    t.Run("B=1", func(t *testing.T) { ... })
    // <tear-down code>
}
```

Each subtest has a unique name in which the combination of the name of the
top-level test and the sequence of names passed to `Run`, separated by 
slashes, with an optional trailing sequence number.  
The argument to the `-run`, `-bench`, and `-fuzz` command-line flags is an
unanchored regular expression that matches the test's name. For tests 
with multiple slash-separated elements, such as subtests, the argument is 
itself slash-separated, with expressions matching each name element in 
turn. Because it is unanchored, an empty expression matches any string.  

```bash
go test -run ''        # Run all tests.
go test -run Foo       # Run top-level tests matching "Foo", such as "TestFooBar".
go test -run Foo/A=    # For top-level tests matching "Foo", run subtests matching "A=".
go test -run /A=1      # For all top-level tests, run subtests matching "A=1".
go test -fuzz FuzzFoo  # Fuzz the target matching "FuzzFoo"
```

Subtests can also be used to control parallelism. A parent test will only 
complete once all of its subtests complete. In this example, all tests are
run in parallel with each other, and only with each other, regardless of 
other top-level tests that may be defined.  
