# Multi-Stage Builds
In a traditional build, all build instructions are executed in sequence, 
and in a single build container.
All those layers end up in your final image. This approach works, but it 
leads to bulky images carrying unnecessary weight and increasing your 
security risks.

Multi-stage builds introduce multiple stages in your Dockerfile, each with 
a specific purpose. Think of it like the ability to run different parts of 
a build in multiple different environments, concurrently. By separating the
build environment from the final runtime environment, you can significantly
reduce the image size and attack surface.

```Dockerfile
# Stage 1: Build Environment
FROM builder-image AS build-stage 
# Install build tools (e.g., Maven, Gradle)
# Copy source code
# Build commands (e.g., compile, package)

# Stage 2: Runtime environment
FROM runtime-image AS final-stage  
#  Copy application artifacts from the build stage (e.g., JAR file)
COPY --from=build-stage /path/in/build/stage /path/to/place/in/final/stage
# Define runtime configuration (e.g., CMD, ENTRYPOINT)
```

Notice there are multiple FROM statements and a new AS `<stage-name>`. In 
addition, the COPY statement in the second stage is copying --from the 
previous stage.

This Dockerfile uses two stages:
- The build stage uses a base image containing build tools needed to 
  compile your application. It includes commands to install build tools, 
  copy source code, and execute build commands.
- The final stage uses a smaller base image suitable for running your 
  application. It copies the compiled artifacts from the build stage. 
  Finally, it defines the runtime configuration for starting your 
  application.
