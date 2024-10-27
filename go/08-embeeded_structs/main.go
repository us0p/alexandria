package main

type Occupation struct {
    name string
    yearsOfExperience int
}

type Car struct {
    maker string
}

// Occupation here is embedded, which mean that Person now has all the fields present in the Occuation struct.
// It's simmilar to inheritance of Object Oriented languages but in Go we are just elevating and sharing fields between structs definitions.
// You can find how to create those structs in the test file.

type Person struct {
    Occupation // Embedded struct
    car Car // Nested struct
    fullName string
    age int
}

// All the methods present in the embedded Occupation struct will be accesssible from the Person struct too.
