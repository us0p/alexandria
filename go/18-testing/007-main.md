# Main
It is sometimes necessary for a test or benchmark program to do extra setup
or teardown before or after it executes. It is also sometimes necessary to
control which code runs on the main thread. To support these and other 
cases, if a test file contains a function:  

```go
func TestMain(m *testing.M)
```

then the generated test will call TestMain(m) instead of running the tests
or benchmarks directly. `TestMain` runs in the main goroutine and can do 
whatever setup and teardown is necessary around a call to `m.Run`. `m.Run`
will return an exit code that may be passed to `os.Exit`. If `TestMain` 
returns, the test wrapper will pass the result of `m.Run` to `os.Exit` 
itself.  
When `TestMain` is called, `flag.Parse` has not been run. If `TestMain` 
depends on command-line flags, including those of the testing package, it 
should call `flag.Parse` explicitly. Command line flags are always parsed 
by the time test or benchmark functions run.  
`TestMain` is a low-level primitive and should not be necessary for casual 
testing needs, where ordinary test functions suffice.  
