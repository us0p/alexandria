If you need to test the same behavior under different inputs, using table driven tests allows you to set a table (slice) of inputs and then you can perform the same test for different inputs rather than write multiple tests that are equal.
```go
func TestFetchScenarios(t *testing.T) {
	// cases table, is used to generate tests
	cases := []struct{
		name    string
		handler http.HandlerFunc
		wantErr bool
	}{
		{"ok response", func(w http.ResponseWriter, r *http.Request) {
			fmt.Fprint(w, `{"status":"ok"}`)
		}, false},
		{"server error", func(w http.ResponseWriter, r *http.Request) {
			http.Error(w, "fail", http.StatusInternalServerError)
		}, true},
	}

	for _, tc := range cases {
		// Wrap each case into a T.Run so you can pinpoint individual tests.
		t.Run(tc.name, func(t *testing.T) {
			ts := httptest.NewServer(tc.handler)
			defer ts.Close()

			_, err := FetchMessage(ts.URL)
			if tc.wantErr && err == nil {
				t.Fatal("expected error")
			}
		})
	}
}
```