Is a way o f thinking and a set of priorities, aimed at accelerating software projects that have to deal with complicated domains.
premise:
- for most software projects, the primary focus should be on the domain and domain logic.
- complex domain designs should be based on a model.
it's oriented toward Agile Development Processes. It assumes a couple of process practices:
- Iterative development.
- A close relationship between developers and domain experts. DDD crunches knowledge into a model that reflects deep insight into the domain and a focus on the key concepts. This is a collaboration between those who know the domain and those who know how to build software. This collaboration must continue throughout the project's life.
>Valuable models do not emerge immediately. They require a deep understanding of the domain. Which comes from diving in, implementing an initial design based on a probably naive model, and then transforming it again and again.

Every model represents some aspect of reality. It is a simplification. It's an interpretation of reality that abstracts the aspects relevant to solving the problem at hand and ignores extra details.

Every software program relates to some activity or interest of its user. That subject area to which the user applies the program is the "domain" of the software.

To create  valuable software, we must bring to bear a body of knowledge related to the activities the software will be involved in. The amount of knowledge can be overwhelming. This is when a team can use modeling to wrestle with that overload.

Domain modeling is not a matter of making as "realistic" a model as possible. Nor is it just the construction of a software mechanism that gives the necessary results. It is more like movie making, loosely representing reality to a particular purpose. Just as a moviemaker selects aspects of experience and presents them in an idiosyncratic way to tell a story or make a point, a domain model is chosen for its utility.

There are three basic uses that determine the choice of a model:
1. The model dictates the form of the design of the heart of the software.a It is the intimate link between the model and the implementation that makes the model relevant. This binding of model and implementation also helps maintenance and continuing development because the code can be interpreted based on understanding the model.
2. The model is the backbone of a language used by all team members. Developers can communicate with domain experts without translation.
3. The model is distilled knowledge. The team's agreed-upon way of structuring domain knowledge and distinguishing the elements of most interest. A model captures how we choose to think about the domain. The shared language allows effective collaboration of developers and domain experts to wrestle information into this form.

>Most talented developers do not have much interest in learning about the specific domain they are working in, much less making a major commitment to expand their domain modeling skill. Technical people enjoy quantifiable technical problems that exercise their technical skill. The domain is messy and demands a lot of complicated new knowledge that doesn't seem to develop a computer scientist's capabilities.

Often having the clients tell exactly what the software should do is a bad idea. Clients are professional of other areas their software ideas are not as accurate as one of a developer. Often not leading to any productivity increase.

The construction of a model is based on the interaction between domain experts and developers and is done by constantly corrections made by the experts until the developer starts to learn. You should strive to reduce collisions and ambiguities in their terminologies and differences between their technical opinions so they can learn and explain things more precisely and consistently as well.
You limit yourselves and explore one feature at the time.
The construction of the model is a process of brainstorming and refining; questioning and explaining.

- Bind model and implementation as soon as possible.
- Cultivate a language based on the model. Terms taken straight out of the model, organized into sentences consistent with the structure of the model test the viability of the model immediately upon reaching the ears.
- Knowledge rich model. The objects should have behavior and enforced rules. The model ins't a data schema, it should solve a problem and capture knowledge of various kinds.
- Important concepts should be added to the model as it become more complete and concepts should be dropped when they don't prove useful or central. If a unneeded concept was tied to one that is needed, a new model should be found that distinguishes the essential concept so that the other could be dropped.
- Knowledge crunching. The langue combined with sketches and brainstorming turn the discussions into laboratories of the model, experiments can be exercised, tried and judged.

Effective domain modelers search for the simple view that makes sense of the mass. Many models are tried and rejected or transformed. Success comes in an emerging set of abstract concepts that make sense of all the detail.

>Some teams get the experts to describe a desired feature and they go build it. They show the experts the results and ask them what to do next. If the programmers practice refactoring they can keep the software clean enough to continue extending it, but if programmers are not interested in the domain, they only learn what the application should do, not the principles behind it. Useful software can be built that way, but the project will never gain the kind of leverage where powerful new features unfold as corollaries to older features.

If you abstract and develop a model only with technical expertise, without collaboration with domain experts, the concepts are naive. It produces software that does a basic job but lacks a deep connection to the domain expert's way of thinking.

Because the domain experts are feeding into it, it reflects deep knowledge of the business and those abstractions are true business principles.

When we set out to write software, we never know enough. Knowledge on the project is fragmented. Domains that seems less technically daunting can be deceiving -- we don't realize how much we don't know. This leas us to make false assumptions.

Highly productive teams consciously grow their knowledge, practicing continuous learning. This includes technical knowledge, along with general domain modeling. But it also includes serious learning about the specific domain they are working in.

Knowledge is accumulated in the minds of the core team.

