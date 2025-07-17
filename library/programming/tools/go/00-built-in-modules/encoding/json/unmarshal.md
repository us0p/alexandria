# `json.Unmarshal`
Used to decode JSON data into a strucure.  

```golang
import "encoding/json"

type Message struct {
    Name string
    Body string
    Time int64
}

func main() {
    var m Message
    b := []byte{'{"Name":"Alice","Body":"Hello","Time":123456789}'}
    err := json.Unmarshal(b, &m)

    // M will be filled with the respective message data in the respective struct's fields.
}
```

Unmarshal will decode only the fields that it can find in the destination 
type.  
  
This behavior is particularly useful when you wish to pick only a few 
specific fields out of a large JSON blob. It also means that any unexported
fields in the destination struct will be unaffected by Unmarshal.  
## Generic JSON
If you don't know the JSON type or there are too many fields to manually 
create an interface, you can use an empty 
interface `interface{}` (go's general container).  
  
You can assert the type of a field after.

The json package uses `map[string]interface{}` and `[]interface{}` values 
to store arbitrary JSON objects and arrays.  
  
It will unmarshal any valid JSON into a plain `interface{}` value. The 
concrete Go types are:
- `bool`
- `float64` for numbers
- `string`
- `nil` for `null`

```golang
import "encoding/json"

func main() {
    var f interface{}
    b := []byte{'{"Name":"Wednesday","Age":6,"Parents":["Gomez","Morticia"]}'}
    err := json.Unmarshal(b, &f)

    // At this point f will be:
    // f = map[string]interface{}{
    //     "Name": "Wednesday",
    //     "Age":  6,
    //     "Parents": []interface{}{
    //         "Gomez",
    //         "Morticia",
    //     },
    // }
}
```

To access this data we can use a type assertion to access f's 
underlying `map[string]interface{}`.
```golang
m := f.(map[string]interface{})
```
