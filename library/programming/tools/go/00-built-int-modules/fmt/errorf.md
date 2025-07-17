# `fmt.Errorf`
Formats according to a format specifier and returns the string as a value 
that satisfies error.
```golang
import "fmt"

func main() {
    name, id := "bueller, 17
    err := fmt.Errorf("user %q (id %d) not found", name, id)

    // user "bueller" (id 17) not found
}
```


