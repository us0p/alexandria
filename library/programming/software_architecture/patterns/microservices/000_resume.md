## Microservices
- each service should contain one or more sub-domain.
- must be independently deployable and loosely coupled.
- each servcice has its own source code and its own pipeline which builds, tests and deploys the service.
### Benefits
- easy to maintain,
- scalable,
- fast deployment pipeline
### Drawbacks
- increased complexity specially when tracing exceptions and bugs on distributed transactions.
### When and How to use
- there's need or planning to scale.
- carefully consider the design to avoid inneficient interactions or tight coupling between services.