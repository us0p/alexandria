package main

import (
	"context"
	"fmt"
	"testing"
	"time"
)

type dictKey string

func TestWithValue(t *testing.T) {
	key := dictKey("key")
	ctx := context.WithValue(context.Background(), key, "value")

	if v := ctx.Value(key); v != "value" {
		t.Errorf("Expected key '%s' to have value '%s\n", key, "value")
	}

	key2 := dictKey("foo")
	if v := ctx.Value(key2); v != nil {
		t.Errorf("Expected key '%s' to yield nil value, got '%s'\n", key2, v)
	}
}

func TestWithCancel(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	if _, ok := <-ctx.Done(); ok != false {
		t.Errorf("Channel should be closed as ctx was canceled")
	}
}

func TestWithDeadline(t *testing.T) {
	neverReady := make(chan int)

	timer := time.Now().Add(time.Second)

	ctx, cancel := context.WithDeadline(context.Background(), timer)
	defer cancel()

	select {
	case <-neverReady:
		t.Fatal("Channel should never be filled")
	case <-ctx.Done():
		fmt.Println("WithDeadline:", ctx.Err())
	}
}

func TestWithTimeout(t *testing.T) {
	neverReady := make(chan int)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	select {
	case <-neverReady:
		t.Fatal("Channel should never be filled")
	case <-ctx.Done():
		fmt.Println("WithTimeout:", ctx.Err())
	}
}
