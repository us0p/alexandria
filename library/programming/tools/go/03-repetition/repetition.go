package iteration

import "strings"

func Repeat(character string, times int) string {
    var repeated string
    for i:= 0; i < times; i++ {
        repeated += character
    }
    return repeated
}

func NativeRepeat(character string, times int) string {
    return strings.Repeat(character, times)
}
