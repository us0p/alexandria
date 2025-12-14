# Layered Architecture
Architecture in which functionality of a system is divided into a set of layers, with each layer having a specific responsibility and interacting with the layers above and below it.

The main idea behind a layered architecture is to separate the concerns of the system into distinct and independent layers, making the code more modular, easier to understand, test, and modify.

There are several types of layered architectures (that's why it's usually referenced as **n-tiered** patter), but a common one is the three-layer architecture which consists of:
- Presentation Layer
- Business Layer
- Data Access Layer

Components are organized in horizontal layers.

![[Pasted image 20251214142111.png]]

Notice for example that all components related to the **Presentation Layer** are placed together, even if they are related to completely different domains. Also note that components on the same layer aren't necessary dependent on each other.
### Closed Layer
Requests must go through all layers from top to bottom. It provides layers of isolation making the code more modular.

![[Pasted image 20251214142650.png]]
> An operation must go through all the layers when they're closed.
### Open Layer
Allows Requests to skip specific layers. Usually applied when extra layers are added to allow requests that would little or no value added by that layer to bypass it.

![[Pasted image 20251214143007.png]]
> Note that by having open layers increase the coupling in the system as now layers must be aware of open layers.