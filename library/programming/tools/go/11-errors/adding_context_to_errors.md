# Adding Context to Errors
When you create a sentinel error with:
```go
import "errors"

var ErrSomething = errors.New("error")
```

This makes errors easy to be compared but also makes them lose a lot of context.

You can wrap errors using `fmt.Errorf` to add more context and information while still allowing them to be easily compared:
```go
import (
	"fmt"
	"errors"
)

var ErrSomething = errors.New("error")

func ErrorFunc(input string) error {
	return fmt.Errorf(
		"%w: Some error happenend for input %s",
		ErrSomething,
		input,
	)
}
```

Now when you receive the error an error from `ErrorFunc()` the error will still be comparable to `ErrSomething` but it'll also include some context like which input produced the error.

>Even if you wrap your error many times, the client code can still check errors correctly with `errors.Is()`.