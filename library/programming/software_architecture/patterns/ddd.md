# Domain Driven Design
Is an architectural pattern that is used to design software systems based on the core business domain and business entities.

It provides several advantages over other architectural patterns, such as alignment with business goals and objectives, improved communication between domain experts and developers, a clear and expressive model of the business domain and improved scalability and maintainability.

It’s implemented using a set of principles and patterns such as **subdomains**, **bounded context**, **entities**, **value objects**, **aggregate**, and **repository**.

DDD is not a technology, rather it introduces terms, practices and principles to support decision making in complex business domains.
- The primary focus of the project is the core domain and domain logic.
- Complex designs are based on models of the domain.
- Collaboration between technical and domain experts is crucial to creating an application model that will solve particular domain problems.
## Domain model
A system of abstractions that describes **selected aspects** of a domain and can be used to solve problems related to that domain.

The domain model isn't an diagram, it's the idea the diagram is intended to convey.

The software needs to be a reflection of the domain. It needs to incorporate core concepts of the domain, and precisely realize the relationship between them.

The domain model is the internal representation of the target domain. To do that, we need to leave some parts of the domain out. A domain contains too much information to include it all into the model.

Usually there are long discussions between software architects or developers and the domain experts. The software specialists want to extract knowledge from the domain experts, and they also have to transform it into a useful form. At some point, they might want to create an early prototype to see how it works so far. While doing that they may find some issues with their model, or their approach, and may want to change the model. The communication is not only one way. There is also feedback, which helps create a better model. This might seem like a very time consuming process, and it is, but this is how it should be

The advisable way of communicating the model is to use small UML diagram each containing a subset of the model with text that explains behavior and constraints the diagram cannot. Each subsection attempts to explain one important aspect of the domain. The documents can be hand-draw, because that transmits the feeling that **they are temporary** and might be changed in the near future, which is true.
### How to approach the transition from model to code
1. Design a portion of the software system to reflect the domain model in a very literal way, so that mapping is obvious.
2. Revisit the model and modify it to be implemented more naturally in software, even as you seek to make it reflect deeper insight into the domain.
3. Demand a single model that serves both purposes well, in addition to supporting a fluent Ubiquitous Language.
## The Ubiquitous Language
 Is a methodology that refers to the same language domain experts and developers use when they talk about the domain they are working on.
 
 All the terms in the ubiquitous language are structured around the domain model.

The team needs to use this language consistently in all communications and in the code.

A change in the language should become a change to the model which represents a change into the code. If domain experts cannot understand something in the model or the language, then it is most likely that there is something is wrong with it.
## Building Blocks of Model-Driven Design
### [Layered Architecture](layer_architecture.md)
Concentrate all the code related to the domain model in one layer and isolate it from the user interface, application, and infrastructure code. Consider using [Clean Architecture](clean_architecture.md).
### Entities
Are objects that are defined by its identity and not by their attributes.

The identity remains the same throughout the states of the software.

Such an object must be matched with another object even though attributes differ.

An object must be distinguished from other objects even though they might have the same attributes.

>The model must define what it means to be the same thing.

Such objects are usually used to represent core concepts in the business domain.
### Value Objects
Value objects have attributes, but can’t exist on their own. For example, the shipping address can be a value object. Often used to describe certain aspects of a domain, and which doesn't have identity.

It's highly recommended that value objects be immutable. Being immutable and having no identity means they can be shared, and for being immutable they also have data integrity. If Value Objects are shareable, they should be immutable. 

Value Objects should be kept thin and simple. Value Objects can contain other Value Objects, and they can even contain references to Entities.

Although Value Objects are used to simply contain attributes of a domain object, that does not mean that it should contain a long list with all the attributes.

Attributes can be grouped in different objects. Attributes chosen to make up a Value Object should form a conceptual whole.

![[Pasted image 20251114082952.png]]
### Services
Some aspects of the domain aren't easily mapped to objects. Usually, nouns from the ubiquitous language are objects and the verbs, associated with the corresponding nouns become part of the behavior of those objects.

But there are some behaviors which don't seem to belong to any object. Adding such behavior to an object would spoil the object, making it stand for functionality which does not belong to it.

Often this kind of behavior functions across several objects, perhaps of different classes. The best practice is to declare it as a Service.

