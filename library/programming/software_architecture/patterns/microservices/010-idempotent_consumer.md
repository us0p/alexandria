Idempotent Consumer
In an enterprise application, it’s usually a good idea to use a message 
broker that guarantees at-least once delivery. At-least once delivery 
guarantees that a message broker will deliver a message to a consumer even 
if errors occur. One side-effect, however, is that the consumer can be 
invoked repeatedly for the same message. Consequently, a consumer must be 
idempotent: the outcome of processing the same message repeatedly must be 
the same as processing the message once. If a consumer is not idempotent, 
multiple invocations can cause bugs.

Problem
How does a message consumer handle duplicate messages correctly?

Solution
Implement an idempotent consumer, which is a message consumer that can 
handle duplicate messages correctly. Some consumers are naturally 
idempotent. Others must track the messages that they have processed in 
order to detect and discard duplicates.
You can make a consumer idempotent by recording in the database the IDs of 
the messages that it has processed successfully. When processing a message,
a consumer can detect and discard duplicates by querying the database. 
There are a couple of different places to store the message IDs. One option
is for the consumer to use a separate PROCESSED_MESSAGES table. The other 
option is for the consumer to store the IDs in the business entities that 
it creates or updates.
