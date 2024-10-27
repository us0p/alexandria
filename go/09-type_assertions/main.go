package main

import (
    "log"
    "fmt"
)

type shape interface {
    area() float64
}

type circle struct {
    radius float64
}

func (c circle) area() float64 {
    return c.radius
}

type rectangle struct {
    width float64
    height float64
}

func (r rectangle) area() float64 {
    return r.width * r.height
}

func main() {
    // s is an instance of shape
    var s shape

    // PAY ATTENTION: Go is a statically typed language, so here we aren't changing s type 
    // as circle implements shape, s still's a shape instance.
    s = circle{radius: 4.5}

    
    // A type assertion provides access to an interface value's underlying concrete value.
    // This statement asserts that the interface value s holds the concrete type circle and assigns the underlying circle value to the variable c. 
    
    // c := s.(circle) -> if s concrete type isn't a circle, this will trigger a panic!

    c, ok := s.(circle) // With the comma OK we can test if the concrete type of s is circle without panicking?

    if !ok {
        log.Fatal("s is not a circle")
    }

    fmt.Printf("c.radius: %.2f\n", c.radius)

    // You can do several type assertions with a switch statement liike this:
    switch v := s.(type) {
        case circle:
            fmt.Printf("%T\n", v)
        case rectangle:
            fmt.Printf("%T\n", v)
        default:
            fmt.Printf("%T\n", v)
    }
}
