package main

import "testing"

func TestOccupation(t *testing.T) {
    occupationName := "Software Engineer"
    occupation := Occupation{name: occupationName, yearsOfExperience: 2}

    if occupation.name != occupationName {
        t.Errorf("Expecting occupation name to be %s, got %s", occupationName, occupation.name)
    }

    if occupation.yearsOfExperience != 2 {
        t.Errorf("Expecting yearsOfExperience to be %d, got %d", 2, occupation.yearsOfExperience)
    }
}

func TestCar (t *testing.T) {
    car := Car{maker: "Ford"}

    if car.maker != "Ford" {
        t.Errorf("Expecting maker to be %s, got %s", "Ford", car.maker)
    }
}

func TestPerson(t *testing.T) {
    fullName := "Luan Lopes de Faria"
    occupationName := "Software Engineer"
    person := Person{fullName: fullName, age: 25, Occupation: Occupation{occupationName, 2}, car: Car{"Ford"}}

    if person.fullName != fullName {
        t.Errorf("Expecting fullName to be %s, got %s", fullName, person.fullName)
    }

    if person.age != 25 {
        t.Errorf("Expecting age to be %d, got %d", 25, person.age)
    }

    // Note that fields from the Occuparion struct are present as top level fields of person.
    // That's the difference between embedded and nested structs.
    // Embedded struct's fields are accessed at the top level.

    if person.name != occupationName {
        t.Errorf("Expecting occupation name to be %s, got %s", occupationName, person.name)
    }

    if person.yearsOfExperience != 2 {
        t.Errorf("Expecting occupation yearsOfExperience to be %d, got %d", 2, person.yearsOfExperience)
    }

    // Nested struct's fields are accessed in a hierachical manner.

    if person.car.maker != "Ford" {
        t.Errorf("Expecting car maker to be %s, got %s", "Ford", person.car.maker)
    }
}
