# `http.ServeMux`
HTTP request multiplexer. It matches URL of each incoming request against a list of registered patterns and calls the handler for the pattern that most closely matches the URL.

Handlers are attached to the `http.ServeMux` to respond to requests.

The `http.DefaultServeMux` is a variable under the `net/http` package that provides a default implementation of `http.ServeMux`.

When you call `http.Handle` or `http.HandleFunc` you're registering handlers on the `http.DefaultServeMux`.

If you create your own `http.ServeMux` you need to call its `Handle` and `HandleFunc` methods to attach the necessary handlers.