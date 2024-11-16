# Testing
Privdes support for automated testing of Go packages.
It's intended to be used in concert with the `go test` command, which 
automates execution of any function of the form:
  
```go
func TestXxx(*testing.T)
```
  
Where `Xxx` does not start with a lowercase letter. The function names 
serves to identify the test routine.  
Within these functions, use the Error, Fail or related methods to signal 
failure.  
Test files must have a name ending `_test.go`. The file will be excluded 
from regular package builds but will be included when the `go test` command
is run.  
The test file can be in the same package as the one being tested, or in a 
corresponding package with the suffix `_test`.  
If the file is in a separate `_test` package, the package being test must 
be imported explicily and only its exported identifiers may be used. This 
is known as `black box` testing.  
