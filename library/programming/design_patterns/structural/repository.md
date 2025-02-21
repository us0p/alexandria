# Repository Pattern
It abstracts data access, providing a centralized way to manage data 
operations by acting as an intermediary layer between an aplication's 
business logic and data storage.
- Its primary purpose is to provide a structured and standardized way to 
  access, manage, and manipulate data while abstracting the underlying 
  details of data storage technologies.
- This pattern promotes a clear separation of concerns, making software 
  more maintainable, testable, and adaptable to changes in data sources.

Contributes in the isolation of the data access layer and the domain layer.
enables the encapsulating of data access logic, and dependency injection.
You should only use this pattern if you're working with domain objects.

```typescript
// example entity
class ClientEntity {
    firstName: string
    lastName: string
    occupation: string

    constructor(firstName, lastName, occupation) {
        this.firstName = firstName
        this.lastName = lastName
        this.occupation = occupation
    }
}
```

## Specialized Repositories
```typescript
interface IClientRepository {
    get: (id: number) => Promise<ClientEntity>
    getAll: () => Promise<ClientEntity[]>
    save: (client: ClientEntity) => Promise<bool>
    update: (client: ClientEntity) => Promise<bool>
    delete: (id: number) => Promise<bool>
}
```
Note that the interface only refers to the `ClientEntity` which makes it 
specialized, it deals only with `ClientEntity` objects.
By using specialized interfaces, we need to create one for each entity in 
the domain. It's a repetitive work but it does provide a clearer contract 
to implement.

## Generity Repositories
```typescript
interface IEntityRepository<Entity>{
    get: (id: number) => Promise<Entity>
    getAll: () => Promise<Entity[]>
    save: (client: Entity) => Promise<bool>
    update: (client: Entity) => Promise<bool>
    delete: (id: number) => Promise<bool>
}
```

Note that the interface is generic over the Entity, this means that it can 
be used by any entity in the domain leadin to less code.
Altough it looks like a bether option, by using a generic repository you 
assume that every entity in your domain has the same caracteristics and 
behaviours, which might not be te case.

Another way of using a generic repository is to make it a base interface 
for specialized repositories, which should implement the basic CRUD 
operations for example and add any extra behavior needed.

```typescript
interface ICarRepository extends IEntityRepository<Car>{
    get: (id: number) => Promise<Car>
    getAll: () => Promise<Car[]>
    save: (client: Car) => Promise<bool>
    update: (client: Car) => Promise<bool>
    delete: (id: number) => Promise<bool>
    getByBrand: (brand: string) => Promise<Car[]>
    deleteByYear: (year: string) => Promise<bool>
}
```

This way you have a consistent contract which should be implemented for all
your CRUD Repositories.

## Implementation
The implementation should be made by implementing the generic or 
specialized interface.
By doing that your domain doesn't need to know about which database or 
persistance storage is being used, rather the provided repository will have
the required methods, it doesn't matter if it's SQLite, MongoDB, Redis or 
any other.

## Why receive and return Entities?
You'll notice that repositories often receive and return Entities, while it
might seems against the recommended way of communication between layers, 
the repository does that to ensure that the entities are always in a valid 
state and that the business rules are always applied.

## Advantages:
- application interact with data through a consistent interface.
- testing becomes simpler.
- separation of concerns, simpler to optimize data access without impacting
  the application as a whole.

## Disadvantages:
- not suitable for small applications.
- requires time to set up interfaces and repository classes.
