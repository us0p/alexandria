package main

import "testing"

func TestHello(t *testing.T) {
	t.Run("Saying hello to people", func(t *testing.T) {
		got := Hello("Luan", "")
		want := "Hello, Luan"

        assertCorrectMessage(t, got, want)
	})

	t.Run("Say 'Hello, World' when an empty string is supplied", func(t *testing.T) {
		got := Hello("", "")
		want := "Hello, World"

        assertCorrectMessage(t, got, want)
	})

    t.Run("In Spanish", func(t *testing.T) {
        got := Hello("Lopes", "Spanish")
        want := "Holla, Lopes"
        assertCorrectMessage(t, got, want)
    })

    t.Run("In French", func(t *testing.T) {
        got := Hello("Luan Lopes", "French")
        want := "Bonjour, Luan Lopes"
        assertCorrectMessage(t, got, want)
    })

    t.Run("In Portuguese", func(t *testing.T) {
        got := Hello("Luan Lopes de Faria", "Portuguese")
        want := "Olá, Luan Lopes de Faria"
        assertCorrectMessage(t, got, want)
    })
}

func assertCorrectMessage(t testing.TB, got, want string) {
    t.Helper()
    if got != want {
        t.Errorf("got %q want %q", got, want)
    }
}
