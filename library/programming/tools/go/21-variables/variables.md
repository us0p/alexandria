```go
// Multiple variables in one 'var' statement
var a, b, c int

// Multiple initializated variables with different types
var a, b = 10, "hello"

// Grouped variable declaration block
var (
	x  int
	y  string
	z  float64
)

// It's not possible to declared grouped var blocks with a singles shared type
var (
	a, b, c int // ERROR!
)

// Or with initialization
var (
	x = 10
	y = "test"
	z = true
)
```