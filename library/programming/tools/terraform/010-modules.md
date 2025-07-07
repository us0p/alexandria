# Modules
Containers for multiple resources that are used together.

A module consists of a collection of `*.tf` and/or `*.tf.json` files kept together in a directory.

Modules are the main way to package and reuse resource configurations with Terraform.
## What makes a good module
- Raises the abstraction level from base resource types.
- Groups resources in a logical fashion.
- Exposes input variables to allow necessary customization and composition.
- Provides useful defaults.
- Returns outputs to make further integrations possible.
## Types of Modules
- **Root Module**: Default module containing all `.tf` files in main working directory.
- **Child Module**: A separate external module referred to from a `.tf` file.
### Module Sources
- Local paths
- Terraform Registry
- GitHub
- HTTP URLs
- S3 Buckets
- ...

```plaintext
# Local Path
module "web-app" {
	source = "../web-app"
}

# Terraform Registry
module "consul" {
	source = "hashicorp/consul/aws"
	version = "0.1.0"
}

# Github
# HTTPS
module "example" {
	source = "github.com/hashicorp/example?ref=v1.2.0"
}

# SSH
module "example" {
	source = "git@github.com:hashicorp/example.git"
}

# GENERIC
module "example" {
	source = "git::ssh://username@example.com/storage.git"
}
```
## Inputs + Meta arguments
Inputs variables are passed in via module block

```plaintext
module "web_app" {
	source = "../web-app-module"

	# Input Variables
	bucket_name = "devops-directive-web-app-data"
	domain      = "mysuperaweasomesite.com"
	db_name     = "mydb"
	db_user     = "foo"
	db_pass     = var.db_pass # reference to variable declared in variables.tf
}
```