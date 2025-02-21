# Kafka
Event streaming is the practice of capturing data in real-time from event 
sources like databases, sensors, mobile devices, cloud services, and 
software applications in the form of streams of events. storing, 
manipulating, processing, and reacting to the event streams in real-time as
well as retrospectivel; and routing the event streams to different 
destinations.
It ensures a continuous flow  and interpretation of data so that storing, 
manipulating, processing, and reacting to the event streams in real-time as
well as retrospectivel; and routing the event streams to different 
destinations.

Kafka is a distributed system consisting of servers and clients that 
communicate via a high-performance TCP network protocol.

Servers: Kafka is run as a cluster of one or more servers that can span 
multiple datacenters or cloud regions. Some of these servers form the 
storage layers, called the brokers. Other servers run Kafka Connect to 
continuously import and export data as event streams to integrate Kafka 
with your existing systems as well as other Kafka clusters.
If any of its servers fails, the other servers will take over their work to
ensure continuous operations without any data loss.

Clients: Applications that read, write, and process streams of events in 
parallel, at scale and in a fault-tolerant manner.

Event: It records the fact that "something happened" in the world. An event
has a key, value, timestamp, and optional metadata headers.

Producers: Client applications that publish events to Kafka.

Consumers: Client applications that subscribe to these events.

Topics: Similar to a folder in a filesystem, and the events are the files 
in that folder. Topics are always multi-producer and multi-subscriber.
Events in a topic can be read as often as needed, events arent' deleted 
after consumption, you can define for how long Kafka should retain your 
events. Kafka performance is effectively constant with respect to data 
size, so storing data for a long time is perfeclty fine.

Partitions: Topics are partitioned, meaning a topic is spread over a number
of "buckets" located on different Kafka brokers.
When a new event is published to a topic, it's actually appended to one of 
the topic's partitions. Events with the same event key are written to the 
same partition. Consumers of a given topic-partition will always read that 
partition's events in exatcly the same order as they were written.

Replication: Every topic can be replicated across geo-regions or 
datacenters.

Default Port: 9092
