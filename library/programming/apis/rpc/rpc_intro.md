# Remote Procedure Call (RPC)
![[Pasted image 20250630064042.png]]
Is a protocol that allows a program to invoke a function or procedure on a different computer (or process) across a network **as if it were a local function call**.

The complexities of the underlying network communication (e.g., sending requests, receiving responses) are abstracted away from the programmer.

stubs/proxies codes are generated from an IDL (Interface Definition Language) and are generated on both sides based on a shared contract which is commonly defined using IDL files.

RPC uses a client-server protocol and when a client invokes a function:
1. The client's stub serializes the method name and its arguments into a protobuf (gRPC) and this data is transmitted over the wire by the communication module which handles network communication with HTTP/2.
2. The server's communication module receives the call and its stub decodes the method name and arguments and calls the appropriate function.
3. The server repeats the process to return the response to the client.

**Use RPC when:**
- You are **building distributed systems or microservices** that need to communicate and you **control both client and server**.
- You require **performance** and **low-latency communication** between services (compared to something heavier like REST+JSON).
- You want **tighter integration** between components (e.g., remote services that resemble local function calls).
**Avoid RPC when**:
- You're building public facing APIs.
- You need loosely coupled services.
## Benefits
- **Abstraction of network communication**: Developers don’t need to manage sockets, protocols, or HTTP. Network calls are hidden behind familiar interfaces.
- **Performance**: Binary protocols like **gRPC** are faster than REST (JSON over HTTP). 
- **Strong typing & contracts**: Interfaces and message schemas (e.g., via Protocol Buffers) define exactly what data is exchanged.
- **Support for bidirectional streams**: Allows the implementation of real-time applications because of its dependency on HTTP/2 multiplexing which allows the creation of bidirectional streams over a single TCP connection.
## Drawbacks
- **Tight coupling**: Services can become tightly coupled due to shared contracts/interfaces. A new API must be defined for every new operation or use case.
- **Complexity**: Requires service discovery, load balancing, and potentially retry logic and error handling.
- **Less human-readable**: Binary protocols like gRPC are not easy to inspect like JSON.
