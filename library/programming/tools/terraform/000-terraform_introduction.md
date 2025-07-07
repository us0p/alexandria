# Terraform
A tool from HashiCorp for building, changing, and versioning infrastructure safely and efficiently across many cloud providers.

Falls in this category as infrastructure as code (IaC) tools, which allows you define you entire cloud infrastructure as a set of config files which then the tool Terraform can go out and interact with the cloud provider API and provision and manage on our behalf.
## Terraform Architecture
- Terraform Core: The engine that takes the configuration files and the current terraform state
- Terraform Providers: Are like plugins to the core that enable communication with a specific cloud provider.
## Working with Terraform
- Install Terraform
- Authenticate with you cloud provider
- Create your terraform config file.
- Init terraform to authenticate with the cloud provider with `terraform init`
- Review the terraform plan for the changes with `terraform plan`
- Apply the changes in the infrastructure with `terraform apply`
- Remove the changes in the infrastructure with `terraform destroy`
## Providers
You can find many providers at https://registry.terraform.io