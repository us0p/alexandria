package main

import (
	"testing"
	//"fmt"
)

func TestWallet(t *testing.T) {
	t.Run("Deposit", func(t *testing.T) {
		wallet := Wallet{}

		wallet.Deposit(Bitcoin(10))

		want := Bitcoin(10)

		assertBalance(t, wallet, want)
	})

	t.Run("Withdraw", func(t *testing.T) {
		wallet := Wallet{balance: Bitcoin(20)}

		err := wallet.Withdraw(Bitcoin(10))

		want := Bitcoin(10)

		assertBalance(t, wallet, want)
		assertNoError(t, err)
	})

	t.Run("Withdraw insufficient funds", func(t *testing.T) {
		startingBalance := Bitcoin(20)
		wallet := Wallet{startingBalance}
		err := wallet.Withdraw(Bitcoin(100))

		assertError(t, err, ErrInsufficientFunds)
		assertBalance(t, wallet, startingBalance)
	})
}

func assertBalance(t testing.TB, wallet Wallet, want Bitcoin) {
	t.Helper()
	got := wallet.Balance()

	//fmt.Printf("address of balance in test is %v \n", &wallet.balance)

	if got != want {
		t.Errorf("got %s want %s", got, want)
	}
}

func assertError(t testing.TB, got error, want error) {
	t.Helper()
	// Erros can be nil because the return type of Withdraw will be error,
	// which is an interface. If you see a function that takes arguments or returns
	// values that are interfaces, they can be nillable
	// Trying to access a value that is nil it will throw a runtime panic.
	if got == nil {
		t.Fatal("didn't get an error but wanted one")
	}

	// We've introduced t.Fatal which will stop the test if it is called. This is
	// because we don't want to make any more assertions on the error returned if
	// there isn't one around. Without this the test would carry on to the next
	// step and panic because of a nil pointer.

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}

func assertNoError(t testing.TB, got error) {
	t.Helper()
	if got != nil {
		t.Errorf("didn't expect to receive an error but got %q", got)
	}
}