The model is the set of concepts built up in the heads of people on the project, with terms and relationships that reflect domain insight.

On a project without a common language, developers have to translate for domain experts. Domain experts translate between developers and other domain experts. Translation is always inaccurate and hides disconnects in understanding between the domain experts and developers.

A model can be viewed as a language. The vocabulary includes the names of classes and prominent operations. The model provides the means to discuss rules that have been made explicit in the model. It can be supplemented with terms from high-level organizing principles imposed on the model. Finally, this language is enriched with the names of patterns the team commonly applies to the domain model.

A prerequisite for an adequate model is commitment by the team to rely on that model. Persistent use of the language will force its weakness into the open. As gaps are found, new words will enter the discussion. With a commitment to the model-based language, these changes will be recognized as changes in the domain model and will lead to updates of class diagrams and renaming of classes and methods in the code.

Use the model as the backbone of a language. Commit the team to using that language relentlessly in all communication within the team and in the code. Use the same language in diagrams, writing, and, especially speech.

Domain experts object to terms or structures that are awkward or inadequate to convey domain understanding, while developers watch for ambiguity or inconsistency that will trip up design.

The language is the primary carrier of the aspects of design that don't appear in code.
Large-scale structures that organize the whole system, and bounded contexts that define the relationships of different systems and models.

Play with the model as you talk about the system. Describe scenarios out loud using the elements and interactions of the model, combining concepts in ways allowed by the model. Find easier ways to say what you need to say and then take those new ideas back down to the diagrams and code.

By using this language in discussions with domain experts, you quickly discover areas where your language is inadequate for their needs, or seems wrong to them. You also find areas where the precision of the domain language exposes contradictions or vagueness in thinking.

The domain model will typically derive from the domain expert's jargon, but will be "cleaned up", to have sharper, narrower, definitions. The domain experts can and should learn these modified definitions, and should object if these definitions diverge from the meanings in the field.

Multiplicity of language if often necessary, but the division should never be between the domain experts and the developers.

Simple, informal UML diagrams can anchor a discussion. Sketch a diagram of three to five objects central to the issue at hand, and everyone can stay focused.
The trouble comes when people feel compelled to convey the whole model or design through UML.

Diagrams are a means of communication and explanation, and they facilitate brainstorming. They serve these ends best if they are minimal. Comprehensive diagrams of the entire object model fail to communicate or explain. They overwhelm the reader with detail and they lack meaning.
They show design constraints, but they are not design specifications in every detail. They represent the skeletons of ideas.

Always remember that the model is not the diagram. The diagram's purpose is to help communicate and explain the model.

A document shouldn't try to do what the code already does well. The code already supplies the detail. It already is the ultimately exact specification of program behavior.
It falls to other documents to illuminate meaning, to give insight into large-scale structures, and to focus attention on core elements. Written documents should compliment the code and the verbal communication.

The greatest value of a design document is to explain the concepts of the model, perhaps its intended style of use, and to help in navigating the detail of the code.

These diagrams can be somewhat casual, even hand-drawn. In addition to saving labor, hand-drawn diagrams have the advantage of feeling casual and temporary.

A document must be involved in project activities. The document must be written in the language people are **currently** speaking on the project which must reflect the language embedded in the code.

Keeping a document up to date through sheer will and discipline waster effort, if the document isn't playing an important role.

As the domain model comes to reflect the most relevant knowledge of the business, application requirements become scenarios within that model, and the **ubiquitous language** can be used to describe such a scenario in terms that directly connect to the **model-driven design**.

Specifications can often be simpler, since they do not have to convey business knowledge that is behind the model.

Documents should be minimal and focused on complimenting code and conversation.

One model should underlie implementation, design, and team communication.

One particular reason other models are needed is scope. The technical models that drives the software development process must be strictly pared down to the necessary minimum to fulfill its functions. An explanatory model can include aspects of the domain that provide context that clarifies the more narrowly scoped model.

Explanatory models provide the freedom to create much more communicative styles tailored to a particular topic.
There's no need for these to be object models, and it's generally best they not be. Avoid UML.
While there often is some correspondence between an explanatory model and the model that drives design, it will seldom be exact.

What good is a model on paper unless it directly aids the development of running software?

Some development processes create an "analysis model", quite distinct from the design, and usually developed by different people. It's called this way because it is the product of analyzing the business domain to organize its concepts without any consideration of the part it will play in a software system. A design should be create later and should have only a loose correspondence to the analysis model.
An analysis model is not created with design issues in mind and therefore is likely to be quite impractical for those needs.
Developers are forced to reconceptualize the domain on their own, and there is no guarantee that the insights gained by the analyst and embedded in the model will be retained. And maintaining any mapping between the design and the loosely connected model is a labor that is not cost effective.
The pure analysis model falls short of its primary goal of understanding the domain, because crucial discoveries always emerge during the design/implementation effort as very specific problems are encountered that were not anticipated.
Pure analysis models often get abandoned soon after coding starts.

