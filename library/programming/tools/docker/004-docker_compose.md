# Docker Compose
Lets you define all of your containers and their configurations in a single
YAML file. 

It's important to understand that Compose is a declarative tool. You don't 
always need to recreate everything from scratch. If you make a change, run 
`docker compose up` again and Compose will reconcile the changes in your 
file and apply them intelligently.

## Dockerfile vs Compose File
A Dockerfile provides instructions to build a container image while a 
Compose file defines your running containers. Quite often, a Compose file 
references a Dockerfile to build an image to use for a particular service.