Such an object does not have an internal state, and its purpose is to simply provide functionality for the domain. A service can group related functionality which serves the Entities and the Value Objects.

It is much better to declare the Service explicitly, because it creates a clear distinction in the domain, it encapsulates a concept. Services act as interfaces which provide operations. 

>A service is not about the object performing the service, but is related to the objects the operations are performed on/for. In this manner, a Service usually becomes a point of connection for many objects.

There are three characteristics of a Service: 
1. The operation performed by the Service refers to a domain concept which does not naturally belong to an Entity or Value Object. 
2. The operation performed refers to other objects in the domain. 
3. The operation is stateless.

While using Services, is important to keep the domain layer isolated. It is easy to get confused between services which belong to the domain layer, and those belonging to the infrastructure.

Deciding the layer a Service belongs to is difficult. If the operation performed conceptually belongs to the application layer, then the Service should be placed there. If the operation is about domain objects, and is strictly related to the domain, serving a domain need, then it should belong to the domain layer.
### Modules
Organize large and complex application models into modules. It organizes related concepts and tasks in order to reduce complexity.

It is recommended to group highly related classes into modules to provide maximum cohesion possible.	

Two of the most used are:
- **Communicational cohesion**: Achieved when parts of the module operate on the same data. It makes sense to group them, because there is a strong relationship between them.
- **Functional cohesion**: Achieved when all parts of the module work together to perform a well-defined task. This is considered the best type of cohesion.

Modules should have well defined interfaces which are accessed by other modules. Seek low coupling in the sense of concepts that can be understood and reasoned about independently of each other. It is recommended to have some flexibility, and allow the modules to evolve with the project, and should not be kept frozen. It is true that module refactoring may be more expensive than a class refactoring, but when a module design mistake is found, it is better to address it by changing the module then by finding ways around it.
### Aggregates
Large and complicated systems have countless entities and value objects. That’s why the domain model needs some kind of structure. This will put them into logical groups that will be easier to manage. 

These groups are called aggregates. They represent a collection of objects that are connected to each other, with the goal to treat them as units. Moreover, they also have an **aggregate root**. This is the only entity that any object outside of the aggregate can reference to.

A model can contain a large number of domain objects. No matter how much consideration we put in the design, it happens that many objects are associated with one another, creating a complex net of relationships. For every traversable association in the model, there has to be corresponding software mechanism which enforces it. 

The challenges of models are most often not to make them complete enough, but rather to make them as simple and understandable as possible. Most of the time it pays of to eliminate or simplify relations from the model. That's is, unless they embed deep understanding of the domain. 

The management of the relationship integrity is usually addressed at database level. While database transactions play a vital role in such operations, it's desirable to solve some of the problems related to data integrity directly in the model. It's also necessary to be able to enforce the invariants. This is difficult to realize when many objects hold references to changing data objects. Many times invariants apply to closely related objects, not just discrete ones.

An Aggregate is a group of associated objects which are considered as one unit with regard to data changes. The aggregate is demarcated by a boundary which separates the objects inside from those outside. 

Each aggregate has one root. The root is an entity, and it is the only object accessible from outside, it means that outside objects can't make changes to the objects inside the aggregate. 
The root can hold references to any of the aggregate objects, and the other objects can hold references to each other, but an outside object can hold references only to the root object.

If there are other Entities inside the boundary, the identity of those entities is **local**, making sense only inside the aggregate. 

The entity ensures data integrity and invariants by encapsulating the other objects in the aggregate. By being the root, other objects can only hold reference to it. Outside objects can only change the root or ask the root to perform some action, thus, the root is the only responsible for making changes to the aggregates. If the root is deleted or removed from memory, all the other objects from the aggregate will be deleted too.

It's possible for the root to pass transient references of internal objects to external ones, with the condition that the external objects do not hold the reference after the operation is finished.

If objects of an Aggregate are stored in the database, only the root should be obtainable through queries. The other objects should be obtained through traversal associations.

Objects inside an Aggregate should be allowed to hold references to roots of other Aggregates.

The root Entity has **global identity**, and is responsible for maintaining the invariants. Internal Entities have **local identity**.

