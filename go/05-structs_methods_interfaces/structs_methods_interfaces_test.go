package main

import "testing"

func TestPerimeter(t *testing.T) {
	rectangle := Rectangle{10.0, 10.0}
	got := Perimeter(rectangle)
	want := 40.0

	if got != want {
		t.Errorf("got %.2f want %.2f", got, want)
	}
}

//func TestArea(t *testing.T) {
//
//    checkArea := func(t testing.TB, shape Shape, want float64) {
//        t.Helper()
//        got := shape.Area()
//        if got != want {
//            t.Errorf("got %g want %g", got, want)
//        }
//    }
//
//	t.Run("Rectangles", func(t *testing.T) {
//		rectangle := Rectangle{12.0, 6.0}
//        checkArea(t, rectangle, 72.0)
//	})
//
//	t.Run("Circles", func(t *testing.T) {
//		circle := Circle{10}
//        checkArea(t, circle, 314.1592653589793)
//	})
//}

// Table driven tests:
func TestArea(t *testing.T) {
	// Anonumous struct
	areTests := []struct {
		name    string
		shape   Shape
		hasArea float64 // improving test readability, it tells exactly what the data is about;
	}{
		{"Rectangle", Rectangle{12, 6}, 72.0},
		// You can name the fields too:
		{name: "Triangle", shape: Triangle{Base: 12, Height: 6}, hasArea: 36},
		{name: "Circle", shape: Circle{Radius: 10}, hasArea: 314.1592653589793},
	}

	for _, tt := range areTests {
		// By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case;
        // And you can run specific tests within your table with go test -run TestArea/Rectangle;
		t.Run(tt.name, func(t *testing.T) {
			got := tt.shape.Area()
			if got != tt.hasArea {
				t.Errorf("%#v got %g want %g", tt.shape, got, tt.hasArea)
			}
		})
	}
}
