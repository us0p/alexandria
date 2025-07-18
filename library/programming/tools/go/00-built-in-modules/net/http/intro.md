# `net/http`
Provide HTTP client and server implementations.
## Common rules.
- A non-2xx response doesn't cause an error.
- To make a request with custom headers, use `NewRequest` and `*Client.Do`.  
- To make a request with a specified context, use `NewRequestWithContext` 
and `*Client.Do` `http.Client`
- Any returned error will be of type `url.Error`.
- Caller should close `resp.Body` when done reading from it. 
