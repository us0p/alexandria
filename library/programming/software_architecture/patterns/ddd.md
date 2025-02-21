Domain Driven Design
Is an architectural pattern that is used to design software systems based 
on the core business domain and business entities.
It provides several advantages over other architectural patterns, such as 
alignment with business goals and objectives, improved communication 
between domain experts and developers, a clear and expressive model of the
business domain and improved scalability and maintainability. It’s 
implemented using a set of principles and patterns such as strategic 
design, subdomains, bounded context, entities, value objects, aggregate, 
and repository.
DDD is not a technology, rather it introduces terms, practices and 
principles to support decision making in complex business domains
- The primary focus of the project is the core domain and domain logic.
- Complex designs are based on models of the domain.
- Collaboration between technical and domain experts is crucial to creating
  an application model that will solve particular domain problems.

In DDD, it’s important to pay attention to the following terms:
- Domain logic: Most commonly, it’s referred to as the business logic. This
  is where your business rules define the way data gets created, stored, 
  and modified.
- Domain model: A system of abstractions that describes selected aspects of
  a domain and can be used to solve problems related to that domain.
- Subdomain: A domain consists of several subdomains that refer to 
  different parts of the business logic.
- Bounded context: This is where you implement the code, after you’ve 
  defined the domain and the subdomains. Bounded contexts actually 
  represent boundaries in which a certain subdomain is defined and 
  applicable.
- The Ubiquitous Language: The Ubiquitous Language is a methodology that 
  refers to the same language domain experts and developers use when they 
  talk about the domain they are working on.
  All the terms in the ubiquitous language are structured around the domain
  model.
- Value objects and aggregates: Value objects have attributes, but can’t 
  exist on their own. For example, the shipping address can be a value 
  object. 
- Entities: Are objects that are defined by its identity and not by their 
  attributes. Such an object must be matched with another object even 
  though attributes differ. An object must be distinguished from other 
  objects even though they might have the same attributes. Such objects are
  usually used to represent core concepts in the business domain.
- Aggregates: Large and complicated systems have countless entities and value 
  objects. That’s why the domain model needs some kind of structure. This 
  will put them into logical groups that will be easier to manage. These 
  groups are called aggregates. They represent a collection of objects that
  are connected to each other, with the goal to treat them as units. 
  Moreover, they also have an aggregate root. This is the only entity that 
  any object outside of the aggregate can reference to.
- Domain service: is an object that implements business logic or business 
  rules related to domain objects. It is a stateless, operation-centric 
  class that encapsulates domain logic or operations that don't naturally 
  fit within the boundaries of an Entity or a Value Object.
  They can be used by Application Services and other Domain Services, but 
  not directly by the presentation layer.

Advantages:
- Simpler communication: Thanks to the Ubiquitous Language, communication 
  between developers and teams becomes much easier.

Downsides:
- Deep domain knowledge is needed. Even for the most technologically 
  advanced teams working on development, there has to be at least one 
  domain specialist on the team who understands the precise 
  characteristics of the subject area that’s the center of the application.
  Sometimes there’s a need for several team members who thoroughly know 
  the domain to incorporate in the development team.
- It might not work best for highly-technical projects. Domain-driven 
  design is perfect for applications that have complex business logic. 
  However, it might not be the best solution for applications with minor 
  domain complexity but high technical complexity. Applications with great
  technical complexity can be very challenging for business-oriented domain
  experts. This could cause many limitations that might not be solvable for
  all team members.

Repository Pattern
Mediates between the domain and data mapping layers using a collection-like
interface for accessing domain objects.
It isolates domain objects from details of the database access code.
A Repository mediates between the domain and data mapping layers, acting 
like an in-memory domain object collection.
It's used to abstract querying data from the domain model which otherwise 
would make value objects and aggregates meaningless, making it impossible 
for these objects to enforce the rules of the domain model.
Without it domain logic moves into queries and application layer code, and 
the entities and value objects become mere data containers.

---

# Domain Driven Design (DDD)
When complexity gets out of hand, the software can no longer be understood
well enought to be easily changed or extended.  
the most significant complexity of many applications is not technical. It 
is in the domain itself, the activity or business of the user. When this 
domain complexity is not dealt with in the design, it won’t matter that the
infrastructural technology is well-conceived.  
  
The premise of this pattern is that:
1. It should be applicable in projects where the primary focus should be on
   the domain and domain logic.
2. Complex domain designs should be based on a model.

Domain-driven design is a way of thinking and a set of priorities, aimed at
accelerating software projects that have to deal with complicated domains.  

To apply *DDD* it's required two practices:
1. Iterative development
2. Close relationship between developers and domain experts.

