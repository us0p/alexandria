# Enterprise Go API Architecture – Summary

## 1. Standard Way to Connect `http.ServeMux` to Controllers

In enterprise Go applications:

- `main.go` is responsible for wiring dependencies.
- Repositories are injected into services.
- Services are injected into controllers (handlers).
- Controller methods are registered with `http.ServeMux`.

This follows clean architecture principles and keeps the system testable and maintainable.

---

## 2. The Scaling Concern (100+ Endpoints)

Manually wiring every controller and service in `main.go` does not scale well.

### Key Insight:
You wire **per module**, not per endpoint.

Instead of initializing every controller separately in `main.go`, you group related functionality into domain modules.

---

## 3. Scalable Module-Based Structure

Recommended feature-based (vertical slice) structure:

```
internal/
  user/
    entity.go
    repository.go
    service.go
    handler.go
    module.go
  order/
    entity.go
    repository.go
    service.go
    handler.go
    module.go
```

Each folder represents a **self-contained domain module**.

---

## 4. Module-Level Wiring Pattern

Each module exposes:

- `NewModule(...)`
- `RegisterRoutes(mux *http.ServeMux)`

### Inside a Module:

1. Create repository
2. Create service (inject repository)
3. Create handler (inject service)
4. Register routes

### `main.go` stays clean:

```go
userModule := user.NewModule(db)
orderModule := order.NewModule(db)

userModule.RegisterRoutes(mux)
orderModule.RegisterRoutes(mux)
```

Even with 100 endpoints, you might only have 8–15 modules.

---

## 5. Where to Define the Entity (e.g., User)?

Two main approaches:

### Option 1 – Pragmatic Go (Recommended)

Define the entity inside the feature module:

```
internal/user/entity.go
```

Example:

```go
package user

type User struct {
    ID    string
    Email string
    Name  string
}
```

Why this works well:

- Keeps everything related to the domain in one place
- Avoids over-engineering
- Most common in production Go services

---

### Option 2 – Strict DDD Style

Separate domain layer:

```
internal/
  domain/
    user.go
  user/
    repository.go
    service.go
    handler.go
    module.go
```

Use this when:

- The domain is complex
- You need multiple repository implementations
- You want strict separation from infrastructure

Most Go teams prefer Option 1 unless the system is very large.

---

## 6. Core Architectural Principles

- Package = architectural boundary
- Avoid circular dependencies
- Keep controllers thin
- Keep business logic in services
- Use manual dependency injection
- Scale by modularizing wiring
- `main.go` should remain small

---

## Final Takeaway

Enterprise Go applications scale well when:

- Architecture is modular (feature-based / vertical slice)
- Wiring happens per domain module
- `main.go` stays minimal
- Entities live with their owning domain (unless strong DDD constraints apply)

Explicit dependency wiring in Go is not a flaw — it is a design feature that improves clarity, testability, and maintainability.
