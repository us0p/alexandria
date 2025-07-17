# GraphQL
A query language and runtime created by Facebook.

Instead of hitting multiple [REST](rest_intro.md) endpoints to get related data, clients can ask exactly for what they need in a single request.
## Benefits
- **No under or over fetching**: Clients get exactly what they need in a single request, great for mobile and low-bandwidth environment.
- **Strong typing & schema**: The API is self documented.
- **Client-driven development**: Frontend teams can build queries without waiting for backend teams.
- **Efficient for nested data**: Fetching related, nested data is more efficient.
## When to use it
- You need flexible API across many frontend platforms.
- Your UI components require related data from many sources.
- Frontend is going to evolve faster than backend.
- You want to avoid versioning (GraphQL uses a single evolving schema).
## Disadvantages
- **Overhead for small apps**: Simple CRUD should be built with [REST](rest_intro.md).
- **Complexity in caching**: HTTP cache is harder because queries are POST requests, not simple GETs.
- **N+1 Problem**: Inefficient queries can easily happen if not optimized at the server.
- **Authorization**: Fine-grained access control must be done per field or query, which can get complex.
- **Performance tuning**: Requires tools like `DataLoader` or persisted queries to manage performance.
