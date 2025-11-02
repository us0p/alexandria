# Clean Code
A guide for producing readable, reusable and extendable software.
# Rules
1. Be consistent
2. Use meaningful names over comments
3. Indentation and code style
4. Keep framework code distant
5. Organize code by Actors
6. Keep it simple, refactor often
## Guidelines
1. Keep methods, classes and files small
2. Avoid passing nulls and booleans
## Command Query Separation (CQS)
Software design principle that separates the responsibilities of a method or function into two categories: commands and queries.

Commands are methods that change the state of the system, while queries are methods that return information but do not change the state of the system.
## Keep Framework Code Distant
Refers to separating the application's code from the framework's code. By doing so, it makes it easier to maintain, test, and upgrade the application's codebase and the framework independently.
1. Use an abstraction layer to separate the application code from the framework code. This allows the application code to be written without the need to know the specifics of the framework.
2. Use dependency injection to decouple the application code from the framework code. This allows the application code to use the framework's functionality without having to instantiate the framework objects directly.
3. Avoid using framework-specific libraries or classes in the application code. This makes it easier to switch to a different framework in the future if needed.
4. Use a standard interface for the application code to interact with the framework. This allows the application code to be written without the need to know the specifics of the framework.
5. Keep the application and the framework code in separate projects and/or repositories.
## Avoid Passing Nulls Booleans
Passing `nulls` or `booleans` can lead to unexpected behavior and difficult-to-debug errors in a program.
- Use `Optionals` types instead of `null` to indicate the absence of a value. This makes it clear when a value is missing and prevents null reference exceptions.
- Use a default value for function arguments instead of allowing them to be `null` or Boolean. This eliminates the need to check for null or Boolean values and reduces the potential for errors.
- Use the Null Object pattern to replace null values with a special object that has a defined behavior. This eliminates the need to check for null values and makes the code more readable.
## Organize Code by Actor it Belongs to
Advocates for structuring your codebase not primarily by technical layers (e.g., `controllers`, `services`, `repositories`) but by the **actors** or **features** that use or interact with specific parts of the system.

Group all code related to a particular use case, feature, or user role together.
### What is an "Actor" in this context?
Is anything that interacts with the system or uses its features. This could include:
- Human Users
- External Systems
- Internal Systems

The core idea is to think about who or what is using a piece of functionality and keep that functionality's code close together.

Example using actor's role, usually preferred for small applications.
```plaintext
src/
├── admin/
│   ├── controllers/
│   │   └── UserController.js     // manage users
│   │   └── ProductController.js  // manage products
│   ├── services/
│   │   └── UserService.js
│   │   └── ProductService.js
│   ├── dtos/
│   │   └── UserUpdateDto.js
│   │   └── ProductCreateDto.js
│   └── repositories/             // Admin might use specific repos or interfaces
│       └── AdminUserRepository.js
├── customer/
│   ├── controllers/
│   │   └── ProfileController.js  // view/update profile
│   │   └── OrderController.js    // place/view orders
│   ├── services/
│   │   └── ProfileService.js
│   │   └── OrderService.js
│   ├── dtos/
│   │   └── CustomerProfileDto.js
│   │   └── PlaceOrderRequestDto.js
│   └── repositories/
│       └── CustomerOrderRepository.js
├── product-manager/
│   ├── controllers/
│   │   └── ProductCatalogController.js // edit product details
│   ├── services/
│   │   └── ProductCatalogService.js
│   └── dtos/
│       └── ProductUpdateDetailsDto.js
└── shared/                     // For truly common components (e.g., core entities, common utilities)
    ├── models/
    │   ├── User.js             // Base User model, potentially extended by roles
    │   ├── Product.js
    │   └── Order.js
    ├── infrastructure/
    │   └── database.js
    └── utils/
        └── authUtils.js
```

Example using features/use cases. It's more granular and often preferred for very large and complex systems.
```plaintext
src/
├── customer/
│   ├── login/
│   │   ├── LoginController.ts
│   │   ├── LoginService.ts
│   │   ├── LoginRequestDto.ts
│   │   └── errors.ts
│   ├── view-profile/
│   │   ├── ViewProfileController.ts
│   │   ├── ViewProfileService.ts
│   │   └── ProfileDto.ts
│   ├── place-order/
│   │   ├── PlaceOrderController.ts
│   │   ├── PlaceOrderService.ts
│   │   ├── PlaceOrderCommand.ts
│   │   └── OrderConfirmationDto.ts
│   └── cancel-order/
│       ├── CancelOrderController.ts
│       └── CancelOrderService.ts
├── admin/
│   ├── manage-users/
│   │   ├── ManageUsersController.ts
│   │   ├── ManageUsersService.ts
│   │   └── UserManagementDto.ts
│   └── approve-returns/
│       ├── ApproveReturnsController.ts
│       └── ApproveReturnsService.ts
└── common/                       // For truly shared entities, types, infrastructure
    ├── entities/
    │   ├── User.ts
    │   ├── Product.ts
    │   └── Order.ts
    ├── interfaces/
    │   └── IRepository.ts
    └── exceptions/
        └── NotFoundException.ts
```