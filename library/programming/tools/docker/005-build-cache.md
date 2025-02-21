# Build Cache
When you run the docker build command to create a new image, Docker 
executes each instruction in your Dockerfile, creating a layer for each 
command and in the order specified. For each instruction, Docker checks 
whether it can reuse the instruction from a previous build. If it finds 
that you've already executed a similar instruction before, Docker doesn't 
need to redo it. Instead, it’ll use the cached result. This way, your build
process becomes faster and more efficient, saving you valuable time and 
resources.

In order to maximize cache usage and avoid resource-intensive and 
time-consuming rebuilds, it's important to understand how cache 
invalidation works. Here are a few examples of situations that can cause 
cache to be invalidated:
- Any changes to the command of a RUN instruction invalidates that layer.
- Any changes to files copied into the image with the COPY or ADD 
  instructions.
- Once one layer is invalidated, all following layers are also invalidated.

If any previous layer, including the base image or intermediary layers, has
been invalidated due to changes, Docker ensures that subsequent layers 
relying on it are also invalidated. This keeps the build process 
synchronized and prevents inconsistencies.
