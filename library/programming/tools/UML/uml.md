# Unified Modeling Language
Standardized visual modeling language used in software engineering to provide general-purpose, and a intuitive way to visualize the design of a system.

## Structural Diagrams
### Composite Structure Diagram
Similar to the class diagram, and it's a kind of component diagram used mainly in micro-level system modeling. But, it depicts individual parts instead of whole classes.

It's a type of static structure diagram that shows the internal structure of a class and interactions that this structure makes possible.

This diagram can include internal paths, ports, through which the paths can communicate with each other, or, through which the class instances the class instances can communicate with various parts, and with the outside world, as well as connect us between paths and ports.

Composite Structure Diagram is a set of interrelated elements that interacts at runtime to achieve a specific goal. Each element has a dedicated role in this collaboration.

![[Pasted image 20251124171959.png]]
### Deployment Diagram
Helps to model the physical aspect of an OO software system. It's a block diagram that shows the system architecture as deployment or distribution of software artifacts.

Artifacts represents specific elements in the physical world that are the results of the development process.

The diagram simulates their runtime configuration in a static view and visualize the distribution of artifacts in the application. In most cases this involves simulating hardware configurations along with the software components that host them.

![[Pasted image 20251124170614.png]]
### Package Diagram
Structural diagram that shows packages and dependencies between them.

It allows us to display different views of the system.

For example, it's easy to simulate a layered application.

![[Pasted image 20251124171203.png]]
### Profile Diagram
Allow us to create domain and platform specific stereotypes and find relationships between them.

We can create stereotypes by drawing shapes of stereotypes and linking them to composition or generalization through a resource oriented interface.

We can also define and visualize stereotype values.

![[Pasted image 20251124172350.png]]
### Class Diagram
Central modeling technique that is used in almost all object-oriented methods. It describes the types of objects in the system and different kinds of static relationships that exist between them. The three most important types of relationships in class diagrams are:
- **Association**: Represents relationships between instances of types.
- **Inheritance**: Corresponds directly to inheritance in OOD.
- **Aggregation**: Form of object composition in OOD.

![[Pasted image 20251124165700.png]]
### Object Diagram
Instance of the class diagram. It shows a detailed snapshot of the system's state at a particular point in time.

The difference is that the class diagram is an abstract model of classes and their relationships. However, object diagram represents a instance at a specific moment which is concrete in nature.

The use of object diagram is rather limited namely to show examples of data structures.

![[Pasted image 20251124170937.png]]
### Component Diagram
Illustrate how components are put together to form large components of software systems and illustrates the architecture of software components and dependencies between then.

These software components can include:
- **Runtime Component**
- **Executable Components**
- **Source Code Components**

![[Pasted image 20251124170202.png]]
## Behavioral Diagrams
### Activity Diagram
Graphical representations of workflows of stepwise activities and actions with the support of choice, iteration and concurrency.

They describe the control flow of the target system such as exploring complex business rules and operations as well as describing the use cases and business processes.

In UML activity diagram are meant for modeling both computational and organizational processes.

![[Pasted image 20251124173115.png]]
### Use Case Diagram
Describes the functional requirements of a system in terms of use cases.

In essence it's a model of intended functionality of the system (Use cases), and, its environment (actors).

Use cases allows us to link what we need from the system with how the system meets those needs.

![[Pasted image 20251124172829.png]]
### State Machine Diagram
It's a type of diagram used to describe system behavior which is based on David Harrell's concept of state diagrams.

It depicts permitted states and transitions as well as events that affect those transitions.

It helps to visualize the entire life cycle of objects and thus helps to better understand state-based systems.

![[Pasted image 20251124173410.png]]
### Interaction Diagrams
#### Sequence Diagram
Models the interaction of object based on a time sequence. It shows how objects interact with each other in a particular use case.

![[Pasted image 20251124173605.png]]
#### Communication Diagram**
Used to model the dynamic behavior of a use case.

When compared to sequence diagram, communication diagram focuses more on showing object collaborations rather than the time sequence. In fact, communication diagrams and sequence diagrams are semantically equivalent and one can be generated from another.

![[Pasted image 20251124174012.png]]
#### Interaction Overview Diagram**
Focuses on the overview of the flow of control of the interactions.

This is a a variant of activity diagram where the nodes depicted are the interactions or interaction occurrences.

It describes the interactions in which messages and lifelines are hidden. We can link up the real diagrams and achieve a high degree of navigation between diagrams within an interaction of your diagram.

![[Pasted image 20251124174246.png]]
![[Pasted image 20251124174306.png]]
#### Timing Diagram**
Shows the behavior of the object or objects at a given time period. In fact, this is a special form of a sequence diagram and the differences between them are that the axes are swapped, so that the time increases from left to right and the lifelines are displayed in separate compartments, arranged vertically.

![[Pasted image 20251124174510.png]]
![[Pasted image 20251124174526.png]]