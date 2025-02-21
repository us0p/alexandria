## Deploy a stack to a swarm
You can deploy a complete application stack to the swarm. The stack 
description is in the form of a Compose file.

> The `docker stack deploy` command uses the legacy compose file version 3 
format, used by Compose V1.

["Compose file version 3 format"](https://github.com/docker/compose/tree/v1/docs)

Keep in mind that all `docker stack` and `docker service` commands must be 
run from a manager node.

create the stack with `docker stack deploy`

To update a stack, make changes to your Compose file, then re-run 

```bash
docker stack deploy -c <new-compose-file> <stack-name>
```

If you use a new config in that file, your services start using them. Keep 
in mind that configurations are immutable, so you can't change the file for
an existing service. Instead, you create a new config to use a different 
file.
