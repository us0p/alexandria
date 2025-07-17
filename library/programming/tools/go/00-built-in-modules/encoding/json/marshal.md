# `json.Marshal`
Encondes a value into a valid JSON representation.
```golang
import "encoding/json"

type Message struct {
    Name string
    Body string
    Time int64
}

func main() {
    m := Message{"Alice", "Hello", 123456789}

    json, err := json.Marshal(m)

    // json will be a []byte containing the JSON data.
}
```

The json package only accesses the exported fields of struct types.  
  
Therefore, only the exported fields of a struct will be present in the JSON
output.  
  
The encoding of each struct field can be customized by the format string 
stored under the "json" struct field's tag.  
  
The format string gives the name of the field, possibly followed by a 
comma-separated list of options. The name may be empty in order to specify 
options without overriding the default field name.  
  
The **"omitempty"** option specifies that the field should be omitted from 
the encoding if the field has an **falsy** value.  
 
As a special case, if the field tag is **"-"**, the field is always omitted.
  
**Examples**
```golang
type MyStruct struct {
    // Field appears in JSON as key "myName".
    Field int `json:"myName"`
    
    // Field appears in JSON as key "myName" and
    // the field is omitted from the object if its value is empty,
    // as defined above.
    Field int `json:"myName,omitempty"`
    
    // Field appears in JSON as key "Field" (the default), but
    // the field is skipped if empty.
    // Note the leading comma.
    Field int `json:",omitempty"`
    
    // Field is ignored by this package.
    Field int `json:"-"`
    
    // Field appears in JSON as key "-".
    Field int `json:"-,"`
}
```
  
The **"string"** option signals that a field is stored as JSON inside a 
JSON-encoded string. It applies only to fields of string, floating point, 
integer, or boolean types.
```golang
type MyStruct struct {
    Int64String int64 `json:",string"`
}
```
  
**Map** values encode as JSON objects. The map's key type must either be a 
string, an integer type, or implement `encoding.TextMarshaler`.
  
Pointer values encode as the value pointed to. A nil pointer encodes as the
null JSON value.  
  
Interface values encode as the value contained in the interface. A nil 
interface value encodes as the null JSON value.