In the example bellow, the customer is the root of the aggregate, and all the other objects are internal. If the address is needed, a copy of it can be passed to external objects.
![[Pasted image 20251116120550.png]]
#### Factories
Used to encapsulate the process of complex object creation, especially useful to create aggregates. It has no responsibility in the domain model but is still part of the domain design.

When the root of the aggregate is created, all the objects contained by the aggregate are created along with it, and all the invariants are enforced. The creation process must be atomic, this is even most true for aggregates. When the root is created, it is necessary that all object subject to invariants are created too. Otherwise, invariants cannot be enforced. 

For immutable Value Objects it means that all attributes are initialized to their valid state.

Provide an interface that encapsulates all complex assembly and that does not require the client to reference the concrete classes of the objects being instantiated.
  
When creating a Factory, we are forced to violate an object's encapsulation, which must be done carefully. Whenever something changes in the object that has an impact on construction rules or on some of the invariants, we need to make sure the Factory is updated to support the new condition.
  
Factories are tightly related to the objects they create. For aggregates, the factory will contain the rules, the constraints and the invariants which have to be enforced for the Aggregate to be valid.
Use a constructor when:
- The construction is not complicated
- The creation of an object does not involve the creation of others, and all the attributes needed are passed via the constructor.
- The client is interested in the implementation, perhaps wants to choose the Strategy used.
- The class is the type. There is no hierarchy involved, so no need to choose between a list of concrete implementations.
#### Repositories
The entire purpose of creating objects is to use them. One must hold a reference to an object in order to be able to use it. To have such a reference, the client must either create the object or obtain it from another, by traversing an existing association.

The problem is now that the client must have a reference to the root. For large applications, this becomes a problem because one must make sure the client always has a reference to the object needed, or to another which has a reference to the respective object.

Using such a rule in the design will force the objects to hold on a series of references they probably wouldn’t keep otherwise. This increases coupling, creating a series of associations which are not really needed.

It turns out that a great deal of objects can be obtained directly from the database.

This solves the problem of getting reference of objects. When a client wants to use an object, it accesses the database, retrieves the object from it and uses it. This seems like a quick and simple solution, but it has negative impacts on the design.

Databases are part of the infrastructure. A poor solution is for the client to be aware of the details needed to access a database.

Repositories are used to encapsulate all the logic needed to obtain object references.

The domain objects won't have to deal with the infrastructure to get the needed references to other objects of the domain. They'll just get them from the Repository.

The repository may store references to some of the objects. When an object is created, it may be saved in the Repository, and retrieved from there to be used later. If the client requested an object from the Repository, and the Repository doesn't have it, it may get it from the storage.

It acts as a storage place for globally accessible objects. The overall effect is that the domain models is decoupled from the need of storing objects or their references, and accessing the underlying persistence infrastructure.

![[Pasted image 20251117072053.png]]

For each type of object that needs global access, create an object that can provide the illusion of an in-memory collection of all objects of that type.

Set up access through a well-known global interface. Provide methods to add and remove objects, which will encapsulate the actual insertion or removal of data in the data store.

Provide methods that select objects based on some criteria and return fully instantiated objects or collections of objects whose attribute values meet the criteria, thereby encapsulating the actual storage and query technology.

Provide repositories only for Aggregate roots that actually need direct access. Keep the client focused on the model, delegating all object storage and access to the Repositories.

A Repository may contain detailed information used to access the infrastructure, but its interface should be simple.

Another option is to specify a selection criteria as a Specification. The Specification allows defining a more complex search criteria.

There is a relationship between Factory and Repository. They are both patterns of the model-driven design, and they both help us to manage the life cycle of domain objects.

While the Factory is concerned with the creation of objects, the Repository takes care of already existing objects.

We should not mix a Repository with a Factory.

When a new object is to be added to the Repository, it should be created first using the Factory, and then it should be given to the Repository which will store it.

Another way this is noted is that Factories are “pure domain”, but that Repositories can contain links to the infrastructure.

![[Pasted image 20251117073843.png]]
## Refactoring Towards Deeper Insight
### Bring Key Concepts Into Light
Refactoring through small steps yield incremental improvements, occasionally producing a **Breakthrough**. Each refinement clarifies the design and might reveal **implicit concepts**. When those hidden concepts prove essential, we should make them explicit through new classes, relationships, and languages terms.

