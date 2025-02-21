# Skipping
Tests or benchmarks may be skipped at run time with a call to the Skip 
method of `*T` or `*B`  

```go
func TestTimeConsuming(t *testing.T) {
    if testing.Short() {
        t.Skip("skipping test in short mode.")
    }
}
```

The Skip method of `*T` can be used in a fuzz target if the input is 
invalid, but should not be considered a failing input.  

```go
func FuzzJSONMarshaling(f *testing.F) {
    f.Fuzz(func(t *testing.T, b []byte) {
        var v interface{}
        if err := json.Unmarshal(b, &v); err != nil {
            t.Skip()
        }
        if _, err := json.Marshal(v); err != nil {
            t.Errorf("Marshal: %v", err)
        }
    })
}
```

