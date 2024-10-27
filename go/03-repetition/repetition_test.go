package iteration

import (
    "testing"
    "fmt"
)

func TestRepeat(t *testing.T) {
    repeated := Repeat("a", 7)
    expected := "aaaaaaa"

    if repeated != expected {
        t.Errorf("expected %q got %q", expected, repeated)
    }
}

func TestNativeRepeat(t *testing.T) {
    repeated := NativeRepeat("b", 3)
    expected := "bbb"

    if repeated != expected {
        t.Errorf("expected %q, got %q", expected, repeated)
    }
}

func BenchmarkRepeat(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Repeat("a", 2)
    }
}

func BenchmarkNativeRepeat(b *testing.B) {
    for i := 0; i < b.N; i++ {
        NativeRepeat("a", 5)
    }
}

func ExampleRepeat() {
    repeated := Repeat("a", 3)
    fmt.Println(repeated)
    // Output: aaa
}
