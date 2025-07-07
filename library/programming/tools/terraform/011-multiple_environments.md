There's two main approaches to handle multiple environments:
- **Workspaces**: 
- **File Structure**: 
## Workspaces
Allow the use of multiple named sections within a single backend. It isolates their state, so if you run `terraform plan`, Terraform will not see any existing state for this configuration.

 **Pros**
- Easy to get started
- Convenient `terraform.workspace` expression
- Minimizes Code Duplication
**Cons**
- Prone to human error
- State stored within same backend
- Codebase doesn't unambiguously show deployment configurations
## File Structure
Directory layout provides separation, modules provide reuse.

**Pros**
- Isolation of backends
	- Improved security
	- Decreased potential for human error
- Codebase fully represents deployed state
**Cons**
- Multiple terraform apply required to provision environments
- Mode code duplication, but can be minimized with modules

As the system grows, in order to handle more components:
- Further separation (at logical components groups) useful for larger projects
	- Isolate things that change frequently from those which don't
- Referencing resources across configuration is possible using `terraform_remote_state`.
![[Pasted image 20250624085517.png]]