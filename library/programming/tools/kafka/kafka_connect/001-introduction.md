# Kafka Connect
Free, open-source component of Apache Kafka that serves as a centralized 
data hub for simple data integration between databases, key-value stores, 
search indexes, and file systems. You can use Kafka Connect to stream data 
between Apache Kafka and other data systems and quickly create connectors 
that move large data sets in and out of Kafka.

## Benefits
- Data-centric pipeline
- Flexibility and scalability
- Reusability and extensibility

It can ingest entire data sets into Kafka topics. An export connector, for 
example, can deliver data from Kafka topics into secondary indexes like 
Elasticsearch.
You can deploy it as a standalone process that runs jobs on a single 
machine (for example, log collection), or as a distributed, scalable, 
fault-tolerant service supporting an entire organization.

## Connectors
High level abstraction that coordinates data streaming by managing tasks.
Connectors in Kafka Connect define where data should be copied to and from.
A connector instance is a logical job that is responsible for managing the 
copying of data between Kafka and another system. All of the classes tha 
timplement or are used by a connector are defined in a 
**connector plugin**.
It's possible to write a new connector plugin from scratch. At a high 
level, a developer who wishes to write a new connector plugin should keep 
to the following workflow.
!["Kafka Connect plugin workflow"](https://docs.confluent.io/platform/current/_images/connector-model-simple.png)

It includeds two types of connectors:
- **Source connector**: ingest data sets and stream table updates to Kafka topics.
- **Sink connector**: deliver data from Kafka topics to secondary indexes.

## Tasks
Implementation of how data is copied to or from Kafka.
Are the main actor in the data model for Connect. Each connector instance 
coordinates a set of tasks that copy data. By allowing the connector to 
break a single job into many tasks, Kafka Connect provides built-in support
for parallelism and scalable data copying with minimal configuration. Tasks
themselves have no state stored within them. Rather a task's state is 
stored in special topics in Kafka and manage by the associated connector. 
Tasks my be started, stopped, or restarted at any time to provide a 
resilient and scalable data pipeline.

**Task rebalancing**
When a connector is first submitted to the cluster, the workers rebalance 
the full set of connectors in the cluster and their tasksk so that each 
worker has approximately the same amount of work. This rebalancing 
procedure is also used when connectors increase or decrease the number of 
tasksk they require, or when a connector's configuration is changed. When a
worker fails, tasks are rebalanced across the active workers. When a task 
fails, no rebalance is triggered, as a task failure is considered an 
exceptional case. As such, failed tasks are not restarted by the framework 
and should be restarted using the REST API.
!["Connect tasks rebalancing framework"](https://docs.confluent.io/platform/current/_images/task-failover.png)

## Workers
The running processes that execute connectors and tasks.
Connectors and tasks are logical units of work and must be scheduled to 
execute in a process. Kafka Connect calls these processes workers and has 
two types of workers:

**Standalone workers** 
The simplest mode, where a single process is responsible for executing all 
connectors and tasks. Since is a single process, it requires minimal 
configuration. This mode is convenient for development, and in certain 
situations where only one process makes sense, such as collecting logs from
a host. However, because there is ony a single process, it also has more 
limited functionality, scalability is limited to the single process and 
there is no fault tolerance beyond any monitoring you add to the single 
process.

**Distributed workers**
It provides scalability and automatic fault tolerance for Kafka Connect. In
distributed mode, you start many worker processes using the same 
`group.id` and they coordinate to schedule executioning of connectors and 
tasks across all available workers.
If you add a worker, shut down a worker, or a worker fails unexpectedly, 
the rest of the workers acknowledge this and coordinate to redistribute 
connectors and tasks across the updated set of available workers. Note the 
similarity to consumer group rebalance. Behind the scenes, connect workers
use consumer groups to coordinate and rebalance.
Note that all workers with the same `group.id` will be in the same connect 
cluster.
!["Distrubuted workers"](https://docs.confluent.io/platform/current/_images/worker-model-basics.png)

## Converters
Code used to translate data between Connect and the system sending or 
receiving data.
Converters are required to have a Kafka Connect deployment support a 
particular data format when writing to, or reading from Kafka. Tasks use 
converters to change the format of data from bytes to a Connect internal 
data format and vice versa.
Converters are decoupled from connectors themselves to allow for the reuse 
of converters between connectors.

## Transforms
Simple logic to alter each message produced by or sent to a connector.
Connectors can be configured with transformations to make simple and 
lightweight modifications to individual messages.
This can be conveninent for minor data adjustments and event routing, and 
many transformations can be chained together in the connector 
configuration.
A transform is a simple function that accepts one record as an input and 
outputs a modified record. All transforms provided by Kafka Connect perform
simple but commonly useful modifications. You can implement the 
Transformation interface with your custom logic, package them as a Kafka 
Connect plugin, and use them with any connector.
When transforms are used with a source connector, Kafka Connect passes each
source record produced by the connector through the first transformation, 
which makes its modifications and outputs a new source record. This updated
source record is then passed to the next transform in the chain, which 
generates a new modified source record. This continues for the remaining 
transforms. The final updated source record is converted to the binary form
and written to Kafka.

## Dead Letter Queue
How Connect handles connector errors
Dead Letter Queues (DLQs) are only applicable for sink connectors.
An invalid record may occur for a number of reasons. When an invalid record
can't be processed by the sink connector, the error is handled based on the
connector `errors.tolerance` configuration property.
An error-handling feature is available that will route all invalid records 
to a special topic and report the error. This topic contains a DLQ of 
records that could not be processed by the sink connector.
