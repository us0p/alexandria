package main

import (
	"errors"
	"fmt"
)

// A pointer is a variable that stores the memory address of another variable.
// The * sintax defines a pointer:
// var p *int
// The & operator generates a pointer to its operand
// myInt := 1
// p = &myInt

// Go doesn't have pointer arithmetic

// Trying to deference a nil pointer will cause a runtime error (panic)

// Here you are creating your own type from an existing one;
type Bitcoin int

// This is very useful when you want to add some domain specific
// functionality on top of existing types.

// This is not really necessary, but i let it here to remember that
// any value that implements a String method will fall withing the
// Stringer interface which is used internally to define the "native"
// format for that value.
type Stringer interface {
    String() string
}

// This interface is defined in the fmt package and lets you define
// how your type is printed when used with the %s format string in prints.

func (b Bitcoin) String() string {
    return fmt.Sprintf("%d BTC", b)
}

type Wallet struct {
	balance Bitcoin
}

// func (w Wallet) Deposit(value int)
// This syntax will provide a copy from the provided wallet to the method
// therefore changes to that copy wont reflect in the real wallet.
// To make the changes in the real wallet we need to receive a pointer to it
func (w *Wallet) Deposit(value Bitcoin) {
	// We get the pointer (memory address) of something by placing an & at the beginning of the symbol.
	//fmt.Printf("address of balance in Deposit is %v \n", &w.balance)
	w.balance += value
}

// There's no need to use a pointer to wallet here
// however, by convention you should keep your method receiver types
// the same for consistency

func (w *Wallet) Balance() Bitcoin {
	// This is a shorthand for the full deferenced notation:
	// (*w).balance
	return w.balance

	// These pointers to structs are also called struct pointers
	// and they are automatically deferenced.
}

// Errors are values:
var ErrInsufficientFunds = errors.New("cannot withdraw, insufficient funds")

func (w *Wallet) Withdraw(total Bitcoin) error {
    if total > w.balance {
        // This creates a new error with a message of your choosing.
        return ErrInsufficientFunds
    }

    w.balance -= total
    return nil
}
