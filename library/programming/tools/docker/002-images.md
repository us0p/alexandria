# Images
It's a standardized package that includes all of the files, binaries, 
libraries, and configurations to run a container.

There are two importantn principles of images:
1. **Images are immutable**: Once an image is created, it can't be 
   modified. You can only make a new image or add changes on top of it.
2. **Container images are composed of layers**: Each layer represents a set
   of file system changes that add, remove, or modify files.

## Image layers
Each layer in an image contains a set of filesystem changes - additions, 
deletions, or modifications.

!["image layers"](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layers.webp)

This is beneficial because it allows layers to be reused between images. 
Docker only rebuilds the changed layer and the layers after it, this is 
beneficial because it allows layers to be reused between images.

!["updated image layer"](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layer_reuse.webp)

They also let you extend images of other by reusing their base layers, 
allowing you to add only the data that your application needs.
