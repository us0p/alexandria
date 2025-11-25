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
	- **Conformist**: The customer is very dependent on the supplier, while the supplier is not. If there is a management to make this work, the supplier will pay the needed attention and will listen to the customer’s requests. If the management has not decided clearly how things are supposed to be between the two teams, or if there is poor management or lack of it, the supplier will slowly be more concerned about its model and design, and less interested in helping the customer. They have their own deadlines after all. Even if they are good people, willing to help the other team, the time pressure will have its say, and the customer team will suffer. This also happens when the teams belong to different companies. When two development teams have a Customer-Supplier relationship in which the supplier team has no motivation to provide for the customer team’s needs, the customer team is helpless. The customer project will be delayed until the team ultimately learns to live with what it is given. An interface tailored to the needs of the customer team is not in the cards. The customer team could adhere to the supplier team’s model, conforming entirely to it. This is much like the Shared Kernel, but there is an important difference. The customer team cannot make changes to the kernel. They can only use it as part of their model, and they can build on the existing code provided. When somebody provides a rich component, and provides an interface to it, we can build our model including the respective component as it would be our own. If the component has a small interface, it might be better to simply create an adapter for it, and translate between our model and the component’s model. This would isolate our model, and we can develop it with a high degree of freedom.
		- **Anticorruption Layer**: We often encounter circumstances when we create an application which has to interact with legacy software or a separate application. This is another challenge for the domain modeler. Many legacy applications have not been built using domain modeling techniques, and their model is confused, entangled hard to understand and hard to work with. Even if it was well done, the legacy application model is not of much use for us, because our model is likely to be quite different. There are different ways for our client system to interact with an external one. One is via network connections. Both applications need to use the same network communication protocols, and the client needs to adhere to the interface used by the external system. Another method of interaction is the database. The external system works with data stored in a database. The client system is supposed to access the same database. In both cases we are dealing with primitive data being transferred between the systems. While this seems to be fairly simple, the truth is that primitive data does not contain any information about the models. We cannot take data from a database and treat it all as primitive data. There is a lot of semantics hidden behind the data. A relational database contains primitive data related to other primitive data creating a web of relationships. The data semantics is very important, and needs to be considered. The client application can’t access the database and write to it without understanding the meaning of the data used. There is the risk for the external model to alter the client model if we allow that to happen. We can’t ignore the interaction with the external model, but we should be careful to isolate our own model from it. We should build an Anticorruption Layer which stands between our client model and the external one. From our model’s perspective, the Anticorruption Layer is a natural part of the model; it does not look like something foreign. It operates with concepts and actions familiar to our model. But the Anticorruption Layer talks to the external model using the external language not the client one. This layer works as a two way translator between two domains and languages. The greatest achievement is that the client model remains pure and consistent without being contaminated by the external one. How should we implement the Anticorruption Layer? A very good solution is to see the layer as a Service from the client model. It is very simple to use a Service because it abstracts the other system and let us address it in our own terms. The Service will do the needed translation, so our model remains insulated. Regarding the actual implementation, the Service will be done as a Façade. Besides that, the Anticorruption Layer will most likely need an Adapter. The Adapter allows you to convert the interface of a class to the one understood by the client. In our case the Adapter does not necessarily wrap a class, because its job is to translate between two systems.
		![[Pasted image 20251121160133.png]]
		The Anticorruption Layer may contain more than one Service. For each Service there is a corresponding Façade, and for each Façade we add an Adapter. We should not use a single Adapter for all Services, because we clutter it with mixed functionality. We still have to add one more component. The Adapter takes care of wrapping up the behavior of the external system. We also need object and data conversion. This is done using a translator. This can be a very simple object, with little functionality, serving the basic need of data translation. If the external system has a complex interface, it may be better to add an additional Façade between the adapters and that interface. This will simplify the Adapter’s protocol, and separate it from the other system.
	- **Separate Ways**: The Separate Ways pattern addresses the case when an enterprise application can be made up of several smaller applications which have little or nothing in common from a modeling perspective. There is a single set of requirements, and from the user’s perspective this is one application, but from a modeling and design point of view it may done using separate models with distinct implementations. We should look at the requirements and see if they can be divided in two or more sets which do not have much in common. If that can be done, then we can create separate Bounded Contexts and do the modeling independently. Before going on Separate Ways we need to make sure that we won’t be coming back to an integrated system. Models developed independently are very difficult to integrate. They have so little in common that it is just not worth doing it.
	- **Open Host Service**: When we try to integrate two subsystems, we usually create a translation layer between them. This layer can be a consistent one, depending on the complexity of relationships and how the external subsystem was designed. If the external subsystem turns out to be used not by one client subsystem, but by several ones, we need to create translation layers for all of them. When a subsystem has to be integrated with many others, there is more and more to maintain, and more and more to worry about when changes are made. The solution is to see the external subsystem as a provider of services. If we can wrap a set of Services around it, then all the other subsystems will access these Services, and we won’t need any translation layer. The difficulty is that each subsystem may need to interact in a specific way with the external subsystem, and to create a coherent set of Services may be problematic. Define a protocol that gives access to your subsystem as a set of Services. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the protocol for that special case so that the shared protocol can stay simple and coherent.
	- **Distillation**: Distillation is the process of separating the substances composing a mixture. The purpose of distillation is to extract a particular substance from the mixture. During the distillation process, some byproducts may be obtained, and they can also be of interest. A large domain has a large model even after we have refined it and created many abstractions. It can remain big even after many refactorings. In situations like this, it may be time for a distillation. The idea is to define a Core Domain which represents the essence of the domain. The byproducts of the distillation process will be Generic Subdomains which will comprise the other parts of the domain. When working with a large model, we should try to separate the essential concepts from generic ones. In the beginning we gave the example of an air traffic monitoring system. We said that a Flight Plan contains the designed Route the plane must follow. The Route seems to be an ever present concept in this system. Actually, this concept is a generic one, and not an essential one. The Route concept is used in many domains, and a generic model can be designed to describe it. The essence of the air traffic monitoring is somewhere else. The monitoring system knows the route that the plane should follow, but it also receives input from a network of radars tracking the plane in the air. This data shows the actual path followed by the plane, and it is usually different from the prescribed one. The system will have to compute the trajectory of the plane based on its current flight parameters, plane characteristics and weather. The trajectory is a four dimensional path which completely describes the route that the plane will travel in time. The module which synthesizes the plane trajectory from the available data is the heart of the business system here. This should be marked out as the core domain. The routing model is more of a generic domain. The Core Domain of a system depends on how we look at the system. A simple routing system will see the Route and its dependencies as central to the design. The air traffic monitoring system will consider the Route as a generic subdomain. The Core Domain of an application may become a generic subdomain of another. It is important to correctly identify the Core, and determine the relationships it has with other parts of the model. Emphasize the most valuable and specialized concepts. Make the Core small. Spend the effort in the Core to find a deep model and develop a supple design—sufficient to fulfill the vision of the system. Justify investment in any other part by how it supports the distilled Core. Some parts of the model add complexity without capturing or  communicating specialized knowledge. The model clogs up with general principles everyone knows or details that belong to specialties which are not your primary focus but play a supporting role. Yet, however generic, these other elements are essential to the functioning of the system and the full expression of the model. Identify cohesive subdomains that are not the motivation for your project. Factor out generic models of these subdomains and place them in separate Modules. Leave no trace of your specialties in them. Once they have been separated, give their continuing development lower priority than the Core Domain, and avoid assigning your core developers to the tasks. Also consider off-the shelf solutions or published models for these Generic Subdomains. Every domain uses concepts that are used by other domains. Money and their related concepts like currency and exchange rate can be included in different systems. Charting is another widely used concept, which is very complex in itself, but it can be used in many applications. There are different ways to implement a Generic Subdomain:
		- **Off-the-shelf Solution**: This one has the advantage of having the entire solution already done by someone else. There is still a learning curve associated with it, and such a solution introduces some dependencies.
		- **Outsourcing**: The design and implementation is given to another team, probably from another company. There is still the inconvenience of integrating the outsourced code. The interface used to communicate with the subdomain needs to be defined and communicated to the other team.
		- **Existing Model**: One handy solution is to use an already created model.
		- **In-House Implementation**: This solution has the advantage of achieving the best level of integration. It does mean extra effort, including the maintenance burden.
