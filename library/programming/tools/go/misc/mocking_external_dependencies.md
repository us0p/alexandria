# Mocking External Dependencies
When you're creating code that interacts with libraries and frameworks, you need a reliable way to mock those dependencies so your code is easy to test.

Dependency Injection should be your ally here.
```go
// Built around external dependency used interface.
type ExternalDependency interface {
	Method1()
	Method2()
}

// In your function you reference your narrower interface rather the original external dependency.
func HasExternalDependency(ed ExternalDependency) {
	// original logic here
}
```
The injected dependency is your own narrower interface.

In your tests you can create a [Spy](004-test_doubles.md#Spies) that follows your injected dependency interface. The  (`ExternalDependency`) is going to record calls and state of the object which you can assert later in your tests.
## Issues with concrete type returns
Most of library code is going to return its own concrete types.

In Go, return types must match exactly, so, in your interface you have two options to abstract this dependency away:
### Interface returns concrete type
```go
import "github.com/go-rod/rod"

// Mimics go-rod *rod.Browser interface
type Browser interface {
	// Returns concrete type
	ControlURL(string) *rod.Browser
	...
}

// sample implementation of ControlURL:
func (f *FakeBrowser) ControlURL(s string) *rod.Browser {
	// Return dummy struct
	return &rod.Browser{}
}
```
- Use it when you're coupled to a specific library/framework. Acceptable only in the infrastructure layer.
- When you don't want flexibility, or whether you're not expecting to change the library/framework.

Pros:
- Simple and idiomatic

Cons:
- Highly coupled code

>If you find yourself, needing to mock many methods of the external dependency, fighting chaining APIs or returning lots of dummy concrete types. Switch to Adapter/Wrapper approach.
### Use an Adapter/Wrapper
```go
import "github.com/go-rod/rod"

// Interface is fully abstract
type Browser interface {
	ControlURL(string) Browser
}

// Adapter
type rodBrowser struct {
	b *rod.Browser
}

// Adapts library method to follow expected interface
func (r *rodBrowser) ControlURL(url string) Browser {
	r.b = r.b.ControlURL(url)
	return r
}

// Factory
func newBrowser() Browser {
	return &rodBrowser{b: rod.New()}
}
```
This approach keeps the external dependency fully abstracted away, but it requires an adapter to be created for every method utilized, maybe creating several adapters for many different types in the library/framework.

Pros:
- It's easy to mock
- Keep contracts clean
Cons:
- Adds complexity
- Needs more boilerplate code