package main

import (
	"fmt"
	"sync"
)

// Mutexes allow us to lock access to data. This ensures that we can control which goroutines can access certain data at which time.
// Maps are not safe for concurrent use. If you have multiple goroutines accessing the same map, and at least one of them is writing to the map, you must lock your maps with a mutex.
// We can protect a block of code by surrounding it with a call to Lock and Unlock.

// It's good practice to structure the protected code within a function so that defer can be used to ensure that we never forget to unlock the mutex.

// The sync.RWMutex is a reader/writer mutual exclusion lock. The lock can be held by an arbitrary number of readers or a single writer (multiple Rlock() calls can happen simultaneously).
// However, only one goroutine can hold a Lock() and all RLock()'s will also be excluded.
func main() {
	m := map[int]int{}

    mu := &sync.Mutex{}
    // With sync.Mutex you can only have one access for reading/writing to the data the time.

	go writeLoop(m, mu)
	go readLoop(m, mu)

	// stop program from exiting, must be killed
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int, mu *sync.Mutex) {
    // Here the type of mu could be *sync.RWMutex and we would lock the operation with mu.Lock() and mu.Unlock(), this will block the operation or writers allowing only one writing operation by the time.
	for {
		for i := 0; i < 100; i++ {
            mu.Lock() 
            // Any other code trying to access this map will wait until this operation is unlocked, any other call to Lock() in this map will wait until it's unlocked.
			m[i] = i
            mu.Unlock()
		}
	}
}

func readLoop(m map[int]int, mu *sync.Mutex) {
    // Here the type of mu could be *sync.RWMutex and we would lock the operation with mu.RLock() and mu.RUnlock(), this will allow n number of readers to read the data at the same time.
	for {
        mu.Lock() // This allows any number of readers to read from the same data at the same time, but only one writer can change it at the time.
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
        mu.Unlock()
	}
}