Some concept types are especially valuable to make explicit:
- **Constraints**: invariants
- **Processes**: best implemented as Services or Strategies when multiple algorithms exist for a given process. Processes should only become explicit when the Ubiquitous Language names them.

Finally, **Specifications** encapsulate complex business rules that would otherwise bloat Entities or Value Objects. Those rules might seems to stretch beyond the domain level making us think it should be moved to the application layer. Actually, the rule should be encapsulated into an object of its own, which becomes the Specification of the original object, and should be kept in the domain layer.

The new object will contain a series of Boolean methods which test if a certain object is eligible for credit or not. Each method plays the role of a small test, and all methods combined give the answer to the original question.

If the business rule is not comprised in one Specification object, the corresponding code will end up being spread over a number of objects, making it inconsistent.
```go
customer := customerRepository.findCustomer(customerIdentiy)

customerEligibleForRefund := NewSpecification( 
	NewCustomerPaidHisDebtsInThePast(), 
	NewCustomerHasNoOutstandingBalances(),
)

if customerEligibleForRefund.isSatisfiedBy(customer) { 
	refundService.issueRefundTo(customer)
}
```
## Preserving Model Integrity
When multiple teams work on a project, code development is done in parallel, each team is assigned to a specific part of the model. Those parts are more or less interconnected. Different teams making changes to different parts of the model can cause the functionality to break and effectively changing the model.

The first requirement of a model is to be consistent, with invariable terms and no contradictions. The internal consistency of a model is called **unification**.

We shouldn't aim for a unified enterprise model because it's not easily accomplished, and sometimes not even worth trying. 

Instead, we should consciously divide it into several models. Several models well integrated can evolve independently as long as they obey the contract they are bound to. Each model should have a clearly delimited border, and the relationships between models should be defined with precision.
### Bounded Context
Each model has a context. When we deal with a single model, the context is implicit and we don't need to define it. When we work on a large enterprise application, we need to define the context for each model we create.

In most cases, try to put a model, elements which are related, and which form a natural concept. A model should be small enough to be assigned to one team.

The context of a model is the set of conditions which need to be applied to make sure that the terms used in the model have a specific meaning. For that we need to draw up the boundaries of its context, then keep it unified.

Explicitly set boundaries in terms of team organization, usage within specific parts of the application, and physical manifestations such as code bases and database schemas.

A Bounded Context is not a Module. Modules are used to organize the elements of a model, so Bounded Context encompasses the Module.

There is a price to pay for having multiple models. We need to define the borders and the relationships between different models. This requires extra work and design effort, and there will be perhaps some translation between different models. But this is not a very difficult task, and the benefits are worth taking the trouble.
### Context Map
Document which outlines the different Bounded Contexts and the relationships between them. Each bounded context name should be part of the Ubiquitous Language.

Everyone should know the boundaries of each context and the mapping between contexts and code.

![[Pasted image 20251118180703.png]]

We present a series of patterns which can be used to create Context Maps where contexts have clear roles and their relationships are pointed out:
- Shared Kernel and Customer-Supplier are patterns with a high degree of interaction between contexts.
- Separate Ways is a pattern used when we want the contexts to be highly independent and evolve separately.

There are another two patterns dealing with the interaction between a system and a legacy system or an external one, and they are Open Host Services and Anticorruption Layers.
#### Shared Kernel
When functional integration is limited, the overhead of continuous integration may be deemed too high. So separate Bounded Contexts might be defined and multiple teams formed.

Therefore, designate some subset of the domain model that the two teams agree to share.

Of course this includes, along with this subset of the model, the subset of code or of the database design associated with that part of the model. This explicitly shared stuff has special status, and shouldn’t be changed without consultation with the other team.

The purpose of the Shared Kernel is to reduce duplication, but still keep two separate contexts. Development on a Shared Kernel needs a lot of care. Both teams may modify the kernel code, and they have to integrate the changes. During these integrations, run the tests of both teams.

Any change of the kernel should be communicated to another team, and the teams should be informed, making them aware of the new functionality.
#### Customer-Supplier
Is a pattern that depicts two subsystems that have have a dependency relationship. One depends a lot on the other.

The contexts in which those two subsystems exist are different, and the processing result of one system is fed into the other.

