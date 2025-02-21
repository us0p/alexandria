# Packages
A package is a directory inside your `root directory` (the directory which
contains a `go.mod` file), containing, among other things, `.go` files.  
The name of the package should match the name of the directory in which its
source is located.  
If your package is called `logger`, then its source files shold be located
in `root_directory/logger`.  

## Package naming rules
- Package names should be all lower case.
- The name of a package is part of every identifier exported by that 
  package.
- All the files in a package must have the same `package` declaration.
  Test files are an exception. Files ended in `_test.go` may include a 
  different `package` declaration by appending `_test` to the end of the 
  package name. This is known as *external test*.

## Main packages
Some packages are actually commands, these carry the declaration 
`package main`.  
In the case of commands, the name of the command is taken from the name of
the package’s directory. Which means that for `package main` packages the 
directory name doesn’t matter.

## The import path
When you create a package, it's stored inside a directory under the 
`root directory`.  
  
The import path of a package is the full path from the `root directory` to
the directory where the package is located prefixed with the module's name
(the module path you specified when you executed `go mod init`).  
  
In Go, unlike some other languages, there is no concept of subpackages. 
Each package stands on its own, and the package name does not include any 
hierarchy. If there were subpackages, there could be naming collisions and
confusion. As an example, consider the `ioutil` package in the standard 
library. Instead of having an import path like `io/util`, it is simply 
named `ioutil`.  
