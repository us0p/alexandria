Event Sourcing
Event sourcing is an architectural pattern that is used to build systems 
that need to maintain a history of all the changes that have occurred over 
time. This pattern stores all changes to the system’s state as a sequence 
of events, rather than just the current state.
In Event sourcing, all changes to the state of the system are treated as 
events, and these events are stored in an append-only log, also known as an
event store. The current state of the system can be reconstructed from the 
event log at any given point in time by replaying the events from the log.

Problem
Most applications work with data, and the typical approach is for the 
application to maintain the current state of the data by updating it as 
users work with it. For example, in the traditional CRUD model a typical 
data process is to read data from the store, make some modifications to 
it, and update the current state of the data with the new values—often by 
using transactions that lock the data.
The CRUD approach has some limitations:
- CRUD systems perform update operations directly against a data store. 
  These operations can slow down performance and responsiveness and can 
  limit scalability, due to the processing overhead it requires.
- In a collaborative domain with many concurrent users, data update 
  conflicts are more likely because the update operations take place on a 
  single item of data.
- Unless there's another auditing mechanism that records the details of 
  each operation in a separate log, history is lost.

Solution
The Event Sourcing pattern defines an approach to handling operations on 
data that's driven by a sequence of events, each of which is recorded in an
append-only store. Application code sends a series of events that 
imperatively describe each action that has occurred on the data to the 
event store, where they're persisted. Each event represents a set of 
changes to the data.
The events are persisted in an event store that acts as the authoritative 
data source about the current state of the data. The event store typically 
publishes these events so that consumers can be notified and can handle 
them if needed.
Notice that the application code that generates the events is decoupled 
from the systems that subscribe to the events.
At any point, it's possible for applications to read the history of events.
You can then use it to materialize the current state of an entity by 
playing back and consuming all the events that are related to that entity.

Advantages
- Events are immutable and can be stored using an append-only operation. 
  The user interface, workflow, or process that initiated an event can 
  continue, and tasks that handle the events can run in the background. 
  This process, combined with the fact that there's no contention during 
  the processing of transactions, can vastly improve performance and 
  scalability for applications.
- Events are simple objects that describe some action that occurred, 
  together with any associated data that's required to describe the action 
  represented by the event. Events don't directly update a data store. 
  They're simply recorded for handling at the appropriate time. Using 
  events can simplify implementation and management.
- Events typically have meaning for a domain expert, whereas 
  object-relational impedance mismatch can make complex database tables 
  hard to understand. Tables are artificial constructs that represent the 
  current state of the system, not the events that occurred.
- Event sourcing can help prevent concurrent updates from causing conflicts
  because it avoids the requirement to directly update objects in the data 
  store. However, the domain model must still be designed to protect itself
  from requests that might result in an inconsistent state.
- The append-only storage of events provides an audit trail that can be 
  used to monitor actions taken against a data store. It can regenerate the
  current state as materialized views or projections by replaying the 
  events at any time, and it can assist in testing and debugging the 
  system. In addition, the requirement to use compensating events to cancel
  changes can provide a history of changes that were reversed. The list of 
  events can also be used to analyze application performance and to detect 
  user behavior trends.
- The event store raises events, and tasks perform operations in response 
  to those events. This decoupling of the tasks from the events provides 
  flexibility and extensibility. Tasks know about the type of event and the
  event data, but not about the operation that triggered the event. In 
  addition, multiple tasks can handle each event. This enables easy 
  integration with other services and systems that only listen for new 
  events raised by the event store.

Issues and considerations
- The system will only be eventually consistent when creating materialized 
  views or generating projections of data by replaying events.
- The event store is the permanent source of information, and so the event 
  data should never be updated. The only way to update an entity to undo a 
  change is to add a compensating event to the event store. If the format 
  (rather than the data) of the persisted events needs to change, perhaps 
  during a migration, it can be difficult to combine existing events in the
  store with the new version. It might be necessary to iterate through all 
  the events making changes so they're compliant with the new format, or 
  add new events that use the new format. Consider using a version stamp on
  each version of the event schema to maintain both the old and the new 
  event formats.
- The consistency of events in the event store is vital, as is the order of 
  events that affect a specific entity. Adding a timestamp to every event 
  can help to avoid issues. Another common practice is to annotate each 
  event resulting from a request with an incremental identifier.
- There's no standard approach, or existing mechanisms such as SQL 
  queries, for reading the events to obtain information.
- The length of each event stream affects managing and updating the system.
  If the streams are large, consider creating snapshots at specific 
  intervals such as a specified number of events.
- Even though event sourcing minimizes the chance of conflicting updates to
  the data, the application must still be able to deal with inconsistencies
  that result from eventual consistency and the lack of transactions.
- Event publication might be at least once, and so consumers of the events 
  must be idempotent. 
- The event storage selected needs to support the event load generated by 
  your application. Be mindful of scenarios where the processing of one 
  event involves the creation of one or more new events since this can 
  cause an infinite loop.

When to use
- When you want to capture intent, purpose, or reason in the data.
- When it's vital to minimize or completely avoid the occurrence of 
  conflicting updates to data.
- When you want to record events that occur, to replay them to restore the 
  state of a system, to roll back changes, or to keep a history and audit 
  log. For example, when a task involves multiple steps, you might need to 
  execute actions to revert updates and then replay some steps to bring the
  data back into a consistent state.
- When you use events. It's a natural feature of the operation of the 
  application, and it requires little extra development or implementation 
  effort.
- When you need to decouple the process of inputting, or updating data from
  the tasks required to apply these actions.

When not to use
- Small or simple domains, systems that have little or no business logic, 
  or nondomain systems that naturally work well with traditional CRUD data 
  management mechanisms.
- Systems where consistency and real-time updates to the views of the data 
  are required.
- Systems where audit trails, history, and capabilities to roll back and 
  replay actions aren't required.
- Systems where there's only a low occurrence of conflicting updates to the
  underlying data. For example, systems that predominantly add data rather 
  than updating it.