They do not have a Shared Kernel, because it may not be conceptually correct to have one, or it may not even be technically possible for the two subsystems to share common code.

The customer team should present its requirements, while the supplier team should make the plans accordingly. 

While all the customer team’s requirements will have to be met in the end, the timetable for doing that is decided by the supplier team. If some requirements are considered really important, they should be implemented sooner, while other requirements might be postponed.

The customer team will also need input and knowledge to be shared by the supplier team. This process flows one way, but it is necessary in some cases.

The interface between the two subsystems needs to be precisely defined. A conformity test suite should be created and used to test at any time if the interface requirements are respected.

> This pattern works well when the teams are under the same management.
##### E-Commerce example
Let's consider two models, **web shopping** and **reporting** of an e-commerce application.

Notice that the web shopping is not at all concerned about the reporting module data but the reporting module is very much concerned about the web shopping data and actually might need some extra data to take on it's tasks.

Following that, the supplier subsystem (web-shopping) has to implement some specifications which are needed by the customer subsystem (reporting). 

Another requirement is related to the database used, more exactly its schema. Both applications will make use of the same database.

If the e-shopping subsystem was the only one to access the database, the database schema could be changed any time to reflect its needs. But the reporting subsystem needs to access the database too, so it needs some stability of its schema.

The two teams will need to communicate, probably they will have to work on the database together, and decide when the change is to be performed. This will act as a limitation for the reporting subsystem, because that team would prefer to swiftly do the change and move on with the development, instead of waiting on the e-shopping app.
### Conformist
The model Customer-Supplier only works if both teams are under the same management. If management is poor or the teams belong to different companies the Supplier has no motivation to provide for the Customer team's needs, leaving the customer team helpless. An interface tailored to the customer's needs is not in the cards.

The Customer team can only use the Supplier team's interface as part of their model, and build on their existing code provided.

When somebody providers a rich component with an interface, we can build our model including the respective component as it would be our own. If the component has a small interface, it might be better to simply create an adapter for it, and translate between our model and the component's model. This isolates our model, and we can develop it with a high degree of freedom.
#### Anticorruption Layer
There are different ways for our client system to interact with an external one, network or database. In both cases we are dealing with primitive data being transferred between the systems. The truth is that primitive data does not contain any information about the models.

We cannot take data from a database and treat it all as primitive data. There is a lot of semantics hidden behind the data. The client application cannot access the database and write to it without understanding the meaning of the data used. There is the risk for the external model to alter the client model if we allow that to happen.

We cannot ignore the interaction with the external model, but we should be careful to isolate our own model from it.

An Anticorruption Layer stands between our client and the external models.

From our model's perspective, it does not look like something foreign. But, for the external system, it talks using the external language not the client one. 

It works as a two way translator between two domains and languages. The client model remains pure and consistent without being contaminated by the external one.

Usually, the **Anticorruption Layer** should be seen as a **Service** from the client model. In the actual implementation, the Service will be done as a **Facade**. Besides that, the Anticorruption Layer will most likely need an **Adapter**. In our case the Adapter does not necessarily wrap a class, because its job is to translate between two systems.

It can also contain more than one Service. For each Service there is a corresponding Facade, and for each Facade we add an Adapter. We also need **object and data conversion**. This is done using a **Translator**. A very simple object, with little functionality, serving the basic need of data translation.

![[Pasted image 20251121160133.png]]
#### Separate Ways
Addresses the case when an enterprise application can be made up of several smaller applications which have little or nothing in common from a modeling perspective.

We should look at the requirements and see if they can be divided in two or more sets which do not have much in common. If that can be done, then we can create separate Bounded Contexts and do the modeling independently. Before going on Separate Ways we need to make sure that we won’t be coming back to an integrated system. Models developed independently are very difficult to integrate.
#### Open Host Service
When we try to integrate two subsystems, we usually create a translation layer between them. If the external subsystem turns out to be used not by one client subsystem, but by several ones, we need to create translation layers for all of them.

The solution is to see the external subsystem as a provider of services.

Define a protocol that gives access to your subsystem as a set of Services. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the protocol for that special case so that the shared protocol can stay simple and coherent.

