# Modules
A module is a collection of Go packages that are released together.
  
A module is identified by a module path, which is declared in a `go.mod`
file, together with information about the module’s dependencies. The module
root directory is the directory that contains the `go.mod` file. The main 
module is the module containing the directory where the `go command` is 
invoked.  
  
Your module specifies dependencies needed to run your code, including the 
Go version and the set of other modules it requires.  
  
A package path is the module path joined with the subdirectory containing 
the package **(relative to the module root)**.
  
When you run `go mod init` to create a module for tracking dependencies, you
specify a module path that serves as the module’s name.  
The module path becomes the import path prefix for packages in the module.  
Be sure to specify a module path that won’t conflict with the module path 
of other modules.  
  
Modules are sometimes defined in repository subdirectories. Such a module 
is expected to be found in a subdirectory that matches the part of the 
module’s path after the repository root path.  
  
For example, suppose the module example.com/monorepo/foo/bar is in the 
repository with root path example.com/monorepo. Its go.mod file must be in
the foo/bar subdirectory.

## Calling your code from another module
Consider the following folder structure:

```plaintext
<home>/
 |-- greetings/
		 |-- go.mod -> example.com/greetings
		 |-- greetings.go
 |-- hello/
		 |-- go.mod -> example.com/hello
		 |-- hello.go
```
  
Here, `hello.go` imports the `greetings` module:

```go
// hello.go
package main

import (
    "fmt"

    "example.com/greetings"
)
//...
```

For production use, you’d publish the example.com/greetings module from its
repository, where Go tools could find it to download it.
