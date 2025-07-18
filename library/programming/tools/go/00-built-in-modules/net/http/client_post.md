# `*Client.Post`
Issues a POST to the specified URL.  
  
If the provided body ia an `io.Closer`, it is closed after the request.
```golang
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
//...
```
  
There's also `http.Post` which is a wrapper around `DefaultClient.Post`.
