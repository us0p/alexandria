# Learning Roadmap
### Pre-Requisites
- Design Patterns
	- Facade
	- Adapter
	- Factory/Abstract Factory
	- Builder
	- Strategy
- Architectural Styles
	- Layered
### Reference people
- Eric Evans
- Vaughn Vernon
- Jimmy Bogard
## 💬 **2. Building the Ubiquitous Language**
### 🎯 Goal:
Learn to collaborate with domain experts and model the business _in a shared language_.
### 📚 Learn:

- How to discover and refine **domain terms** with non-technical stakeholders.
- Use **Event Storming** or **Domain Storytelling** to uncover workflows.
- Create a **Glossary** of shared terms.
### 🧩 Practice:
- Run a mock “discovery session” for a simple domain (e.g., online bookstore, car rental).
- Identify entities, value objects, and aggregates in that domain.
### 🧰 Tools:
- Sticky notes, whiteboard (physical or Miro/Mural)
- EventStorming guides by Alberto Brandolini
---
## 🧱 **3. Strategic Design — Structuring the Big Picture**
### 🎯 Goal:
Learn how to organize large systems into coherent, independent parts.
### 📚 Learn:
- **Bounded Contexts** — distinct models within the same domain.
- **Context Maps** — relationships between contexts.
- **Core, Supporting, and Generic Subdomains** — prioritizing effort.
### 🧠 Key skills:
- Identify where one model ends and another begins.
- Manage integration (e.g., via published language, ACLs, or anti-corruption layers).
### 📘 Read:
- Evans book: Chapters 14–16
- _Implementing Domain-Driven Design_ by Vaughn Vernon — Part I
- _DDD Distilled_ by Vaughn Vernon — short and practical
---
## ⚙️ **4. Tactical Design — Modeling Inside a Bounded Context**
### 🎯 Goal:
Learn how to express the domain model in code.
### 📚 Learn:
- **Entities** — objects with identity.
- **Value Objects** — immutable objects defined by value.
- **Aggregates** — transactional consistency boundaries.
- **Repositories** — persistence abstraction.
- **Domain Events** — representing significant occurrences.
- **Factories** — for complex object creation.
- **Services** — stateless domain operations.
### 🧩 Practice:
Implement these concepts in your language of choice (e.g., Java, C#, Python, TypeScript).
### 🧰 Suggested stack (optional):
- **C#:** .NET + MediatR + EF Core
- **Java:** Spring Boot + Axon Framework
- **Node.js:** NestJS + TypeORM
- **Python:** FastAPI + SQLAlchemy
---
## 🧠 **5. Applying DDD in Real Projects**
### 🎯 Goal:
Understand when and how to apply DDD in the real world.
### 📚 Learn:
- DDD is **not for everything** — it shines in **complex domains**.
- How to combine DDD with:
    - **Hexagonal Architecture (Ports & Adapters)**
    - **CQRS**
    - **Event Sourcing**
    - **Microservices**
### 🧩 Practice:
- Refactor an existing application using DDD principles.
- Identify bounded contexts and aggregate roots.
- Implement command and query separation.
### 📘 Read:
- _Implementing Domain-Driven Design_ — Vaughn Vernon (deep dive)
- _Learning Domain-Driven Design_ — Vlad Khononov (modern and practical)
---
## 🚀 **6. Advanced Topics and Ecosystem**
### 🎯 Goal:
Go beyond code — think in systems.
### 📚 Learn:
- **Event-driven architectures**
- **Domain events as integration contracts**
- **DDD and Microservices alignment**
- **DDD in distributed systems**
- **Collaborative modeling techniques**
### 📘 Read / Watch:
- _Strategic Monoliths and Microservices_ — Vaughn Vernon
- _Patterns, Principles, and Practices of DDD_ — Scott Millett
- Talks by Nick Tune, Alberto Brandolini, and Mathias Verraes