A model represents some aspect of reality or of an idea that is of interes.
It is an interpretation of reality that abstracts the aspects relevant to 
solving the problem at hand and ignores extraneous detail.  
Every software program relates to some activity or interest of its user. 
That subject area to which the user applies the program is the “domain” of
the software.  
Software domains usually have little to do with computers, though there are
exceptions.  
  
To create valuable software, we must bring to bear a body of knowledge 
related to the activities the software will be involved in.  
This is when a development team can use modeling to wrestle with that 
overload.  
An appropriate model makes sense of information and brings it to bear on a
problem.  
The domain model is not a particular diagram; it is the idea that the 
diagram is intended to convey.  
Domain modeling is not a matter of making as “realistic” a model as 
possible.  

## Utility of a model in DDD
There are three basic uses that determine the choice of a model:
1. The model dictates the form of the design of the heart of the software.
   - This binding of model and implementation helps maintenance and 
     continuing development because code can be interpreted based on 
     understanding the model.
2. The model is the backbone of a language used by all team members and 
   domain experts.
   - Because of the binding of model and implementation, developers can 
     talk about the program in this language.
3. The model is the team's agreed-upon way of structuring domain knowledge,
   and distinguishin the elements of most interest.
   - A model captures how we choose to thinkg about the domain as we select 
     terms, break down concepts, and relate them.
   - The shared language allows effective collaboration to wrestle 
     information into this form.
   - The binding of model and implementation ensures means that experience 
     with early versions of the software are also valid feedback into the 
     modeling process.

## The centrality of Domain Functionality
The heart of software is its ability to solve domain related problems for the user.
All other features, bital through they may be, support this basic purpose.

## Crunching Knowledge
> You should probably learn a little about UML diagrams.

Draw diagrams for the users as you discuss the things they want the software to do.
They must correct you.
The experts must agree over a terminology and technical opinions.
focus in one particular feature at the time for your model.
in the beginning the model shouldn't describe the entire behaviour, but the
specific feature at hand.
It should map how the software should work using terms and concepts agreed with the experts.

With the model defined you should start to bind the model to the 
implementation and write some code
which should follow the rules, names and conventions specified by the 
model.
By interative developing these concepts in a concrete implementation, 
you'll build your knowledge in the domain
and the model discussions will become more productive as the experts will 
be able to see how you incorporated the newly aquired knowled into the 
software.
and also will provide concrete feedback so them can evaluate their own 
thoughts.

In the end, your model will embedded knowledge about the domain relevant to the problem being solved.
it should consolidate many synonyms and slight variations in descriptions.
exclude hundreds of facts that the experts understand but are not directly relevant.
A software specialist should be able to look at the diagrams and in minutes start to get a grip on what the software was about.

As new features are needed, you should walk through scenarios of interactions of the objects with the experts team.
Is the model objects can't carry you through an important scenario, brainstorm new ones or change the old to refine the model and the code.

## Important topics
1. Binding model and implementation as soon as possible.
2. Cultivate a language based on the model.
3. knowledge rich model, the objects must have behaviour and enforce rules, the model can't be just a data schema, it must capture knowledge of various kinds.
4. The model must be distilled, important concepts are added as it becomes more complete but equally important.
   concepts must be drpped when they don't prove useful or central.
   unneeded concept tied to needed ones should lead to a new model that distinguishes the essential concept so that the other can be dropped.
5. knowledge crunching, the language combined with diagrams and brainstorms will turn the model discussions into laboratories of the model.

Effective domain modelers are knowledge crunchers. They take a torrent of information and probe for the
relevant trickle. They try one organizing idea after another, searching for the simple view that makes sense
of the mass. Many models are tried and rejected or transformed. Success comes in an emerging set of
abstract concepts that make sense of all the detail. This distillation is a rigorous expression of the particular
knowledge that has been found most relevant.

Knowledge crunching is not a solitary activity. A team of developers and domain experts collaborate,
typically led by developers. Together they draw in information and crunch it into a useful form. The raw
material comes from the minds of domain experts, from users of existing systems, from the prior
experience of the technical team with a related legacy system or another project in the same domain.

projects have iteration, but don’t build up knowledge because they don’t abstract. They get the
experts to describe a desired feature and they go build it. They show the experts the result and ask them
what to do next.

if programmers are not interested in the domain, they only learn what the
application should do, not the principles behind it. Useful software can be built that way, but the project
will never gain the kind of leverage where powerful new features unfold as corollaries to older features.

Useful software can be built that way, but the project
will never gain the kind of leverage where powerful new features unfold as corollaries to older features.
That shallowness of knowledge produces software that does a basic job but lacks a deep connection to the
domain expert’s way of thinking.

-> page 20, "Continuous Learning"
