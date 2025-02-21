## Tasks
A task carries a Docker container and the commands to run inside the 
container. It is the atomic scheduling unit of swarm. Manager nodes assign 
tasks to worker nodes according to the number of replicas set in the 
service scale. Once a task is assigned to a node, it cannot move to another
node. It can only run on the assigned node or fail.

A task is the atomic unit of scheduling within a swarm. When you declare a 
desired service state by creating or updating a service, the orchestrator 
realizes the desired state by scheduling tasks.

For instance, you define a service that instructs the orchestrator to keep 
three instances of an HTTP listener running at all times. The orchestrator 
responds by creating three tasks. Each task is a container spawned by the 
scheduler. The container is the instantiation of the task.

A task is a one-directional mechanism. It progresses monotonically through 
a series of states: assigned, prepared, running, etc.
If an HTTP listener task subsequently fails its health check or crashes, 
the orchestrator creates a new replica task that spawns a new container.

!["service and task generation"](https://docs.docker.com/engine/swarm/images/service-lifecycle.webp)

Each task has a life cycle, with states like `NEW`, `PENDING`, and 
`COMPLETE`.
Tasks are execution units that run once to completion. When a task stops, 
it isn't executed again, but a new task may take its place.

Tasks advance through a number of states until they complete or fail. Tasks
are initialized in the `NEW` state. The task progresses forward through a 
number of state, and its state doesn't go backward.
