# Types
Every single expression in PHP has one of the following built-in types:
- null
- bool
- int
- float
- string
- array
- object
- callable
- resource

PHP is a dynamic typed language. However, it's possible to statically type 
some aspect of the language via the use of `type declarations`.

If an expression/variable is used in an operation which its type doesn't 
support, PHP will attempt to `type juggle` the value into a type that 
supports the operation.

```php
$a_bool = true;
$a_str = "foo";
$an_int = 12;
```

## Atomic types
**Built-in types**
- Scalar types:
    - bool
    - int
    - float
    - string
- array
- object
- resource
- never
- void
- Relative class types: self, parent, and static
- Singleton types
    - false
    - true
- Unit types
    - null

**User-defined types (generally referred to as class-types)**
- Interfaces
- Classes
- Enumerations

**Others**
- callable

## Composite types
It's possible to combine multiple atomic types into composite types in the 
following ways:
- Intersection of class-types (interfaces and class names).
- Union of types.

## Intersection types
An intersection type accepts values which satisfies multiple class-type 
declarations, rather than a single one. Idividual types which form the 
intersection type are joined by the `&` symbol 
(e.g. types T, U, and V => T&U&V).

## Union types
Accepts values of multiple different types, rather than a single one. Types
are joined by the `|` symbol.
If one of the types is an intersection type, it needs to be bracketed with 
parenthesis `T|(X&Y)`.

## Type aliases
PHP supports two types aliases which corresponds to the union type of some 
types:
- `mixed`: object|resource|array|string|float|int|bool|null
- `iterable`: Traversable|array
