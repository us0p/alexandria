package main

import "math"

//func Perimeter(width float64, height float64) float64 {
//	return 2 * (width + height)
//}
//
//func Area(width float64, height float64) float64 {
//	return width * height
//}

func Perimeter(rectangle Rectangle) float64 {
	return 2 * (rectangle.Width + rectangle.Height)
}

//func Area(rectangle Rectangle) float64 {
//	return rectangle.Width * rectangle.Height
//}

// Struct:
// A struct is just a named collection of fields where you can store data.
type Rectangle struct {
	Width  float64
	Height float64
}

// Methods:
// A method is a function with a receiver. A method declaration binds an
// identifier, the method name, to a method, and associates the method
// with the receiver's base type.
// Methods are called by invoking them on an instance of a particular type.

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

// Syntax: func (receiverName ReceiverType) MethodName(args)
// It is a convention in Go to have the receiver variable be the first letter of the type.
// When your method is called on a variable of that type, you get your reference to its data
// via the receiverName variable. In other languages this is done implicity and you access the receiver via this.

type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

type Triangle struct {
    Base float64
    Height float64
}

func (t Triangle) Area() float64 {
    return (t.Base * t.Height) * 0.5
}

// Interfaces:
// Collections of methods sgnatures.
// In Go interface resolution is implicit. If the type you pass in matches all the methods that the interface
// is asking for, it will compile.
// When a type implements an interface, it can then be used as the interface type.
// Then Circle, Triangle and Rectangle can be considered a Shape
// The empty interface, interface{}, is always implemented by every type because it has no requirements.

type Shape interface {
	Area() float64
}

// Note that:
// Rectangle has a method called Area that returns a float64 so it satisfies the Shape interface.
// Circle has a method called Area that returns a float64 so it satisfies the Shape Interfaces.
// string does not have such a method, so it doesn't satisfy the interface.

// We can name our interface arguments to make more clear what we expect in each method.
type Copier interface {
    Copy(sourceFile, destinationFile string) (bytesCopied int)
}

// Tips:
// Keep interfaces small -> Interfaces are meant to define the minimal behavior necessary to accurately represent an idea or concept.
// They shouldn’t be aware of any types that happen to satisfy the interface at design time. Instead, you should use type assertion to 
// derive the underlying type when given an instance of the car interface.

// Interfaces on pointers don't extend the implementation to the underlying type:
type InterfacePointer interface {
    width() int
    height() int
}

type square struct {
    lenght int
}

func (s *square) width() int {
    return s.lenght
}

func (s *square) height() int {
    return s.lenght
}

func GetArea(form InterfacePointer) int {
    return form.width() * form.height()
}

// var a = square{1}
// GetArea(a)
// Note that trying to use a in this GetArea call can't be done because the underlying type square doesn't implement the methods, only the *square type.
// Trying to make this call would yeld:
// cannot use a (variable of type square) as InterfacePointer value in argument to GetArea: square doesn't implement InterfacePointer (method height has pointer receiver).

// Here's ok, b is a *square, so it implements the InterfacePointer interface.
// var b = &square{1}
// GetArea(b)
