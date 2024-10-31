# Workspaces
A workspace is a collection of modules on disk that are used as the main 
modules when running **minimal version selection (MVS)**.  
  
A workspace can be declared in a `go.work` file that specifies relative 
paths to the module directories of each of the modules in the workspace. 
When no `go.work` file exists, the workspace consists of the single module 
containing the current directory.  
  
Most go subcommands that work with modules operate on the set of modules 
determined by the current workspace.  
  
## How workspace is determined
A command determines whether it is in a workspace context by:
1. Examining the GOWORK environment variable. If GOWORK is set to off, the
   command will be in a single-module context.
2. If the `GOWORK` env is empty or not provided, the command will search 
   the current working directory, and then successive parent directories, 
   for a file `go.work`. If a file is found, the command will operate in 
   the workspace it defines; otherwise, the workspace will include only the
   module containing the working directory.
3. If `GOWORK` names a path to an existing file that ends in `.work`, 
   workspace mode will be enabled. Any other value is an error.
  
You can use the go env `GOWORK` command to determine which `go.work` file 
the `go` command is using. `go env GOWORK` will be empty if the `go` 
command is not in workspace mode.

## Do not include your go.work file in VCS
It is generally inadvisable to commit `go.work` files into version control
systems, for two reasons:
1. A checked-in `go.work` file might override a developer’s own go.work 
   file from a parent directory, causing confusion when their use 
   directives don’t apply.
2. A checked-in `go.work` file may cause a continuous integration (CI) 
   system to select and thus test the wrong versions of a module’s 
   dependencies. 
  
CI systems should generally not be allowed to use the `go.work` file so 
that they can test the behavior of the module as it would be used when 
required by other modules, where a `go.work` file within the module has no
effect.
That said, there are some cases where committing a `go.work` file makes 
sense. For example, when the modules in a repository are developed 
exclusively with each other but not together with external modules, there 
may not be a reason the developer would want to use a different combination
of modules in a workspace.
