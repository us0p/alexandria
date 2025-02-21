## Explanation
When a container starts, it uses the files and configuration provided by 
the image. Each container is able to create, modify, and delete files and 
does so without affecting any other containers. When the container is 
deleted, these file changes are also deleted.
While this ephemeral nature of containers is great, it poses a challenge 
when you want to persist the data.

# Volumes
Volumes are a storage mechanism that provide the ability to persist data 
beyond the lifecycle of an individual container. Think of it like providing
a shortcut or symlink from inside the container to outside the container.

You can create new volumes using docker, the create volume need to be 
mounted (or attached) into some folder within the container.
All changes to the attached folder within the container will be replicated 
to the volume which lives outside the container.

If you delete the container and start a new container using the same 
volume, the files will still be there.

## Sharing files using volumes
You can attach the same volume to multiple containers to share files 
between containers. This might be helpful in scenarios such as log 
aggregation, data pipelines, or other event-driven applications.

## Volumes versus bind mounts
If you want to ensure that data generated or modified inside the container 
persists even after the container stops running, you would opt for a 
volume.

If you have specific files or directories on your host system that you want
to directly share with your container, like configuration files or 
development code, then you would use a bind mount. It's like opening a 
direct portal between your host and container for sharing. Bind mounts are 
ideal for development environments where real-time file access and sharing 
between the host and container are crucial.

## File permissions for Docker access to host files
When using bind mounts, it's crucial to ensure that Docker has the 
necessary permissions to access the host directory

## Synchronized File Share
As your codebase grows larger, traditional methods of file sharing like 
bind mounts may become inefficient or slow, especially in development 
environments where frequent access to files is necessary. Synchronized file
shares improve bind mount performance by leveraging synchronized filesystem
caches. This optimization ensures that file access between the host and 
virtual machine (VM) is fast and efficient.