If the design, or some central part of it, does not map to the conceptual domain model, that model is of little value, and the correctness of the software is suspect. At the same time, complex mappings between models and design functions are difficult to understand, and, in practice, impossible to maintain as the design changes. A deadly divide opens between analysis and design so that insight gained in each of those activities does not feed into the other.

Model-driven design discards the dichotomy of analysis model versus design to search out a single model that serves both purposes. Setting aside purely technical issues, each object in the design plays a conceptual role described in the model. This requires us to be more demanding of the chosen model, since it must fulfill two quite different objectives.

This can't be at the cost of a weakened analysis. Nor can we accept clumsy designs. It demands a model that works as both analysis and design. When the model doesn't seem to be practical for implementation, we must search for a new one. When the model doesn't faithfully express the key concepts of the domain, we must search for a new one. The modeling and design process then becomes a single iterative loop.

The design should retain as many of the concepts of the model, as literally as possible, while the model should be chosen such that a practical design model can be created that corresponds to it.

Trying to create in the UI an illusion of a model other than the domain model will cause confusion unless the illusion is perfect.

When a modeler is separated from the implementation process, he or she never acquires, or quickly loses, a feel for the constraints of implementation. The basic constraint of MDD, that the model supports an effective implementation and abstract key insights into the domain, is half gone, and the resulting models will be impractical. Meanwhile, if the people who write the code do not feel responsible for the model, or don't understand how to make the model work for an application, then the model has nothing to do with the software. If developers don't realize that changing the code changes the model, then their refactoring will weaken the model rather than strengthen it. Finally, the knowledge and skills of experienced designers won't be transferred to other developers if the division of labor prevents the kind of collaboration that conveys the subtleties of coding a MDD.

The effectiveness of an overall design is very sensitive to the quality and consistency of the fine-grained design and implementation decisions.
With MDD, a portion of the code is an expression of the model, so changing that code changes the model.

Any technical person contributing to the model must spend some time touching the code, whatever primary role he or she plays on the project. Anyone responsible for changing code must learn to express a model through the code. Every developer must be involved in some level of discussion about the model and have contact with domain experts.

DDD puts a model to work to solve problems for an application. Through knowledge crunching, a team distills a torrent of chaotic information into a practical model. A MDD intimately connects the model and the implementation. The Ubiquitous Language is the channel for all that information to flow between developers, domain experts and the software.

Elaborate models only cut through complexity if care is taken with the fundamentals, producing detailed elements that can be confidently combined.

![[Pasted image 20250328062939.png]]

The part of software that specifically solves problems from the domain usually constitutes only a small portion of the software of a system. To apply our best thinking, we need to be able to look at the elements of our model and see them as a system. This requires decoupling the domain objects from other function of the system so they are not lost in the mass and do domain concepts are not blurred and confused with concepts related to software technology.

To achieve this level of decoupling we'll be considering a **layered architecture**. The essential principle is that an element of a **layer** has dependencies only on other elements in the same layer or on elements of the layers "beneath" it.

We'll be considering these four layers:
- **User interface/Presentation Layer**
- **Application Layer**
- **Domain Layer/Model Layer**
- **Infrastructure Layer**

The crucial point is the separation of the **domain layer** that enables **MDD**.

The infrastructure layer does not initiate action in the domain layer. Such technical capabilities are most often offered as **services**. This decoupling gives some extra versatility. The message-sending interface might be connected to an email or fax sender or whatever is available. The main benefit is that the application layer keep focused on its job, knowing **when** to send a message, but not burdened with **how**.

Not all infrastructure is in the form of services callable from the higher layers. Some technical components are designed to directly support the basic functions of other layers, such as domain objects in the domain layer and provide mechanisms for them to relate.
## Architectural Frameworks
The best architectural frameworks solve complex technical problems while allowing the domain developer to concentrate on expressing a model. But they can easily get in the way, either by making too many assumptions that constrain domain design choices or by making the implementation so heavyweight that developers slow down.

When applying a framework, the team needs to keep focused on the goal of an implementation that expresses a domain model and uses it to solve important problems. The team must seek ways of employing the framework to those ends. This may mean not using all the framework's features. A lot of the downside of frameworks can be avoided by selectively applying them to solve difficult problems without looking for a one-size-fits-all solution. This keeps the implementation less coupled to the framework, which gives some flexibility in later design decisions, but more importantly, since many of the current frameworks are very complicated to use, keeps the business objects readable and expressive.
## The domain layer is where the model lives
DDD requires the domain layer to exist. The domain model is a set of concepts. The domain layer is the manifestation of that model and all directly related design elements. The design and implementation of business logic constitute the domain layer. In a MDD, the software constructs of the domain layer will mirror the model concepts.
Isolating the domain implementation is a prerequisite for a ddd.
## Smart UI anti-pattern
Is an alternate, mutually exclusive branch in the road, incompatible with the approach of DDD.

