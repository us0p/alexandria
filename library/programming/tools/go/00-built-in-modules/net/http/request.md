# `http.Request`
Represents an HTTP request.  
## `http.NewRequestWithContext`
Returns a new `http.Request` given a method, URL, and optional body.  
  
The `http.Request` returned is suitable for use with `*Client.Do` or 
`Transport.RoundTrip`.  
  
For outgoing client request, the context controls the entire lifetime of a 
request and its response.  
  
If body is of type `*bytes.Buffer`, `*bytes.Reader`, or `*strings.Reader`, 
the returned request's `ContentLength` is set to its exact value, `GetBody`
is populated, and `Body` is set to `NoBody` if the `ContentLength` is 0.
