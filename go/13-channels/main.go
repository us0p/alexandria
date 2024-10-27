package main

import (
	"fmt"
	"time"
    "sync"
)

// concurrency != paralellism
// synchronous != sequential

// a goroutine is a way of running code asynchronously by meaning of concurrency.

func goroutines() {
    // To use a function in a goroutine we use the keyword go.
    go fmt.Println(2)

    fmt.Println(1)
    // The proccess wont wait for tasks in a goroutine, therefore we need to wait for then to finish
    // to execute all the tasks.
    time.Sleep(time.Second)

    // To wait for all goroutines lauched to finish we can use the WaitGroup:
    var wg sync.WaitGroup

    for i := 0; i < 5; i++ {
        // For each goroutine that we lauch we need to increment the group count by 1:
        wg.Add(1)

        i := i
        // Here we are redeclaring i because each iteration of the loop uses the same instance of the variable i, 
        // so each closure shares that single variable. When the closure runs, it prints the value of i at the time 
        // fmt.Println is executed, but i may have been modified since the goroutine was launched.
        // So if we didn't redeclare variable i here the print fn would print the same value in all executions because,
        // that would be the current value of i then.
        // To detect this problem before it happens run go vet.

        // Wrap the worker call in a closure that makes sure to tell the WaitGroup that this worker is done.
        go func() {
            defer wg.Done()
            fmt.Println(i) // This print call can return number out of the order, that's because it's being executed asynchronously.
        }()
    }

    // Block until the WaitGroup counter goes back to 0. 
    wg.Wait()
}

// Channels are a typed, thread-safe queue. Channels allow different goroutines to communicate with each other.
// Tip:
// Empty structs (struct{}) are often used as tokens in go, this is, when we don't care about the result, only if we receive something and when.
// We can block and wait until something is sent on a channel with:
// <- ch

func channels() chan int {
    // Channels need to be created before use.
    // Sending to a nil channel will block forever.
    // ch := make(chan int)

    // Channels can be buffered.
    ch := make(chan int, 1) // 1 is the number of itens the channel will store before it is full.
    // Sending on a buffered channel only blocks when the buffer is full.
    // Receiving blocks only when the buffer is empty.
    // Buffered channels can be used within the same thread.

    // Sending data to a channel is done with the <- operator which is called channel operator.
    // Data flows in the direction of the arrow.
    // This operation will block until another goroutine is ready to receive the value.
    // Receiving from a nil channel blocks forever.
    ch <- 69 // If the channel is full already and all the consumers are idle, this operation will panic with a deadlock, which means that a groupof
    // of goroutines are blocked and none of them can continue.

    // Receiving data from a channel, in this case saving it into a variable.
    // This will also block until there is a value to read in the channels.
    v := <- ch // This will also panic with a deadlock if the channels is empty and there are no producing goroutines.

    fmt.Println(v)

    // Channels can be explicitly closed by the sender
    close(ch)

    // ch is now empty and closed, trying to send on a closed channels will case a panic.
    return ch
}

func ranginChannels() {
    for i := 1; i <= 5; i++ {
        ch := make(chan int, i)
        for j := 0; j < i; j++ {
            ch <- j
        }

        // Channels can be ranged over, simmilar to generators.
        // k will receive values from the channel (blocking at each iteration if nothing new is there).
        // This loops exits only when the channel is closed.
        for k := range ch {
            fmt.Printf("Channel range: %d\n", k)
            if k + 1 == i {
                close(ch)
            }
        }
    }
}

// When we have a goroutine that listen to multiple channels we can use the select statement to listen to multiple
// channels at the same time. It's similar to a switch statement but for channels.
// If multiple channels are ready at the same time one is chosen randomly.
// Note: the channels passed to this function are read only as defined by the type <-chan string.
// For writing only channels we could use the type chan<- string.
func logMessages(chEmails, chSms <-chan string) {
		select {
			case em, ok := <-chEmails:
                if !ok {
                    return
                }
				fmt.Println(em)
			case sm, ok := <-chSms:
                if !ok {
                    return
                }
				fmt.Println(sm)
		}

        // The default case in a select statement executes immediately if no other channel has a value ready. 
        // A default case stops the select statement from blocking.
}

func main() {
    goroutines()
    ch := channels()

    _, ok := <-ch

    if !ok {
        fmt.Println("Channels is closed")
    }
    ranginChannels()
}
