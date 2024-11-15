# Docker
`Docker` is a platform that simplifies the process of creating, deploying, 
and managing containers. It provides developers and administrators with a 
set of tools and APIs to manage containerized applications. With Docker, 
you can build and package application code, libraries, and dependencies 
into a container image, which can be distributed and run consistently in 
any environment that supports Docker.  
  
## Docker Compose
`Docker` is used to create, deploy and manage containers individually, as
your application grows, you'll at some point, deploy some other services
like a cache or a queue to attend your application needs.  
`Docker Compose` a platform used to manage many containers at once with a
single command.  
With Compose you can define all of your containers and their 
configurations in a single `YAML` file.  

## Dockerfile versus Compose file
A `Dockerfile` provides instructions to build a container image while a 
`Compose` file defines your running containers. Quite often, a `Compose` 
file references a `Dockerfile` to build an image to use for a particular 
service.  

## Containers
`Containers` are lightweight, portable, and isolated software environments 
that allow developers to run and package applications with their 
dependencies, consistently across different platforms.  
It ensures that applications run consistently, regardless of the underlying
infrastructure.  

## Namespaces
`Namespaces` is a Linux kernel feature that allows the isolation of various
system resources, making possible to a process and its children to have a
separate view of a subset of the system resources that is separate from 
the others.  
It creates an abstraction layer to keep containerized processes separate 
from one another and from the host system.  
When a container is started, `Docker` creates a new set of namespaces for 
that container. These namespaces only apply within the container, so any 
processes running inside the container have access to a subset of system 
resources that are isolated from other containers as well as the host 
system.  

## cgroups
`cgroups` or `control groups` is a Linux kernel feature that allows you to 
allocate and manage resources, such as CPU, memory, network bandwidth, and 
I/O, among groups of processes running on a system.  
`Docker` utilizes `cgroups` to enforce resource constraints on containers, 
allowing them to have a consistent and predictable behavior.  

## UnionFS
`Union filesystems`, also known as `UnionFS`, is a unique type of 
filesystem that creates a virtual, layered file structure by overlaying 
multiple directories.  
Instead of modifying the original file system or merging directories, 
UnionFS enables the simultaneous mounting of multiple directories on a 
single mount point while keeping their contents separate. It allows us to 
manage and optimize storage performance by minimizing duplication and 
reducing the container image size.  

## What are containers used for?
Before containers came into the picture, developers often faced challenges 
when deploying applications across different environments including:
- **Inconsistent environments**: Developers often work in different 
  environments which might have different configurations and libraries 
  compared to production servers. This leads to compatibility issues in 
  deploying applications.
- **Inefficient resource utilization**: `Virtual Machines (VMs)` were 
  widely used to overcome environment inconsistency. However, VMs require 
  an entire OS to be running for each application, making the resource 
  utilization inefficient.  
- `Slow processes and scalability issues`: Traditional deployment methods 
  have a slower time to market and scaling difficulties, which hinders fast 
  delivery of software updates.  
  
Containers address these challenges as follows:
- **Consistent environment**: Containers solve environment inconsistencies
  by bundling an application and its dependencies, configurations, and 
  libraries into a single container. This guarantees that the application 
  runs smoothly across different environments.  
- **Efficient resource utilization**: Unlike `VMs`, containers share 
  underlying system resources and OS kernel, which makes them lightweight 
  and efficient. Containers are designed to use fewer resources and boot up
  faster, improving resource utilization.  
- **Faster processes and scalability**: Containers can be easily created, 
  destroyed, and replaced, leading to faster development and deployment 
  cycles. Scaling applications becomes easier as multiple containers can 
  be deployed without consuming significant resources.  

## Virtual Machines
`Virtual machines (VMs)` are a way to run multiple applications on a single 
server. Each VM runs on top of a `hypervisor`, which is a piece of software 
that emulates the hardware of a computer. The `hypervisor` allows you to 
run multiple operating systems on a single server, and it also provides 
isolation between applications running on different VMs.
