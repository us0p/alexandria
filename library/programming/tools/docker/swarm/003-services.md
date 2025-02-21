## Services
A service is the definition of the tasks to execute on the manager or 
worker nodes. It's the central structure of the swarm system and the 
primary root of user interaction with the swarm.

When you create a service, you specify which container image to use and 
which commands to execute inside running containers.

Swarm services use a declarative model, which means that you define the 
desired state of the service, and rely upon Docker to maintain this state. 
The state includes information such as (but not limited to):
- The image name and tag the service containers should run
- How many containers participate in the service
- Whether any ports are exposed to clients outside the swarm
- Whether the service should start automatically when Docker starts
- The specific behavior that happens when the service is restarted (such as
  whether a rolling restart is used)

## Pending services
Created services do not always run right away. A service can be in a 
pending state if its image is unavailable, if no node meets the 
requirements you configure for the service, or for other reasons.

## Note about service images
When you create a service, the image's tag is resolved to the specific 
digest the tag points to at the time of service creation. Worker nodes for 
that service use that specific digest forever unless the service is 
explicitly updated. This feature is particularly important if you do use 
often-changing tags such as `latest`, because it ensures that all service 
tasks use the same version of the image.
Note that if a service is created with a diferent version in `latest`, 
you'll have services tasks running different versions.

If the manager can't resolve the tag to a digest, each worker node is 
responsible for resolving the tag to a digest, and different nodes may use 
different versions of the image. If this happens, a warning like the 
following is logged

```bash
unable to pin image <IMAGE-NAME> to digest: <REASON>
```

After you create a service, its image is never updated unless you 
explicitly run docker service update with the `--image` flag as described 
below. Other update operations such as scaling the service, adding or 
removing networks or volumes, renaming the service, or any other type of 
update operation do not update the service's image.

## Updating a service
When you update a service, Docker stops its containers and restarts them 
with the new configuration.

A service may be configured in such a way that no node currently in the 
swarm can run its tasks. In this case, the service remains in state 
`pending`.

If you only intention is to prevent a service from being deployed, scale 
the service to 0.

## Service rolling update
You configure the rolling update policy at service deployment time.
By default, when an update to an individual task returns a state of 
RUNNING, the scheduler schedules another task to update until all tasks are
updated. If at any time during an update a task returns FAILED, the 
scheduler pauses the update.
The scheduler applies rolling updates as follows by default:
- Stop the first task.
- Schedule update for the stopped task.
- Start the container for the updated task.
- If the update to a task returns RUNNING, wait for the specified delay 
  period then start the next task.
- If, at any time during the update, a task returns FAILED, pause the 
  update.

## Control service placement
Swarm services provide a few different ways for you to control scale and 
placement of services on different nodes.
- You can specify whether the service needs to run a specific number of 
  replicas or should run globally on every worker node.
- You can configure the service's CPU or memory requirements, and the 
  service only runs on nodes which can meet those requirements.
- Placement constraints let you configure the service to run only on nodes 
  with specific (arbitrary) metadata set, and cause the deployment to fail 
  if appropriate nodes do not exist. For instance, you can specify that 
  your service should only run on nodes where an arbitrary label 
  pci_compliant is set to true.
- Placement preferences let you apply an arbitrary label with a range of 
  values to each node, and spread your service's tasks across those nodes 
  using an algorithm. Currently, the only supported algorithm is spread, 
  which tries to place them evenly.

## Replicated or global services
Swarm mode has two types of services: replicated and global. For replicated
services, you specify the number of replica tasks for the swarm manager to 
schedule onto available nodes. For global services, the scheduler places 
one task on each available node that meets the service's placement 
constraints and resource requirements.
You control the type of service using the `--mode` flag. If you don't 
specify a mode, the service defaults to replicated.

## Automatically roll back if an update fails
You can configure a service in such a way that if an update to the service 
causes redeployment to fail, the service can automatically roll back to the
previous configuration. This helps protect service availability.

## Data volumes
Volumes can be created before deploying a service, or if they don't exist 
on a particular host when a task is scheduled there, they are created 
automatically according to the volume specification on the service.

## Bind mounts
The file system path must exist before the swarm initializes the container 
for the task.
Bind mounts can be useful but they can also cause problems. In most cases, 
it is recommended that you architect your application such that mounting 
paths from the host is unnecessary. The main risks include the following:
- If you bind mount a host path into your service’s containers, the path 
  must exist on every swarm node.
- The Docker swarm mode scheduler may reschedule your running service 
  containers at any time if they become unhealthy or unreachable.
- Host bind mounts are non-portable. When you use bind mounts, there is no 
  guarantee that your application runs the same way in development as it 
  does in production.
