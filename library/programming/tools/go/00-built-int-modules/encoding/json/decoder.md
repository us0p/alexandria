# `json.Decoder`
Reads and decodes data from an input stream.  
  
Can be used to write to HTTP connections, WebSockets, or files.
## `json.NewDecoder`
Rerturns a new decoder that reads from input stream.

### `*Decoder.Decode`
Decode reads the next JSON-encoded value from its input and stores it in 
the value pointed to.

```golang
import (
    "encoding/json"
    "net/http"
)

func main() {
    var receiver map[string]interface{}

    resp, _ := http.get("https://google.com")
    defer resp.Body.Close() 

    decoder := json.NewDecoder(resp.Body)
    _ := decoder.decode(&receiver)

    // If everything is ok, receiver is going to hold the response body.
}
```

It decodes data as it's received.

```golang
import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"strings"
)

func main() {
	const jsonStream = `
	{"Name": "Ed", "Text": "Knock knock."}
	{"Name": "Sam", "Text": "Who's there?"}
	{"Name": "Ed", "Text": "Go fmt."}
	{"Name": "Sam", "Text": "Go fmt who?"}
	{"Name": "Ed", "Text": "Go fmt yourself!"}
`
	type Message struct {
		Name, Text string
	}
	dec := json.NewDecoder(strings.NewReader(jsonStream))
	for {
		var m Message
		if err := dec.Decode(&m); err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%s: %s\n", m.Name, m.Text)

        // Ed: Knock knock.
        // Sam: Who's there?
        // Ed: Go fmt.
        // Sam: Go fmt who?
        // Ed: Go fmt yourself!
	}
}
```
