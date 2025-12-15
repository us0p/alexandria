# Clean Architecture

!["clean architecture diagram"](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

## TLDR
**Goal:**
- Separation of concerns by dividing software into layers.

**Produce systems that are:**
- Independent of any external agency
- Testable

**Commonly splited around four areas of software:**
1. Entities - Enterprise Business Rules
2. Use cases (Interactor, Commands, Service Layer) - Application Business 
   Rules
3. Interface Adapters - Controllers, Gateways, Presenters
4. Frameworks and Drivers - DB, Devices, Web, UI, External Interfaces

**Dependency rule:**
- Source code dependencies always point inwards.
- The outermost circle is low level concrete details.
- The inner most circle is the most general.
- Nothing in an inner circle can know anything at all about something in an outer circle. 
- The name of something declared in an outer circle must not be mentioned  by the code in an inner circle.
- Data formats used in an outer circle should not be used by an inner  circle
- Inner circles are policies, they define interfaces which must be implemented by outer circles.

**Flow of data:**
Data that crosses the boundaries are simple data structures. You can use basic structs, simple DTO's, or simply arguments in function calls. The important thing is that isolated, simple, data structures are passed across the boundaries. Don’t pass Entities or Database rows.
## Getting deeper
### What is Clean Architecture
It's a mix of ideas regarding the architecture of software. It's built upon:
- Hexagonal Architecture
- Onion Architecture
- Screaming Architecture
- DCI
- BCE

Though these architectures all vary somewhat in their details, they are very similar. They all have the same objective, which is the separation of concerns. They all achieve this separation by dividing the software into layers.

Each of these architectures produce systems that are:
- Independent of Frameworks: The architecture does not depend on the existence of some library. This allows you to use such frameworks as tools, rather than having to cram your system into their limited constraints.
- Testable: The business rules can be tested without the UI, Database, Web Server, or any other external element.
- Independent of UI: The UI can change easily, without changing the rest of the system.
- Independent of Database: Your business rules are not bound to the database.
- Independent of any external agency: In fact your business rules simply don’t know anything at all about the outside world.

!["clean architecture diagram"](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

Note that there's no rule that says you must always have just these four circles. However the **dependency rule** always applies. Source code dependencies always point inwards.

As you move inwards the level of abstraction increases. The outermost circle is low level concrete detail.  As you move inwards the software grows more abstract, and encapsulates higher level policies. The inner most circle is the most general.
## The Dependency Rule
The concentric circles represent different areas of software. In general, the further in you go, the higher level the software becomes. The outer circles are mechanisms. The inner circles are policies.

This rule says that source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle.
In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle. That includes, functions, classes. variables, or any other named software entity.

By the same token, data formats used in an outer circle should not be used by an inner circle, especially if those formats are generate by a framework in an outer circle.
## Entities - Enterprise Business Rules
Entities encapsulate Enterprise wide business rules. An entity can be used by many different applications in the enterprise.

They encapsulate the most general and high-level rules. They are the least likely to change when something external changes.They are designed to evolve with the business logic.

They are, high-level business objects or domain objects which represent the core application logic, regardless of how or where it's used. 
For example, in an e-commerce application, entities could be `Order`, `Product`, or `User`.

Common responsibilities:
- Model domain objects in a data storage agnostic way.
- Perform validation to ensure that the object isn't in a invalid state.
- Validation is usually made in the constructor by throwing an error if the provided state is invalid, this create less responsibility on the developer to remember to call validation methods. You must consider the impact of this practice, for example, in your repositories, your data is going to be valid during entity construction?
- Objects contain behaviors that are common to all use cases across the system.
## Use Cases - Application Business Rules
The software in this layer contains application specific business rules. It encapsulates and implements all of the use cases of the system.

These use cases orchestrate the flow of data to and from the entities, and direct those entities to use their enterprise wide business rules to achieve the goals of the use case.

It's expected that changes to the operation of the application will affect the use-cases and therefore the software in this layer.

They define and implement specific actions or workflows that the application can perform. 

Coordinate interactions between entities, data sources, and external systems.

Common responsibilities:
- Interact with entities to call methods to enforce business rules.
- Define workflows to combine and sequence operations to accomplish specific tasks.
- Prepare data for external layers to transform or structure data for output, often using DTOs.
- Each use case handles one specific workflow or action.
- Perform validation on data to ensure the data is valid for the given use case.

For example, an user login use case, uses the `User` entity to validate username and password, then applies the use case business rule and generates a JWT and returns the token or an error message.

**A use case must be a class with only one exec() method?**
- It's not a rule rather a recommendation.
- The class name is more objective and less generic.
- If the use case don't focus on one task usually end up being a wrapper of the repository.
- In a big code base the developer must find the right method in the use case.
- It's common for use cases to only wrap a repository function if there aren't any application rules for a specific use case.
## Interface Adapters - Controllers, Gateways, Presenters
The software in this layer is a set of adapters that convert data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the Database or the Web.

The Presenters, Views, and Controllers all belong in here. The models are likely just data structures that are passed from the controllers to the use cases, and then back from the use cases to the presenters and views.

Also in this layer is any other adapter necessary to convert data from some external form, such as an external service, to the internal form used by the use cases and entities.

**Controllers:** Handle user input, select the appropriate use case to execute based on the user input by extracting the input data. It only delegates to the use case without validating. Should be focused on request handling.
  
**Gateways:** Responsible for accessing external data sources, such as databases or web services. It's an adapter between a data source and a particular domain object (e.g. Repository).
- Repositories interfaces are defined in the domain layer and implemented in the framework and drivers layer. Some implementation allows repositories to return entities to reduce conversion between objects.

**Presenters:** Responsible for rendering data in the user interface. Ensure consistent response structure by formatting the output from the Use Case into a structure suitable for the delivery mechanism (Controller or View). usually sits between use case return value and controller return  data, it transforms raw data into a response-friendly format by adapting  the data returned from the use case for the designed output. 
Good to use when multiple delivery mechanisms need the same data format.

## DB, Devices, Web, UI, External Interfaces - Frameworks and Drivers
The outermost layer is generally composed of frameworks and tools such as the Database, the Web Framework, etc. Generally you don’t write much code in this layer other than glue code that communicates to the next circle inwards.

This is where you will implements the interfaces defined by inner circles.
## Crossing Boundaries
The communication and relation between boundaries is achieved by the use of **dependency inversion** as an inner circle can know nothing about an outer circle, an interface is created in the innermost circle and implemented in  the outermost circle.
## What data crosses the boundaries
Typically the data that crosses the boundaries is simple data structures. You can use basic structs or simple DTO's if you like. Or the data can simply be arguments in function calls.

The important thing is that isolated, simple, data structures are passed across the boundaries. We 
don’t want to cheat and pass Entities or Database rows.

For example, many database frameworks return a convenient data format in response to a query. We might call this a `RowStructure`.
We don’t want to pass that row structure inwards across a boundary. That would violate The Dependency Rule because it would force an inner circle to know something about an outer circle.
## Entity x Model
Entity represents the core business logic and data for a domain object (note the relation with DDD), residing in the domain layer.

Model is a data structure that represents data in a specific format for presentation or storage, often adapting the entity data to suit external needs like the UI or database, and typically located in the data access layer.

Essentially, an entity is the "pure" business concept, while a model is a tailored representation of that concept for a specific context.
## Plain Old Java/JavaScript Object - POJO
Is a simple object that doesn't adhere to any specific framework or  requirement. Typically represents and encapsulates data. No need to  implement interfaces or extend classes. May contain business logic but  better to keep as simple as possible.

Can be defined in any layer as it's  just a data container but it's better to define it in the domain layer to  enable a simple data structure as communication amongst the application.

Using POJOS creates the need to convert entities to POJOs which can increase complexity but it allows for clearer contracts.

As Randy Stafford said in P of EAA “Don't underestimate the cost of using DTOs.... It's significant, and it's painful - perhaps second only to the cost and pain of object-relational mapping”.
## Data Access Object - DAO
Provides an abstract interface for accessing data from a persistent storage mechanism like a database. It encapsulates data access logic.

**DAO x Repository**
  - DAO is an abstraction of data persistence.
  - Repository is an abstraction of a collection of objects, it has a narrower interface.
  - A Repository can be implemented using a DAO but a DAO shouldn't be implemented by using a Repository.
  - A method like Update is appropriate on a DAO, but not in a Repository.
  - DAO doesn't restrict you to store data of the same type, thus you can easily have a DAO that deals with related objects.
  - Repositories handle only one type of objects.
## Data Transfer Object - DTO
  - An object that carries data between processes.
  - Useful when you want to transfer data across different layers of an  application or over the network.
  - Are often immutable.
  - Should be used when you have a significant mismatch between the model  in your presentation layer and the underlying domain.
  - The whole purpose is to shift data in expensive remote calls.
  - Using it for more than network communication can lead to conversions  from DTO to Domain objects and back which increases complexity.
  - It doesn't include business logic, but it can include some methods to  format data like serialization and desserialization mechanisms for  transferring data over the wire.
  - Often requires conversion from and to POJOs or entities, which can be a costly process.
  - Most commonly used in the services layer in a N-tier application to  transfer data between itself and the UI layer, the service layer must  control what data leaves the application layer.
  - Some DTOs belong in the interface adapters layer when they are specific to UI representation, framework, external services, or if the response  format is different from the use case (e.g. must be snake_case instead of camelCase).
## DTO x POJO
|                 | POJO                                          | DTO                                                             |
| --------------- | --------------------------------------------- | --------------------------------------------------------------- |
| Purpose         | Temporary structure to hold data              | Defined explicitly for data transfer                            |
| Layers          | Domain or Use Case                            | Use Case or Interface                                           |
| Dependency      | No external dependencies                      | Might be used with libraries                                    |
| Behavior        | Usually has no additional logic               | May contain formatting, transformation, serialization, etc      |
| Reusability     | Typically ad-hoc and speficic to the use case | Explicitly structure to match API contracts or external systems |
| Maintainability | Can be easily modified within the use case    | Acts as a stable contract, ensuring API consistency             |

## Comon Folder Structure
  - Domain
    - Entities
    - Exceptions
    - Repositories (interfaces)
    - ?POJOs
  - Application
    - Interfaces
    - UseCases
        - Entity1
            - ...usecases
        - Entity2
            - ...usecases
    - ?DTOs
  - Adapters
    - Controllers
    - Middlewares
    - ViewModels
    - ?DTOs
  - Drivers
    - Databases
        - Repositories (impl)
    - Web APIs