- Keep in mind some of the pitfalls of domain modeling: 
	1) Stay hands-on. Modelers need to code.
	2) Focus on concrete scenarios. Abstract thinking has to be anchored in concrete cases.
	3) Don't try to apply DDD to everything. Draw a context map and decide on where you will make a push for DDD and where you will not. And then don't worry about it outside those boundaries.
	4) Experiment a lot and expect to make lots of mistakes. Modeling is a creative process.
## Case of study - DDD Service
Let’s consider a practical example, a web reporting application. The reports make use of data stored in a database, and they are generated based on templates. The final result is an HTML page which is shown to the user in a web browser. The UI layer is incorporated in web pages and allows the user to login, to select the desired report and click a button to request it. The application layer is a thin layer which stands between the user interface, the domain and the infrastructure. It interacts with the database infrastructure during login operations, and interacts with the domain layer when it needs to create reports. The domain layer will contain the core of the domain, objects directly related to the reports. Two of those objects are Report and Template, which the reports are based on. The infrastructure layer will support database access and file access. When a user selects a report to be created, he actually selects the name of the report from a list of names. This is the reportID, a string. Some other parameters are passed, like the items shown in the report and the time interval of the data included in the report. But we will mention only the reportID for simplicity. This name is passed through the application layer to the domain layer. The domain layer is responsible for creating and returning the report being given its name. Since reports are based on templates, a Service could be created, and its purpose would be to obtain the template which corresponds to a reportID. This template is stored in a file or in the database. It is not appropriate to put such an operation in the Report object itself. It does not belong to the Template object either. So we create a separate Service whose purpose is to retrieve a report template based on report’s ID. This would be a service located in the domain layer. It would make use of the file infrastructure to retrieve the template from the disk.
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