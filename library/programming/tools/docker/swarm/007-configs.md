## Configs
Docker swarm service configs allow you to store non-sensitive information, 
such as configuration files, outside a service's image or running 
containers. This allows you to keep your images as generic as possible, 
without the need to bind-mount configuration files into the containers or 
use environment variables.

Configs operate in a similar way to secrets, except that they are not 
encrypted at rest and are mounted directly into the container's filesystem 
without the use of RAM disks. Configs can be added or removed from a 
service at any time, and services can share a config. You can even use 
configs in conjunction with environment variables or labels, for maximum 
flexibility. Config values can be generic strings or binary content 
(up to 500 kb in size).
Docker configs are only available to swarm services, not to standalone 
containers.

## How Docker manages configs
When you add a config to the swarm, Docker sends the config to the swarm 
manager over a mutual TLS connection. The config is stored in the Raft log,
which is encrypted. The entire Raft log is replicated across the other 
managers, ensuring the same high availability guarantees for configs as for
the rest of the swarm management data.
When you grant a newly-created or running service access to a config, the 
config is mounted as a file in the container. The location of the mount 
point within the container defaults to `/<config-name>` in Linux 
containers. In Windows containers, configs are all mounted into 
`C:\ProgramData\Docker\configs` and symbolic links are created to the 
desired location, which defaults to `C:\<config-name>`.

You can update a service to grant it access to additional configs or revoke
its access to a given config at any time.

A node only has access to configs if the node is a swarm manager or if it 
is running service tasks which have been granted access to the config. When
a container task stops running, the configs shared to it are unmounted from
the in-memory filesystem for that container and flushed from the node's 
memory.

If a node loses connectivity to the swarm while it is running a task 
container with access to a config, the task container still has access to 
its configs, but cannot receive updates until the node reconnects to the 
swarm.

You can add or inspect an individual config at any time, or list all 
configs. You cannot remove a config that a running service is using.
