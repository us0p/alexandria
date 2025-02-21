# Modules
A module is a class annotated with a `@Module()` decorator. It provides 
metadata that Nest makes use of to organize the application structure.

Each application has at least one module, a root module. The root module is
the starting point Nest uses to build the application graph - The internal 
data structure Nest uses to resolve module and provider relationships and 
dependencies.
Modules are **strongly** recommended as an effective way to organize your 
components. Thus, for most applications, the resulting architecture will 
employ multiple modules, each encapsulating a closely related set of 
capabillities.

The module encapsulates providers by default. This means that it's 
impossible to inject providers that are neither directly part of the 
current module nor exported from the imported modules. Thus, you may 
consider the exported providers from a module as the module's public 
interface, or API.

## Feature module
It simply organizes code relevant for a specific feature, keeping code 
organized and establishing clear boundaries.
This means that classes that provide a specific feature should be moved to 
its own module.

## Shared modules
Modules are singletons by default, and thus you can share the same instance
of any providers between multiple modules effortlessly.
Every module is automatically a shared module. Once created it can be 
reused by any module.
If you want to share an instance of your providers between several other 
modules you need first to export the providers by adding it to the module's
`exports` array.

Now any module that imports this updated module will have access to that 
provider and will share the same instance with all other modules that 
import it as well.

## Module re-exporting
Module can export their internal providers. In addition, they can re-export
modules that they import, thus, making it available for other modules which
import this one.

## Dependency Injection
Module classes can inject providers as well via the constructor as 
mentioned.
However, module classes themselves cannot be injected as providers due to 
`circular dependency`

## Global modules
Nest encapsulates providers inside the modules scope. You aren't able to 
use a module's providers elsewhere without first import the encapsulating 
module.
When you want to provide a set of providers which should be available 
everywhere out-of-the-box, make the module global with the `@Global()` 
decorator.

The `@Global()` decorator makes the module global-scoped. Global modules 
should be registered only once, generally by the root or core module.
Providers in global modules are ubiquitous, and modules that wants to 
inject the service will not need to import the global service module.

## Dynamic modules
It enables you to easily create customizable modules that can register and 
configure providers dynamically.
