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
	- Refactoring Toward Deeper Insight
		- **Continuous Refactoring**: Refactoring is the process of redesigning the code to make it better without changing application behavior. Refactoring is usually done in small, controllable steps, with great care so we don’t break functionality or introduce some bugs. After all, the purpose of refactoring is to make the code better not worse. Automated tests are of great help to ensure that we haven’t broken anything. There is another type of refactoring, one related to the domain and its model. Sometimes there is new insight into the domain, something becomes clearer, or a relationship between two elements is discovered. All that should be included in the design through refactoring. Technical refactoring, the one based on patterns, can be organized and structured. Refactoring toward deeper insight cannot be done in the same way. We cannot create patterns for it. The complexity of a model and the variety of models do not offer us the possibility to approach modeling in a mechanistic way. A good model is the result of deep thinking, insight, experience, and flair. One of the first things we are taught about modeling is to read the business specifications and look for nouns and verbs. The nouns are converted to classes, while the verbs become methods. This is a simplification, and will lead to a shallow model. All models are lacking depth in the beginning, but we should refactor the model toward deeper and deeper insight. Using a proven set of basic building blocks along with consistent language brings some sanity to the development effort. This leaves the challenge of actually finding an incisive model, one that captures subtle concerns of the domain experts and can drive a practical design. A model that sloughs off the superficial and captures the essential is a deep model. This should make the software more in tune with the way the domain experts think and more responsive to the user’s needs. Sophisticated domain models are seldom developed except through an iterative process of refactoring, including close involvement of the domain experts with developers interested in learning about the domain.
		- **Bring Key Concepts Into Light**: Refactoring is done in small steps. The result is also a series of small improvements. There are times when lots of small changes add very little value to the design, and there are times when few changes make a lot of difference. It’s a Breakthrough. We start with a coarse, shallow model. Then we refine it and the design based on deeper knowledge about the domain, on a better understanding of the concerns. We add new concepts and abstractions to it. The design is then refactored. Each refinement adds more clarity to the design. This creates in turn the premises for a Breakthrough. To reach a Breakthrough, we need to make the implicit concepts explicit. When we talk to the domain experts, we exchange a lot of ideas and knowledge. Some of the concepts make their way into the Ubiquitous Language, but some remain unnoticed at the beginning. They are implicit concepts, used to explain other concepts which are already in the model. During this process of design refinement, some of those implicit concepts draw our attention. We discover that some of them play a key role in the design. At that point we should make the respective concepts explicit. We should create classes and relationships for them. When that happens, we may have the chance of a Breakthrough. Sometimes sections of the design may not be so clear. There is a set of relationships that makes the path of computation hard to follow. Or the procedures are doing something complicated which is hard to understand. This is awkwardness in the design. This is a good place to look for hidden concepts. When building knowledge it is possible to run into contradictions. What a domain expert says seem to contradict what another upholds. A requirement may seem to contradict another. Some of the contradictions are not really contradictions, but different ways of seeing the same thing, or simply lack of accuracy in explanations. We should try to reconcile contradictions. Sometimes this brings to light important concepts. Even if it does not, it is still important to keep everything clear. There are other concepts which are very useful when made explicit: Constraint, Process and Specification. A Constraint is a simple way to express an invariant. Processes are usually expressed in code with procedures. We won’t use a procedural approach, since we are using an object oriented language, so we need to choose an object for the process, and add a behavior to it. The best way to implement processes is to use a Service. If there are different ways to carry out the process, then we can encapsulate the algorithm in an object and use a Strategy. Not all processes should be made explicit. If the Ubiquitous Language specifically mentions the respective process, then it is time for an explicit implementation. The last method to make concepts explicit that we are addressing here is Specification. Simply said, a Specification is used to test an object to see if it satisfies a certain criteria. The domain layer contains business rules which are applied to Entities and Value Objects. Those rules are usually incorporated into the objects they apply to. Some of these rules are just a set of questions whose answer is “yes” or “no”. Such rules can be expressed through a series of logical operations performed on Boolean values, and the final result is also a Boolean. One such example is the test performed on a Customer object to see if it is eligible for a certain credit. The rule can be expressed as a method, named isEligible(), and can be attached to the Customer object. But this rule is not a simple method which operates strictly on Customer data. Evaluating the rule involves verifying the customer’s credentials, checking to see if he paid his debts in the past, checking to see if he has outstanding balances, etc. Such business rules can be large and complex, bloating the object to the point that it no longer serves its original purpose. At this point we might be tempted to move the entire rule to the application level, because it seems that it stretches beyond the domain level. Actually, it is time for a refactoring. The rule should be encapsulated into an object of its own, which becomes the Specification of the Customer, and should be kept in the domain layer. The new object will contain a series of Boolean methods which test if a certain Customer object is eligible for credit or not. Each method plays the role of a small test, and all methods combined give the answer to the original question. If the business rule is not comprised in one Specification object, the corresponding code will end up being spread over a number of objects, making it inconsistent.
