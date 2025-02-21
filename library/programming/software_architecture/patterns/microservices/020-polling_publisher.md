Polling Publisher

Problem
How to publish messages/events into the outbox in the database to the 
message broker?

Solution
Publish messages by polling the database’s outbox table.

Benefits
- Works with any SQL database.

Drawbacks
- Tricky to publish events in order.
- Not all NoSQL databases support this pattern.
