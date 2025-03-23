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