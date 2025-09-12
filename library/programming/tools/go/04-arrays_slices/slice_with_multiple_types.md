## Using `interface{}`
If you actually need your slice to have heterogenous data:
```go
items := []interface{}{"hello", 42, 3.14, true}
```

Sacrifices type safety, you need to do type assertions.
## Define a common interface
If the types have some shared behavior, define an interface they all implement:

This approach is type safe and polymorphic but needs previous setup and might result in unnecessary abstractions only for the sake of polymorphism.
```go
type Describable interface {
	Describe() string
}

type Person struct{ Name string }
func (p Person) Describe() string { return "Person: " + p.Name }

type Car struct{ Model string }
func (c Car) Describe() string { return "Car: " + c.Model }

func main() {
	items := []Describable{
		Person{"Alice"},
		Car{"Tesla"},
	}

	for _, item := range items {
		fmt.Println(item.Describe())
	}
}
```
## Use Generics
If you don't need to actually support different types into the slice at the same type but rather an slice that might store different types you should use [Generics](go_generics.md)