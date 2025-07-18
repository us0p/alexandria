# `*Client.Do`
Senda an HTTP request and returns an HTTP response, following policy as 
configured on the client.  
  
An error is returned if caused by client policy, or failure to speak HTTP. 
  
```golang
client := &http.Client{
    CheckRedirect: redirectPolicyFunc,
}

req, err := client.Get("http://example.com")
// ...

req.Header.Add("If-None-Match", "W/wyzzy")
resp, err := client.Do(req)
```