```Java
Customer customer = customerRepository.findCustomer(customerIdentiy);

Specification customerEligibleForRefund = new Specification( 
	new CustomerPaidHisDebtsInThePast(), 
	new CustomerHasNoOutstandingBalances()
); 

if(customerEligibleForRefund.isSatisfiedBy(customer)) { 
	refundService.issueRefundTo(customer);
}
```

- **Preserving Model Integrity**: When multiple teams work on a project, code development is   done in parallel, each team being assigned a specific part of the   model. Those parts are not independent, but are more or less   interconnected. They all start with one big model, and they are   given a share of it to implement. Let’s say that one of the teams   has created a module, and they make it available for other teams   to use it. A developer from another team starts using the module,   and discovers that it is missing some functionality needed for his   own module. He adds the needed functionality and checks-in the   code so it can be used by all. What he might not realize is that   this is actually a change of the model, and it is quite possible that this change will break application functionality. The first requirement of a model is to be consistent, with invariable terms and no contradictions. The internal consistency of a model is called unification. An enterprise project could have one model covering the entire domain of the enterprise, with no contradictions and overlapping terms. A unified enterprise model is an ideal which is not easily accomplished, and sometimes it is not even worth trying it. The solution is not so obvious, because it is the opposite of all we have learned so far. Instead of trying to keep one big model that will fall apart later, we should consciously divide it into several models. Several models well integrated can evolve independently as long as they obey the contract they are bound to. Each model should have a clearly delimited border, and the relationships between models should be defined with precision.
	- **Bounded Context**: Each model has a context. When we deal with a single model, the context is implicit. We do not need to define it. When we create an application which is supposed to interact with other software, for example a legacy application, it is clear that the new application has its own model and context, and they are separated from the legacy model and its context. But when we work on a large enterprise application, we need to define the context for each model we create. There is no formula to divide one large model into smaller ones. Try to put in a model those elements which are related, and which form a natural concept. A model should be small enough to be assigned to one team. Team cooperation and communication is more fluid and complete, which helps the developers working on the same model. The context of a model is the set of conditions which need to be applied to make sure that the terms used in the model have a specific meaning. The main idea is to define the scope of a model, to draw up the boundaries of its context, then do the most possible to keep the model unified. Explicitly define the context within which a model applies. Explicitly set boundaries in terms of team organization, usage within specific parts of the application, and physical manifestations such as code bases and database schemas. Keep the model strictly consistent within these bounds, but don’t be distracted or confused by issues outside. A Bounded Context is not a Module. A Bounded Context provides the logical frame inside of which the model evolves. Modules are used to organize the elements of a model, so Bounded Context encompasses the Module. When using multiple models, everybody can work freely on their own piece. We all know the limits of our model, and stay inside the borders. We just have to make sure we keep the model pure, consistent and unified. Each model can support refactoring much easier, without repercussions on other models. The design can be refined and distilled in order to achieve maximum purity. There is a price to pay for having multiple models. We need to define the borders and the relationships between different models. This requires extra work and design effort, and there will be perhaps some translation between different models. We won’t be able to transfer any objects between different models, and we cannot invoke behavior freely as if there was no boundary. But this is not a very difficult task, and the benefits are worth taking the trouble.
	- **Continuous Integration**: Once a Bounded Context has been defined, we must keep it sound. When a number of people are working in the same Bounded Context, there is a strong tendency for the model to fragment. We need a process of integration to make sure that all the new elements which are added fit harmoniously into the rest of the model, and are implemented correctly in code. We need to have a procedure used to merge the code. The sooner we merge the code the better. For a single small team, daily merges are recommended. We also need to have a build process in place. The merged code needs to be automatically built so it can be tested. Another necessary requirement is to perform automated tests. If the team has a test tool, and has created a test suite, the test can be run upon each build, and any errors are signaled. The code can be easily changed to fix the reported errors, because they are caught early, and the merge, build, and test process is started again.
	- **Context Map**: Is a document which outlines the different Bounded Contexts and the relationships between them. Each Bounded Context should have a name which should be part of the Ubiquitous Language. That helps the team communication a lot when talking about the entire system. Everyone should know the boundaries of each context and the mapping between contexts and code. A common practice is to define the contexts, then create modules for each context, and use a naming convention to indicate the context each module belongs to. We present a series of patterns which can be used to create Context Maps where contexts have clear roles and their relationships are pointed out. The Shared Kernel and Customer-Supplier are patterns with a high degree of interaction between contexts. Separate Ways is a pattern used when we want the contexts to be highly independent and evolve separately. There are another two patterns dealing with the interaction between a system and a legacy system or an external one, and they are Open Host Services and Anticorruption Layers.
	![[Pasted image 20251118180703.png]]
	- **Shared Kernel**: When functional integration is limited, the overhead of Continuous Integration may be deemed too high. This may especially be true when the teams do not have the skill or the political organization to maintain continuous integration, or when a single team is simply too big and unwieldy. So separate Bounded Contexts might be defined and multiple teams formed. Therefore, designate some subset of the domain model that the two teams agree to share. Of course this includes, along with this subset of the model, the subset of code or of the database design associated with that part of the model. This explicitly shared stuff has special status, and shouldn’t be changed without consultation with the other team. Integrate a functional system frequently, but somewhat less often than the pace of Continuous Integration within the teams. During these integrations, run the tests of both teams. The purpose of the Shared Kernel is to reduce duplication, but still keep two separate contexts. Development on a Shared Kernel needs a lot of care. Both teams may modify the kernel code, and they have to integrate the changes. If the teams use separate copies of the kernel code, they have to merge the code as soon as possible, at least weekly. A test suite should be in place, so every change done to the kernel to be tested right away. Any change of the kernel should be communicated to another team, and the teams should be informed, making them aware of the new functionality.
	- **Customer-Supplier**: Is a pattern that depicts two subsystems that have have a dependency relationship. One depends a lot on the other. The contexts in which those two subsystems exist are different, and the processing result of one system is fed into the other. They do not have a Shared Kernel, because it may not be conceptually correct to have one, or it may not even be technically possible for the two subsystems to share common code. For example, assuming we agree to have separate models, let's consider two models web shopping and reporting of an e-commerce application. Notice that the web shopping is not at all concerned about the reporting module data but the reporting module is very much concerned about the web shopping data and actually might need some extra data to take on it's tasks. Following that, the supplier subsystem has to implement some specifications which are needed by the customer subsystem. This is one connection between the two subsystems. Another requirement is related to the database used, more exactly its schema. Both applications will make use of the same database. If the e-shopping subsystem was the only one to access the database, the database schema could be changed any time to reflect its needs. But the reporting subsystem needs to access the database too, so it needs some stability of its schema. The two teams will need to communicate, probably they will have to work on the database together, and decide when the change is to be performed. This will act as a limitation for the reporting subsystem, because that team would prefer to swiftly do the change and move on with the development, instead of waiting on the e-shopping app. This pattern works well when the teams are under the same management. The reporting team should play the customer role, while the e shopping team should play the supplier role. The customer team should present its requirements, while the supplier team should make the plans accordingly. While all the customer team’s requirements will have to be met in the end, the timetable for doing that is decided by the supplier team. If some requirements are considered really important, they should be implemented sooner, while other requirements might be postponed. The customer team will also need input and knowledge to be shared by the supplier team. This process flows one way, but it is necessary in some cases. The interface between the two subsystems needs to be precisely defined. A conformity test suite should be created and used to test at any time if the interface requirements are respected. The supplier team will be able to work more unreservedly on their design because the safe net of the interface test suite alerts them whenever it is a problem. Add these tests to the supplier team’s test suite, to be run as part of its continuous integration. This testing will free the supplier team to make changes without fear of side effects to the customer team’s application.
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