```go
package iteration

import "strings"

func Repeat(character string, times int) string {
	var repeated string
	for i := 0; i < times; i++ {
		repeated += character
	}
	return repeated
}

func Reverse(str []byte) {
	// Declaring many variables in a single loop
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		tmp := str[i]
		str[i] = str[j]
		str[j] = tmp
	}
}

func NativeRepeat(character string, times int) string {
	return strings.Repeat(character, times)
}
```