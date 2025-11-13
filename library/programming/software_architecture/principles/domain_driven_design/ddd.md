# Domain Driven Design
Is an approach to **software development** that aims to **match the mental model** of the problem domain we're addressing.

>Software should model the **business domain**, not just data or processes.

Doing so enables you to write expressive, rich and encapsulated software that are testable, scalable and maintainable that evolves alongside the business.
## When
- Misalignment between business and tech
- Over-complicated architectures
- Anemic domain models (consequence of MDD)
## How
- Discover the domain model by interacting with domain experts and agreeing upon a common set of terms to refer to **processes, actors and any other phenomenon that occurs in the domain**.
- Embed those terms into the code to create a rich model that reflects the actual business and its rules.
- Protect the model from all the other technical intricacies.
---
# Learning Roadmap
## 🩵 **1. Foundations — Understand the Mindset**

### 🎯 Goal:
Get the _why_ of DDD — what problems it solves, and how it differs from traditional architecture.
### 📚 Learn:
- The **core idea**: Software should model the **business domain**, not just data or processes.
- The **problems** DDD addresses:
### 📘 Read / Watch:
- _Domain-Driven Design Quickly_ (free summary of Evans’ book)
- Eric Evans — _Domain-Driven Design: Tackling Complexity in the Heart of Software_ (2003), Chapters 1–3
- Talks by Eric Evans, Vaughn Vernon, or Jimmy Bogard (YouTube)
### 🧠 Key concepts to grasp:
- Domain
- Subdomain
- Ubiquitous Language
- Model vs. implementation
- Complexity in business software

---

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
    

---

## 🧩 **7. Practice Projects and Community**

### 💻 Do:

- Build small DDD-style projects.
    
- Join open-source DDD projects.
    
- Participate in DDD meetups or Slack/Discord groups (e.g., “DDD Crew”).
    

### 🌐 Follow:

- **dddcommunity.org**
    
- **@vladikk**, **@vvvernon**, **@brandolini** on Twitter/X
    
- YouTube: _Virtual DDD_, _DDD Europe_
    

---

## 🗺️ **Summary Roadmap Flow**

**Phase 1 →** Mindset and Foundations  
**Phase 2 →** Ubiquitous Language and Discovery  
**Phase 3 →** Strategic Design (Bounded Contexts)  
**Phase 4 →** Tactical Design (Entities, Aggregates, etc.)  
**Phase 5 →** Implementation and Integration  
**Phase 6 →** Advanced and Distributed DDD  
**Phase 7 →** Real Projects + Community Learning