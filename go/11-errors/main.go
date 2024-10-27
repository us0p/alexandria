package main

import "fmt"

// An Error is any type that implements the built-in error interface:
//type error interface{
//    Error() string
//}

// If you want to include more information than just the error message string you can create your own custom types that implement the error interface.
// By convention, custom error type names should end with Errr.
type userError struct {
    name string
}

// Note that you should implement the method with a pointer receiver.
// That's because error is an interface, which means that they are comparable by comparing the values that they wrap, which means that you get different
// comparison result based on what they're wrapping.
// When you implement the Error interface with a pointer, this means that two erros will only be equal if they reference to the same adress.
// This is intentional to guarantee that custom programs don't implment overlaping errors. 
func (u *userError) Error() string {
    return fmt.Sprintf("%s had an error", u.name)
}

type anotherUserError struct {
    name string
}

func (au anotherUserError) Error() string {
    return fmt.Sprintf("%s had an error", au.name)
}

// You can then use it as an error.
func cantSum(n1, n2 float64) error {
    err := userError{name: "some error"}

    return &err
}

func main() {
    userError1 := &userError{"us0p"}
    userError2 := &userError{"us0p"}
    anotherUserError1 := anotherUserError{"us0p"}
    anotherUserError2 := anotherUserError{"us0p"}

    fmt.Printf("userError1 == userError2: %t\n", userError1 == userError2)
    // output: false
    // Even holding the same values they are not equal because they point to different memory addresses.
    fmt.Printf("anotherUserError1 == anotherUserError2: %t\n", anotherUserError1 == anotherUserError2)
    // output: true
    // Here they are equal because we didn't used a pointer receiver.

}
