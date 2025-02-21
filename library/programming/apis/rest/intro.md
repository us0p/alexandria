# Representational State Transfer - REST
Is an architectural style for designing networked applications. It relies 
on standard HTTP methods (GET, POST, PUT, DELETE) to interact with 
resources, which are represented as URIs (Uniform Resource Identifiers). 
REST APIs are stateless, meaning each request from a client to a server 
must contain all the information needed to understand and process the 
request. They use standard HTTP status codes to indicate the outcome of 
requests and often communicate in formats like JSON or XML. REST APIs are 
widely used due to their simplicity, scalability, and ease of integration 
with web services and applications.

## What's an API?
An API is a set of definitions and protocols for building and integrating 
application software. It’s sometimes referred to as a contract between an 
information provider and an information user.

REST is a set of architectural constraints, not a protocol or a standard.
API developers can implement REST in a variety of ways.
the REST constraints do not specify a communication protocol.
in today’s Internet world, RESTful almost always means an HTTP-based API.

## The six constraints
1. **Uniform Interface**: defines the interface between clients and 
   servers. It simplifies and decouples the architecture, which enables 
   each part to evolve independently. The four guiding principles of the 
   uniform interface are:
   1. **Resource based**: Individual resources are identified in requests 
      using URIs as resource identifiers. The resources themselves are 
      conceptually separate from the representations that are returned to 
      the client. For example, the server does not send its database, but 
      rather, some HTML, XML or JSON that represents some database records
      expressed 
   2. **Manipulation of Resources Through Representations**: When a client 
      holds a representation of a resource, including any metadata 
      attached, it has enough information to modify or delete the resource
      on the server, provided it has permission to do so.
   3. **Self-descriptive Messages**: Each message includes enough 
      information to describe how to process the message. For example, 
      which parser to invoke may be specified by an Internet media type 
      (previously known as a MIME type). Responses also explicitly indicate
      their cache-ability.
   4. **Hypermedia as the Engine of Application State (HATEOAS)**: Clients 
      deliver state via body contents, query-string parameters, request 
      headers and the requested URI (the resource name). Services deliver 
      state to clients via body content, response codes, and response 
      headers. This is technically referred-to as hypermedia (or hyperlinks
      within hypertext). 
      Aside from the description above, HATEOS also means that, where 
      necessary, links are contained in the returned body (or headers) to 
      supply the URI for retrieval of the object itself or related objects.
2. **Stateless**: Essentially, what this means is that the necessary state
   to handle the request is contained within the request itself, whether as
   part of the URI, query-string parameters, body, or headers. The URI 
   uniquely identifies the resource and the body contains the state (or 
   state change) of that resource. Then after the server does its 
   processing, the appropriate state, or the piece(s) of state that matter,
   are communicated back to the client via headers, status and response 
   body.
   Implementing the concept of “session” which maintains state across 
   multiple HTTP requests can be confused with a stateful application.
   In REST, the client must include all information for the server to 
   fulfill the request, resending state as necessary if that state must 
   span multiple requests, thus, each request is indeed stateless.
   There are cases that don’t honor the statelessness principle, such as 
   three-legged OAuth, API call rate limiting, etc.
   1. **State**: Data necessary for the current session or request.
   2. **Resource**: Defines the resourece representation, data stored in 
      the database for instance.
3. **Cacheable**: As on the World Wide Web, clients can cache responses. 
   Responses must therefore, implicitly or explicitly, define themselves as
   cacheable, or not, to prevent clients reusing stale or inappropriate 
   data in response to further requests.
4. **Client-Server**: The uniform interface separates clients from servers.
   This means that clients and servers doesn't need to care about the 
   responsibilities of other's layers.
5. **Layered System**: A client cannot ordinarily tell whether it is 
   connected directly to the end server, or to an intermediary along the 
   way.
6. **Code on Demand (optional)**: Servers are able to temporarily extend or
   customize the functionality of a client by transferring logic to it that
   it can execute. Examples of this may include compiled components such as
   client-side scripts such as JavaScript.
