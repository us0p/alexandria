Command Query Responsibility Segregation - CQRS
Is an architectural pattern that is used to separate the responsibilities 
of reading and writing data in a software system. In a CQRS architecture, 
the system is divided into two separate parts: the command side and the 
query side.
The command side is responsible for processing commands and updating the 
system’s state, while the query side is responsible for reading the current
state of the system and returning the results to the client. The command 
and query sides can use different data models, storage mechanisms, and even
different technologies.
If separate read and write databases are used, they must be kept in sync. 
Typically this is accomplished by having the write model publish an event 
whenever it updates the database. Since message brokers and databases 
usually cannot be enlisted into a single distributed transaction, there can
be challenges in guaranteeing consistency when updating the database and 
publishing events.

Command x Queries
- Commands should be task-based, rather than data centric. ("Book hotel 
  room", not "set ReservationStatus to Reserved"). The other part of 
  that is to look at modifying the business logic processing those commands
  to be successful more frequently. In that manner, the cause for 
  server-side command failures can be narrowed to race conditions, and
  even those can sometimes be addressed with some more data and logic 
  (putting a guest on a waiting list).
- Commands may be placed on a queue for asynchronous processing, rather 
  than being processed synchronously.
- Queries never modify the database. A query returns a DTO that does not 
  encapsulate any domain knowledge.

Context and problem
In traditional architectures, the same data model is used to query and 
update a database. That's simple and works well for basic CRUD operations.
In more complex applications, however, this approach can become unwieldy. 
For example, on the read side, the application may perform many different 
queries, returning data transfer objects (DTOs) with different shapes. 
Object mapping can become complicated. On the write side, the model may 
implement complex validation and business logic. As a result, you can end 
up with an overly complex model that does too much.
Read and write workloads are often asymmetrical, with very different 
performance and scale requirements.

Benefits:
- Independent scaling: CQRS allows the read and write workloads to scale 
  independently, and may result in fewer lock contentions.
- Optimized data schemas: The read side can use a schema that is optimized
  for queries, while the write side uses a schema that is optimized for 
  updates.
- Security: It's easier to ensure that only the right domain entities are 
  performing writes on the data.
- Separation of concerns: Segregating the read and write sides can result 
  in models that are more maintainable and flexible. Most of the complex 
  business logic goes into the write model. The read model can be 
  relatively simple.
- Simpler queries: By storing a materialized view in the read database, the
  application can avoid complex joins when querying.

Drawbacks:
- Complexity: The basic idea of CQRS is simple. But it can lead to a more 
  complex application design, especially if they include the Event Sourcing
  pattern.
- Messaging: Although CQRS does not require messaging, it's common to use 
  messaging to process commands and publish update events. In that case, 
  the application must handle message failures or duplicate messages. 
  Priority Queues are usually used to deal with commands having different 
  priorities.
- Eventual consistency: If you separate the read and write databases, the 
  read data may be stale. The read model store must be updated to reflect 
  changes to the write model store, and it can be difficult to detect when
  a user has issued a request based on stale read data.

When to use CQRS
- Has a high demand for data consumption.
- Performance of data reads must be tuned separately from the performance 
  of data writes, especially when the number of reads is much greater than
  the number of writes.
- Integration with other systems, especially in combination with event 
  sourcing, where the temporal failure of one subsystem shouldn’t affect 
  the availability of the others.
- You can afford stale data.

Command Bus
Provides a centralized infrastructure for routing commands to their 
corresponding handlers.

This patterns has three different classes:
1. Command: Is a class that only contains the needed data to execute the 
   command. Validations are done in this class and its objects are 
   immutable.
2. CommandHandler: Execute the behaviour when taking a specific Command 
   object as input. It should not be doing any domain logic itself.
   The relationship between Command and CommandHandler is one-to-one.
3. CommandBus: After receiving a Command object, CommandBus will route it
   to the suitable CommandHandler.

Benefits:
    - Separation of concerns: It allows for the separation of the code that
      performs an action from the code that requests the action, making the
      code more maintainable and easier to test.
    - Architectural boundary: It provides a clear and consistent structure 
      for the application, making it easier to understand and maintain.
    - Extendable: It can be extended with new functionality, such as 
      wrapping commands in database transactions.
    - Scalability: It can handle a large number of commands and handlers, 
      making it suitable for large-scale applications.

Drawbacks:
    - Complexity: It can add complexity to the application, especially if 
      the commands and handlers are not properly designed.
    - Over-engineering: It may be overkill for trivial use cases, and may 
      not be necessary for small applications.
    - Command complexity: Commands can grow to enormous complexity, just 
      like all objects, and may require careful design and management.
