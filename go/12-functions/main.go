package main

import "fmt"

// This is a variadic function.
// Variadic function can take an arbitrary number of FINAL arguments
// that will be received as a slice of that type.
func printStrings(strings ...string) {
    for _, string := range strings {
        fmt.Println(string)
    }
}

// Go supports first-class and higher-order functions:
func add(x, y int) int {
  return x + y
}

func mul(x, y int) int {
  return x * y
}

// aggregate applies the given math function to the first 3 inputs
func aggregate(a, b, c int, arithmetic func(int, int) int) int {
  return arithmetic(arithmetic(a, b), c)
}

// Currying is the practice of creating a function that receive a function(s) as input and returns a new function.
// It's a High-Order Function, and its best use scenario is when you want to add extra behavior on a function
// that you don't have access to:
func curryingPrintf(addPrefix func()) func (string, ...interface{}) (int, error) {
    return func (s string, values ...interface{}) (int, error) {
        addPrefix()
        return fmt.Printf(s, values...)
    }
}

func addPrefix () {
    fmt.Printf("You typed: ")
}

// The defer keyword allows a function to be executed automatically just before its enclosing function returns:
// The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.
// A defer call will be executed even if the function has multiple returns
func def() {
    defer fmt.Println("end")
    fmt.Println("start")
}

// A closure is a function that references variables from outside its own function body. The function may access and assign to the referenced variables.
func concatter() func(string) string {
	doc := ""
	return func(word string) string {
		doc += word + " "
		return doc
	}
}

func doMath(mather func (float64, float64) float64, f1, f2 float64) float64 {
    return mather(f1, f2)
}

func main() {
    strings := []string{
        "Hello",
        "World",
    }

    // We can spread the arguments into a variadic function with the spread operator.
    printStrings(strings...)

    fmt.Printf("aggregate fn with add %d\n", aggregate(2, 3, 4, add))
    fmt.Printf("aggregate fn with mul %d\n", aggregate(2, 3, 4, mul))

    myPrintf := curryingPrintf(addPrefix)

    myPrintf("A test of my version of Prinff %t\n", true)

    def()

    harryPotterAggregator := concatter()
	harryPotterAggregator("Mr.")
	harryPotterAggregator("and")
	harryPotterAggregator("Mrs.")
	harryPotterAggregator("Dursley")
	harryPotterAggregator("of")
	harryPotterAggregator("number")
	harryPotterAggregator("four,")
	harryPotterAggregator("Privet")

	fmt.Println(harryPotterAggregator("Drive"))

    // Anonymus function
    mathResult := doMath(func (f1, f2 float64) float64{
        return f1 + f2
    }, 4.0, .9)
    
    fmt.Printf("mathResult: %.2f\n", mathResult)
}
