# Benchmarks
Functions of the form

```go
func BenchmarkXxx(*testing.B)
```

Are executed by the `go test` command when its `-bench` flag is provided. 
Benchmarks are run sequentially.  
A sample benchmark function looks like this:  

```go
func BenchmarkRandInt(b *testing.B) {
    for range b.N {
        rand.Int()
    }
}
```

The benchmark function must run the target code `b.N` times. It is called 
multiple times with `b.N` adjusted until the benchmark function lasts long 
enough to be timed reliably.  
  
> BenchmarkRandInt-8   	68453040	        17.8 ns/op

This output means that the loop ran 68453040 times at a speed of 17.8 ns 
per loop.  
If a benchmark needs some expensive setup before running, the timer may be
reset:  

```go
func BenchmarkBigLen(b *testing.B) {
    big := NewBig()
    b.ResetTimer()
    for range b.N {
        big.Len()
    }
}
```

If a benchmark needs to test performance in a parallel setting, it may use 
the RunParallel helper function; such benchmarks are intended to be used 
with the `-cpu` flag.  

```go
func BenchmarkTemplateParallel(b *testing.B) {
    templ := template.Must(template.New("test").Parse("Hello, {{.}}!"))
    b.RunParallel(func(pb *testing.PB) {
        var buf bytes.Buffer
        for pb.Next() {
            buf.Reset()
            templ.Execute(&buf, "World")
        }
    })
}
```