If we can wrap a set of Services around it, then all the other subsystems will access these Services, and we won’t need any translation layer.
### Distillation
A large domain has a large model even after we have refined it and created many abstractions. It can remain big even after many refactors. In situations like this, it may be time for a distillation. The idea is to define a Core Domain which represents the essence of the domain. The byproducts of the distillation process will be Generic Subdomains which will comprise the other parts of the domain.

The Core Domain of a system depends on how we look at the system.

The Core Domain of an application may become a generic subdomain of another. It is important to correctly identify the Core, and determine the relationships it has with other parts of the model. Emphasize the most valuable and specialized concepts.

Identify cohesive subdomains that are not the motivation for your project. Factor out generic models of these subdomains and place them in separate Modules. Leave no trace of your specialties in them.

Consider off-the shelf solutions or published models for these Generic Subdomains.

There are different ways to implement a Generic Subdomain:
- **Off-the-shelf Solution**: This one has the advantage of having the entire solution already done by someone else. There is still a learning curve associated with it, and such a solution introduces some dependencies.
- **Outsourcing**: The design and implementation is given to another team, probably from another company. There is still the inconvenience of integrating the outsourced code. The interface used to communicate with the subdomain needs to be defined and communicated to the other team.
- **Existing Model**: One handy solution is to use an already created model.
- **In-House Implementation**: This solution has the advantage of achieving the best level of integration. It does mean extra effort, including the maintenance burden.
##### Distillation example
Let's consider an example of an air traffic monitoring system. 

A Flight Plan contains the designed Route the plane must follow.

The Route seems to be an ever present concept in this system. Actually, this concept is a generic one, and not an essential one. The Route concept is used in many domains, and a generic model can be designed to describe it.

The essence of the air traffic monitoring is somewhere else.

The monitoring system knows the route that the plane should follow, but it also receives input from a network of radars tracking the plane in the air. This data shows the actual path followed by the plane, and it is usually different from the prescribed one.

The system will have to compute the trajectory of the plane based on its current flight parameters, plane characteristics and weather. The trajectory is a four dimensional path which completely describes the route that the plane will travel in time.

The module which synthesizes the plane trajectory from the available data is the heart of the business system here. This should be marked out as the core domain.

---
## Domain-Driven Design (DDD)
DDD is commonly divided into **two complementary parts**:
### 1. Strategic Design
High-level view of the domain.  
Focused on **understanding the business**, not on implementation details.  
Usually done **first**.
### 2. Tactical Design
Low-level view of the domain.  
Focused on **modeling and implementing** the solution in code.  
Done **after** Strategic Design.
## Strategic Design
Strategic Design operates primarily in the **Problem Space**.  
Here we are concerned with **what the problem is**, not how we solve it.
### Problem Space Concepts
#### 1. Value
- The business value the application is meant to create.
- Answers: _Why does this system exist?_
#### 2. Knowledge Discovery
A collaborative learning process between developers and domain experts.
- **Domain Experts**
    - People with deep knowledge of the business domain.
    - Not necessarily technical.
- **Event Storming**
    - A collaborative modeling technique.
    - Focuses on **Domain Events** (things that _have happened_).
    - Similar to brainstorming, but structured around time and causality.
    **Key elements:**
    - **Domain Events**: Facts that happened in the domain.
    - **Commands**: Intent to perform an action (often lead to events).
    - **Policies / Business Rules**: Rules that react to events and trigger commands.
    - **Aggregates / Entities**: Identified later as behavior clusters.
- Conducted by **developers and business experts together**
- Goal: Achieve a **shared understanding** of the domain and problem space.
#### 3. Communication
- Achieved through **Ubiquitous Language**
- A shared language used:
    - In conversations
    - In documentation
    - In code
- Eliminates translation between business and technical terms.
#### 4. Domain Analysis
Information is clustered to identify **Subdomains**:
- **Core Subdomain**
    - The heart of the business.
    - Main source of competitive advantage.
    - Must be developed in-house.
    - Where most of the effort and expertise goes.
- **Supporting Subdomains**
    - Necessary to support the core.
    - Not a competitive advantage.
    - Can be built internally or partially outsourced.
- **Generic Subdomains**
    - Well-known, common problems.
    - Can be fully outsourced (e.g., authentication, billing, logging).
