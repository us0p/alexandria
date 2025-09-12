## Partial Struct
You can model only the fields you care about. Go will ignore anything that isn't defined.
```go
import (
	"encoding/json"
	"fmt"
)

type Response struct {
	Result []struct {
		TokenInfo struct {
			Supply       uint64 `json:"supply"`
			Decimals     int    `json:"decimals"`
			TokenProgram string `json:"token_program"`
		} `json:"token_info"`
	} `json:"result"`
}

func main() {
	data := []byte(`{"jsonrpc":"2.0","result":[{"token_info":{"supply":999935381034790,"decimals":6,"token_program":"TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}}],"id":"1"}`)

	var resp Response
	if err := json.Unmarshal(data, &resp); err != nil {
		panic(err)
	}
}
```
## Use `map[string]any`
Less type-safe, but quick for prototyping.
```Go
// snippet
	var m map[string]any
	json.Unmarshal(data, &m)
	
	result := m["result"].([]any)
	first := result[0].(map[string]any)
	tokenInfo := first["token_info"].(map[string]any)
	
	fmt.Println("Supply:", tokenInfo["supply"])
// snippet
```
