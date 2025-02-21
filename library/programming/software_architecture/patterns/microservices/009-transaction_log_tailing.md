Transaction Log Tailing

Problem
How to publish messages/events into the outbox in the database to the 
message broker?

Solution
Tail the database transaction log and publish each message/event inserted 
into the outbox to the message broker.

Benefits
- No 2PC.
- Guaranteed to be accurate.1

Drawbacks
- Relatively obscure although becoming increasing common.
- Requires database specific solutions.
- Tricky to avoid duplicate publishing.
