package main

import "fmt"

type Enum int // creating specific type for type safety

const (
	StateActive Enum = iota // iota generates successive constant values automatically.
	StateAway
	StateOffline
)

// If needed, can create a map[Enum]string to provide string representation through Stringer.
var names = map[Enum]string{
	StateActive:  "active",
	StateAway:    "away",
	StateOffline: "offline",
}

func (e Enum) String() string {
	return names[e]
}

func main() {
	fmt.Println(StateActive)  // should print "active"
	fmt.Println(StateAway)    // should print "away"
	fmt.Println(StateOffline) // should print "offline"
}
