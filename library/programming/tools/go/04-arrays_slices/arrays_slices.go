package main

import "fmt"

// The size of the Array is encoded in its type. If you try to pass an [4]int
// into a function that expects [5]int, it won't compile.
// They are different types so it's just the same as trying to pass a string
// into a function that wants an int.

// You can't use slices with arrays as they are from different types;
// []int cannot be used with [5]int;
func Sum(numbers []int) int {
    sum := 0

    for _, number := range numbers {
        sum += number
    }

    return sum
}

func SumAll(numbersToSum ...[]int) []int {
    var sums []int

    for _, numbers := range numbersToSum {
        sums = append(sums, Sum(numbers))
    }

    return sums
}

// Slices can be sliced! The syntax is slice[low:high]. 
// If you omit the value on one of the sides of the : it 
// captures everything to that side of it. 
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int

    for _, numbers := range numbersToSum {
        if len(numbers) == 0 {
            sums = append(sums, 0)
        } else {
            tail := numbers[1:]
            sums = append(sums, Sum(tail))
        }
    }

    return sums
}

func printNum() {
    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }
}
