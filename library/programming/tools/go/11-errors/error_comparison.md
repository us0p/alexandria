# Direct comparison
Only works for the same error value.
```go
var ErrNotFound = errors.New("not found")

func check() error {
    return ErrNotFound
}

err := check()
if err == ErrNotFound { // works, same value
    fmt.Println("matched")
}

if err == fmt.Errorf("not found") { // doesn't work, same text but different addresses as error is an interface
    fmt.Println("matched")
}
```
## Comparing error messages
You can check the underlying messages for equality but this is not idiomatic as it's fragile and wrapping the error breaks the check.
```go
err = fmt.Errorf("not found")
// If err is nil would cause a nil dereference error.
if err != nil && err.Error() == fmt."not found" { // matches, checking underlying value
    fmt.Println("matched")
}
```
## Using `error.Is`
```go
// Using predefined errors allows for more type safety
// Errors usually go in a separate application package to be reutilized
var ErrNotFound = errors.New("not found")

func check() error {
	// %w wraps the error, this allow us to add more info to predefined errors
    return fmt.Errorf("db error: %w", ErrNotFound)
}

err := check()

if errors.Is(err, ErrNotFound) { // works even if wrapped
    fmt.Println("matched")
}
```