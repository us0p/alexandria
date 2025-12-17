# Boundary Testing
In Boundary Testing you treat external dependencies as trusted and avoid mocking them.

This sets up a clear boundary:
- External Application logic.
- Your application logic.

With this you can unit test all the logic or supporting code you perform for the dependency code and perform integration tests across the boundary.

For this to work you need to extract away the unit-testable logic.
```go
```

In the example your boundary is `d.Method()` and your testable logic is `fmt.Sprintf(...)`. You can extract your unit logic and test is separately:
```go
// can be easily unit tested.
func generateDParam() string {
	return fmt.Sprintf(...)
}

// If required can be tested in integration tests.
func PerformActionWithDependency(d Dependency, d_param string) {
	d.Method(d_param, d_param)
	
	//...
}
```

The same logic can be used to extract decisions and intent (control flow statements).
## When to use it
Use it when the dependency is hard to mock or you don't want to be creating a lot of adapters and wrappers.