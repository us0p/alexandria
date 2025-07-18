# `*Client.PostForm`
Issues a POST to the specified URL, with data's key and values URL-encoded 
as the request body.  
  
The `Content-Type` header is set to `application/x-www-form-urlencoded`.  
```golang
resp, err := http.PostForm(
    "http://example.com/form",
    url.Values{
        "key": {"Value"},
        "id": {"123"}
    })
// ...
```
  
There's also `http.PostForm` which is a wrapper around `DefaultClient.PostForm`.
