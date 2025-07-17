# `fmt.Sprint`
Formats using the default formats for its operands and returns the 
resulting *string*.  
Spaces are added between operands when neither is a string.  
```golang
import "fmt"

func main() {
    name, age := "Kim", 22
    s := fmt.Sprint(name, " is ", age, " years old.\n")

    // Kim is 22 years old.
}
```
# `fmt.Sprintln`
Formats using the default formats for its operands and returns the 
resulting string. Spaces are always added between operands and a newline is
appended.
```golang
import "fmt"

func main() {
    name, age := "Kim", 22
    s := fmt.Sprintln(name, " is ", age, " years old.")

    // Kim is 22 years old.
}
```
# `fmt.Sprintf`
Formats according to a format specifier and returns the resulting string.
```golang
import "fmt"

func main() {
    name, age := "Kim", 22
    s := fmt.Sprintf("%s is %d years old.\n", name, age)

    // Kim is 22 years old.
}
```
