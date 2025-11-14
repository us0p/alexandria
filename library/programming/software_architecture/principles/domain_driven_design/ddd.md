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
	- In order to create good software, one must understand the domain that software is trying to represent.
	- To understand the domain properly, the developer needs to coordinate with domain specialists.
	- Any software of a complex domain needs to fit harmoniously with the domain. For that, the software needs to be a reflection of the domain. It needs to incorporate core concepts of the domain, and precisely realize the relationship between them.
	- Software has to model the domain.
	- It's necessary to create an abstraction of the domain. This abstraction is what we call the **domain model**. The domain model isn't an diagram, it's the idea the diagram is intended to convey.
	- The domain model is the internal representation of the target domain. During the design process we remember and make lots of references to the model. To do so, we need to organize information, systematize it, divide into smaller pieces and group it into logical groups. To do that, we need to leave some parts of the domain out. A domain contains too much information to include it all into the model.
	- The model is the essence of the software, but we need to create ways to express it, to communicate it with others. We are not alone in this process, so we need to share knowledge and information, and we need to do it well, precisely, completely, and without ambiguity.
	- Usually there are long discussions between software architects or developers and the domain experts. The software specialists want to extract knowledge from the domain experts, and they also have to transform it into a useful form. At some point, they might want to create an early prototype to see how it works so far. While doing that they may find some issues with their model, or their approach, and may want to change the model. The communication is not only one way. There is also feedback, which helps create a better model. Domain experts know their area of expertise well, but they organize and use their knowledge in a specific way, which is not always the best to be implemented into a software system. The analytical mind of the software designer helps unearth some of the key concepts of the domain during discussions with domain experts, and also help construct a structure for future discussion. This might seem like a very time consuming process, and it is, but this is how it should be
	- Use a language based on the model since it's the common ground. The team needs to use this language consistently and in all communications and in the code.
	- Iron out difficulties by experimenting with alternative expressions, which reflect alternative models. Then refactor the code, renaming classes, methods, and modules to conform to the new model. Resolve confusion over terms in conversation, in just the way we come to agree on the meaning of ordinary words.
	- A change in the language should become a change to the model. If domain experts cannot understand something in the model or the language, then it is most likely that there is something is wrong with it.
	- UML is a good tool to create the model and represents concepts as classes and represent relationships. It's easy for everyone to follow what is in the diagram. But it's only useful when the number of elements is small. Also, UML is not good at expression behavior. It cannot convey the meaning of the concepts it represents and what the objects are supposed to do. The advisable way of communicating the model is to use small diagrams each containing a subset of the model with text that explains that explains behavior and constraints the diagram cannot. Each subsection attempts to explain one important aspect of the domain.
	- The documents can be hand-draw, because that transmits the feeling that they are temporary and might be changed in the near future, which is true.
	- How to approach the transition from model to code: Developers should be included in the modeling process. The main idea is to choose a model which can be appropriately expressed in software and based on the model.
	- Design a portion of the software system to reflect the domain model in a very literal way, so that mapping is obvious. Revisit the model and modify it to be implemented more naturally in software, even as you seek to make it reflect deeper insight into the domain. Demand a single model that serves both purposes well, in addition to supporting a fluent Ubiquitous Language.
	- Building blocks of Model-Driven Design
		- Layered Architecture: Partition a complex program into LAYERS. Develop a design within each LAYER that is cohesive and that depends only on the layers below. Follow standard architectural patterns to provide loose coupling to the layers above. Concentrate all the code related to the domain model in one layer and isolate it from the user interface, application, and infrastructure code. The domain objects, free of the responsibility of displaying themselves, storing themselves, managing application tasks, and so forth, can be focused on expressing the domain model. Consider using Clean Architecture.
		- **Entities**: Category of objects which seem to have an identity, which remains the same throughout the states of the software. For these objects it is not the attributes which matter, but a thread of continuity and identity, which spans the life of a system and can extend beyond it. When an object is distinguished by its identity, rather than its attributes, make this primary to its definition in the model. Keep the class definition simple and focused on life cycle continuity and identity. Define a means of distinguishing each object regardless of its form or history. e alert to requirements that call for matching objects by attributes. Define an operation that is guaranteed to produce a unique result for each object. The model must define what it means to be the same thing.
		- **Value Objects**: Object used to describe certain aspects of a domain, and which doesn't have identity. It's highly recommended that value objects be immutable. Being immutable and having no identity means they can be shared, and for being immutable they also have data integrity. If Value Objects are shareable, they should be immutable. Value Objects should be kept thin and simple. Value Objects can contain other Value Objects, and they can even contain references to Entities. Although Value Objects are used to simply contain attributes of a domain object, that does not mean that it should contain a long list with all the attributes. Attributes can be grouped in different objects. Attributes chosen to make up a Value Object should form a conceptual whole.
		![[Pasted image 20251114082952.png]]
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