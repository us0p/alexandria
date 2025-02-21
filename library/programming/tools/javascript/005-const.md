# const
The `const` declaration declares block-scoped local variable. The value of 
a constant can't be changed through reassignment using the assignment 
operator, but if a constant is a object, its properties can be added, 
updated, or removed.

```javascript
const number = 42;
try {
    number = 99;
} catch (err) {
    console.log(err);
    // TypeError: invalid assignment to const 'number'
}

console.log(number); // 42
```

- is scoped to blocks as wells as functions.
- can only be accessed after the place of declaration is reached (TDZ). For
  this reason, `const` declarations are commonly regarded as non-hoisted.
- do not create properties on `globalThis` when declared at the top level 
  of a script.
- cannot be redeclared by any other declaration in the same scope.
- it begins declarations, not statements. That means you cannot use a lone 
  `const` declaration as the body of a block since there's no way to access
  the variable.
- an initializer for a constant is required given that it can't be changed 
  later.

The `const` declaration creates an immutable reference to a value. It does 
not mean the value it holds is immutable, just that the variable identifier
cannot be reassigned. For instance, in the case where the content is an 
object. You should understand `const` declarations as "create immutable 
bindings", not "immutable values".
