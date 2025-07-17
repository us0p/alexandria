# `json.Encoder`
Encoder type. Writes JSON values to an output stream.  
  
Can be used to write to HTTP connections, WebSockets, or files.
## `json.NewEncoder`
Returns a new encoder that writes to the stream.
### `*Encoder.Encode`
Encode writes the JSON encoding of the provided structure to the stream, 
with insignificant space characters elided, followed by a newline 
character.

```golang
import (
    "encoding/json"
    "log"
    "os"
)

func main() {
    dec := json.NewDecoder(os.Stdin)
    enc := json.NewEncoder(os.Stdout)
    for {
        var v map[string]interface{}
        if err := dec.Decode(&w); err != nil {
            log.Println(err)
            return
        }
        for k := range v {
            if k != "Name" {
                delete(v, k)
            }
        }
        if err: enc.Encode(&v); err != nil {
            log.Println(err)
        }
    }
}
```
