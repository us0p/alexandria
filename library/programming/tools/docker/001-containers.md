# Containers
Isolated processes for each component. Each component runs in its own 
isolated environment, completely isolated from everything else on your 
machine.
Containers are self contained. Each container has everything it need to 
function with no reliance on any pre-installed dependencies on the host 
machine.
Containers are isolated and independent, which means that they have minimal
influence on host and independent of any other container.

## Pros
- Consistent environment: Containers bundling an application and its 
  dependencies, configurations, and libraries into a single container. This
  guarantees that the application runs smoothly across different 
  environments.
- Efficient resource utilization: Unlike VMs, containers share underlying 
  system resources and OS kernel, which makes them lightweight and 
  efficient. Containers are designed to use fewer resources and boot up 
  faster, improving resource utilization.
- Faster processes and scalability: Containers can be easily created, 
  destroyed, and replaced, leading to faster development and deployment 
  cycles. Scaling applications becomes easier as multiple containers can 
  be deployed without consuming significant resources.

## Containers x Virtual Machines
A VM is an entire operating system with its own kernel, hardware drivers, 
programs, and applications. Spinning up a VM only to isolate a single 
application is a lot of overhead.
A container is simply an isolated process with all the files it needs to 
run. If you run multiple containers, they all share the same kernel, 
allowing you to run more applications on less infrastructure.

## How does a container work?
A container uses a mix of Linux kernel features that enables the isolation 
of processes and the mounting of files systems in layers to save memory 
usage, bellow you'll find an introduction to those features.

## Namespaces
Is a Linux kernel feature that allows the isolation of various system 
resources, making possible to a process and its children to have a
separate view of a subset of the system resources that is separate from 
the others. It creates an abstraction layer to keep containerized processes
separate from one another and from the host system.
When a container is started, Docker creates a new set of namespaces for 
that container. These namespaces only apply within the container, so any 
processes running inside the container have access to a subset of system 
resources that are isolated from other containers as well as the host 
system.

## Control Groups (CGroups)
Is a Linux kernel feature that allows you to allocate and manage resources,
such as CPU, memory, network bandwidth, and I/O, among groups of processes 
running on a system.
Docker utilizes cgroups to enforce resource constraints on containers, 
allowing them to have a consistent and predictable behavior.

## Union Filesystems (UnionFS)
Is a unique type of filesystem that creates a virtual, layered file 
structure by overlaying multiple directories. Instead of modifying the 
original file system or merging directories, UnionFS enables the 
simultaneous mounting of multiple directories on a single mount point while
keeping their contents separate. 
It allows us to manage and optimize storage performance by minimizing 
duplication and reducing the container image size.
