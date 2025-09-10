`http.ListenAndServe` starts an HTTP server with a given address and handler.

The handler is usually `nil`, which means to use `DefaultServerMux`, `Handle` and `HandleFunc` add handlers to `DefaultServerMux`.
```go
import (
	"net/http"
	"fmt"
	"html"
	"log"
)

func main() {
	// fooHandler is of type http.Handler
	http.Handle("/foo", fooHandler)
	
	http.HandleFunc("/bar", func(w http.ResponseWritter, r *http.Request) {
		fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
	})
	
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

>You can create your own `http.Server` and `ListenAndServe` on it.