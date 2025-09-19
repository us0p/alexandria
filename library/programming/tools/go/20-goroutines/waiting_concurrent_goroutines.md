The most idiomatic way to wait for multiple concurrent operations to finish is to use a `sync.WaitGroup`.

```go
package main

import (
	"fmt"
	"net/http"
	"sync"
)

func main() {
	urls := []string{
		"https://example.com",
		"https://golang.org",
		"https://httpbin.org/get",
	}

	var wg sync.WaitGroup
	results := make([]string, len(urls)) // preallocate to avoid race on append

	// making several calls concurrently
	for i, url := range urls {
		// increate wait count
		wg.Add(1)

		go func(i int, url string) {
			// decreases wait count
			defer wg.Done()

			resp, err := http.Get(url)
			if err != nil {
				results[i] = fmt.Sprintf("error: %v", err)
				return
			}
			defer resp.Body.Close()

			results[i] = resp.Status
		}(i, url)
	}

	// Wait for all goroutines to finish
	// Will wait util count goes back to 0
	wg.Wait()

	fmt.Println("Results:", results)
}
```