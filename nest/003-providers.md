# Providers
Are a fundamental concepts in Nest. Many of the basic Nest classes may be 
treated as a provider. The main idea of a provider is that i can be 
injected as a dependency; this means objects can create various 
relationships with each other, and the function of "wiring up" these 
objects largely be delegated to the Nest runtime system.

!["providers"](https://docs.nestjs.com/assets/Components_1.png)

Controllers should handle HTTP requests and delegate more complex tasks to 
providers.
Providers are plain JavaScript classes that are declared as `providers` in 
a NestJS module.

## Services

