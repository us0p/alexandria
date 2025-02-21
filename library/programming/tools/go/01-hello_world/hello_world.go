package main

import "fmt"

// Those constans are dynamically typed as string;
const (
	spanish    = "Spanish"
	french     = "French"
	portuguese = "Portuguese"

	englishHelloPrefix    = "Hello, "
	spanishHelloPrefix    = "Holla, "
	frenchHelloPrefix     = "Bonjour, "
	portugueseHelloPrefix = "Olá, "
)

// This is the full form of a variable declaration
var targetLanguage string = "English"

func Hello(name string, language string) string {
	if name == "" {
		name = "World"
	}

	return greetingPrefix(language) + name
}

func greetingPrefix(language string) (prefix string) {
	switch language {
	case french:
		prefix = frenchHelloPrefix
	case spanish:
		prefix = spanishHelloPrefix
	case portuguese:
		prefix = portugueseHelloPrefix
	default:
		prefix = englishHelloPrefix
	}

	return
}

func main() {
	// This is the short form of a variable declaration;

	name := "world"

	// We don't provide a type, but we must provide a initialization value;
	// This cannot be used outside functions bodies or if, for or switch initializers;

	// Unlike regurar variable declarations, a short variable declaration may redeclare variables provided earlier in the same block
	// (or the parameters lists if the block is the function body) with the same type, and at least one of the non-blank variables is new.
	// As a consequence, redeclaration can only appear in a multi-variable short declaration.
	// The non-blank variable names on the left side of := must be unique.

	name, targetLanguage := "Luan Lopes", "Portuguese" // redeclares name and targetLanguage

	// name := "Luan Lopes" will throw an error because we're not adding new variables on the left side;

	// x, y, x := 1, 2, 3                              // illegal: x repeated on left side of :=

	fmt.Println(Hello(name, targetLanguage))
}
