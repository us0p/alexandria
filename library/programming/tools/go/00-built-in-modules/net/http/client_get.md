# `*Client.Get`
Issues a GET to the specified URL.  
  
An error is returned if there was an HTTP protocol error.
```golang
resp, err := http.Get("http://example.com/")
// ...
```
  
There's also `http.Get` which is a wrapper around `DefaultClient.Get`.
