package main

import "fmt"

// Generics allow us to use variables to refer to specific types.

// Withoud generics:
func splitStringSlice(s []string) ([]string, []string) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}

// With generics:
// T is the name of the type parameter, and it must match the any constraint, which means it can be anything.
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
// Constraints are just interfaces that allow us to write generics that only operate within the constraint of 
// a given interface type. In the example above, the any constraint is the same as the empty interface because it means the type in question can be anything.
// In other words, constraints are interfaces and you can use any type that implements the interface.

// Type lists
// Ordered is a type constraint that matches any ordered type.
// An ordered type is one that supports the <, <=, >, and >= operators.
type Ordered interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
        ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
        ~float32 | ~float64 |
        ~string
}

type book struct {
    title string
    author string
    price float64
}

func (b book) Price() float64 {
    return b.price
}

func (b book) Name() string {
    return fmt.Sprint("%s by %s", b.title, b.author)
}

type toy struct {
	name  string
	price float64
}

func (t toy) Price() float64 {
	return t.price
}

func (t toy) Name() string {
	return t.name
}

type bookStore struct {
    booksSold []book
}

func (bs *bookStore) Sell(b book) {
    bs.booksSold = append(bs.booksSold, b)
}

type toyStore struct {
	toysSold []toy
}

func (ts *toyStore) Sell(t toy) {
	ts.toysSold = append(ts.toysSold, t)
}

// Intefaces definitions can accept type parameters as well.
type store[P product] interface {
    Sell(P)
}

type product interface {
    Price() float64
    Name() string
}

// sellProducts takes a store and a slice of products and sells
// each product one by one.
func sellProducts[P product](s store[P], products []P) {
	for _, p := range products {
		s.Sell(p)
	}
}

func main() {
    bs := bookStore{
		booksSold: []book{},
	}
    
    // By passing in "book" as a type parameter, we can use the sellProducts function to sell books in a bookStore
    // Here we're passing the address of bs because sellProducts expects a store which is an interface and terefore can be nil.
	sellProducts[book](&bs, []book{
		{
			title:  "The Hobbit",
			author: "J.R.R. Tolkien",
			price:  10.0,
		},
		{
			title:  "The Lord of the Rings",
			author: "J.R.R. Tolkien",
			price:  20.0,
		},
	})
	fmt.Println(bs.booksSold)

    // We can then do the same for toys
	ts := toyStore{
		toysSold: []toy{},
	}
	sellProducts[toy](&ts, []toy{
		{
			name:  "Lego",
			price: 10.0,
		},
		{
			name:  "Barbie",
			price: 20.0,
		},
	})
	fmt.Println(ts.toysSold)
}