Once we understand **what problem we’re solving**, we move to the **Solution Space**.
## Tactical Design
Tactical Design operates in the **Solution Space**.  
It focuses on **how** we model and implement the domain.
### Solution Space Concepts
#### 1. Bounded Context
- A **boundary** within which:
    - A specific model applies
    - The Ubiquitous Language has a precise meaning
- Identified based on **Strategic Design insights**.
**Context interaction patterns include:**
- **Direct Invocation** (synchronous)
- **Domain Events** (asynchronous)
- **Shared Kernel** (shared model, used sparingly)
- **Anti-Corruption Layer (ACL)**
    - Translates one context’s model into another
    - Prevents model pollution
#### 2. Entities
- Have a **distinct identity** that persists over time.
- Identity matters more than attribute values.
- **Do NOT span multiple Bounded Contexts**  
#### 3. Value Objects
- Immutable
- No identity
- Equality is based on value
- Used as building blocks for entities.
#### 4. Aggregates
- A **consistency boundary**.
- A cluster of entities and value objects with:
    - One **Aggregate Root**
    - All access from outside goes through the root.
- Enforces invariants.
- Usually defines a **transaction boundary**.
```go
type Delivery struct {
 	// fields 
}  

type Drone struct {
	// fields 
}

type DeliveryAggregate struct {
	// Aggregate Root 	
	Delivery Delivery 	
	drone    Drone 
}
// Methods on the aggregate enforce rules and coordinate changes.`
```
> Rule: Only the Aggregate Root can be referenced from outside.
#### 5. Domain Events
- Represent something that _has happened_ in the domain.
- Used for:
    - Decoupling bounded contexts
    - Asynchronous communication
- Expressed in the Ubiquitous Language.
#### 6. Services
Services are **stateless** and represent operations that don’t naturally belong to an entity or value object.
- **Domain Services**
    - Pure domain logic
    - Use only domain concepts
    - Often coordinate multiple aggregates
- **Application Services**
    - Orchestrate use cases
    - Handle concerns like:
        - Transactions
        - Authentication
        - Emailing
        - Calling repositories
    - Do not contain domain rules.
## Anemic vs Rich Domain Model
### Anemic Model
- Data-only structures
- Business logic lives elsewhere
- Often resembles CRUD + DTOs
```go
type Drone struct {
 	id string 
 	model string
 	status string
 	batteryLevel int 
}
```
**Problems:**
- No invariants
- No encapsulation
- Hard to maintain business rules
### Rich Domain Model
- Behavior and data live together
- Invariants enforced inside the model
- Uses meaningful types
```go
type Drone struct {
 	id string
 	model string
 	status Status
 	batteryLevel BatteryLevel 
}
func NewDrone(
	id, model string,
	status Status,
	batteryLevel BatteryLevel
) (Drone, error) {
	if model == "" {
	 	return Drone{}, errors.New("model is required")
	}
	return Drone{
		id: id,
		model: model,
		status: status,
		batteryLevel: batteryLevel,
	}, nil }
```
**Benefits:**
- Business rules are explicit
- Safer and more expressive code
- Easier evolution of the domain

---
## Notes
- Subdomain: A domain consists of several subdomains that refer to different parts of the business logic.
Advantages:
- Simpler communication: Thanks to the Ubiquitous Language, communication between developers and teams becomes much easier.
- Keep in mind some of the pitfalls of domain modeling:
	1) Stay hands-on. Modelers need to code.
	2) Focus on concrete scenarios. Abstract thinking has to be anchored in concrete cases.
	3) Don't try to apply DDD to everything. Draw a context map and decide on where you will make a push for DDD and where you will not. And then don't worry about it outside those boundaries.
	4) Experiment a lot and expect to make lots of mistakes. Modeling is a creative process.

Downsides:
- Deep domain knowledge is needed. Even for the most technologically advanced teams working on development, there has to be at least one domain specialist on the team who understands the precise characteristics of the subject area that’s the center of the application. Sometimes there’s a need for several team members who thoroughly know the domain to incorporate in the development team.
- It might not work best for highly-technical projects. Domain-driven design is perfect for applications that have complex business logic. However, it might not be the best solution for applications with minor domain complexity but high technical complexity. Applications with great technical complexity can be very challenging for business-oriented domain experts. This could cause many limitations that might not be solvable for all team members.