If a project needs to deliver simple functionality, dominated by data-entry and display with few business rules and staff is not composed of advanced object modelers.
The staff will have a difficult learning curve. The overhead of managing infrastructure and layers make very simple tasks take longer. Simple projects come with short time lines and modest expectations. And in the end, if they do surmount these challenges, they will have produced a simple system. Rich capabilities were never requested.

The point is that  the approach advocated in the rest of this book pays off for ambitious projects, and requires strong skill. And not all projects are ambitious or can muster those skills.

Therefore, when circumstances warrant.

Put all the business logic into the user interface. Chop the application into small functions and implement them as separate user interfaces, embedding the business rules into them. Use a database as a shared repository of the data. Use the most automated UI building and visual programming tools available.

The gospel is that domain and UI should be separate. In fact, it is difficult to apply any of the methods discussed later in this book without that separation. Therefore, this might be considered an "anti-pattern", but it isn't always, and it is important to understand why we want to separate application from domain, even when we might not want to.

Advantages:
- Productivity is high and immediate for simple applications.
- Less capable developers can work this way with little training.
- Even deficiencies in requirements-analysis can be overcome by releasing a prototype to users and then quickly changing the product to fit their requests.
- Applications are decoupled from each other so that delivery of small modules can be planned relatively accurately, and expansion of the system with additional, simple behavior is easy.
- When applications are handed off, maintenance programmers will be able to quickly redo portions they can't figure out since the effects should be localized to the UI being worked on.
Disadvantages:
- There is no reuse of behavior and no abstraction of the business problem.
- Rapid prototyping and iteration reach a natural limit because the lack of abstraction limits refactoring options.
- Complexity buries you quickly, so the growth path is strictly toward additional simple applications. There is no graceful path to richer behavior.

If this pattern is applied conciously, a team can avoid taking on a great deal of overhead that is required to attempt other approaches. 
The bottom line is this: *If the architecture isolates the domain related code in a way that allows a cohesive domain design loosely coupled to the rest of the system then it can probably support DDD. Other development styles have their place, but you must accept varying limits on complexity and flexibility.*
## Associations
A model that shows an association between a customer and a sales representative corresponds to two things:
- It abstracts a relationship developers deemed relevant between two real people.
- Corresponds to an object pointer between two objects, or some comparable implementation.

In real life, there are lots of many-to-many associations, and many are naturally bi-directional. These general associations complicate implementation and maintenance. A generic many-to-many relationship is uncommunicative as well as difficult to implement.
There are at least three ways of making associations more tractable:
- Imposition of a traversal direction.
- Addition of a qualifier, effectively reducing multiplicity.
- Elimination of non-essential associations.

It is important to constrain relationship as much as possible. Bi-directional associations are tricky to implement, and they also mean that both objects can only be understood together. When application requirements do not require traversal in both directions, adding a traversal direction reduces interdependence and simplifies the design.

Very often, deeper understanding leads to a "qualified" relationship (an extra rule that must be met for a relationship).
For example, a country has had many presidents (one-to-many) but each president has had only one president  at a time (qualified relationship).

The ultimate simplification is to eliminate an association altogether.
## Entities
Object modeling tends to lead us to focus on the attributes of an object, but the fundamental concept of an ENTITY is an abstract continuity threading through a life cycle and even multiple forms.

Some objects are not defined primarily by their attributes. They represent a thread of identity that runs through time and often across distinct representations. Sometimes such an object must be matched with another object even though attributes differ. An object must be distinguished from other objects even though they might have the same attributes. Mistaken identity can lead to data corruption.

An object defined primarily by it identity is called an "ENTITY". They have life cycles that can radically change their form and content, while a thread of continuity must be maintained. Their identities must be defined so that they can be effectively tracked. Their class definitions, responsibilities, attributes and associations should revolve around who they are, rather than the particular attributes they carry. Even for Entities that don't transform radically or have such complicated life cycles.

Keep the class definition simple and focused on life cycle continuity and identity. Define a means of distinguishing each object regardless of its form or history. Be alert to requirement to match by attributes. The model must define what it means to be the same thing.
## Modeling Entities
Entities are defined by their identities. Attributes tare attached and change. Therefore, strip the Entity object's definition down to the most intrinsic characteristics, particularly those that identify it, or are commonly used to find or match it. Separate other characteristics into other objects associated with the core Entity.

Attributes associated with identity stay with the Entity.