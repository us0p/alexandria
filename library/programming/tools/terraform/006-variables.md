# Variable
### Input Variables
Referenced by using `var.<name>`
```plaintext
variable "instance_type" {
	description = "some description"
	type        = string
	default     = "default value for variable"
}
```
### Local Variables
Referenced by using `local.<name>`
```plaintext
locals {
	service_name = "name"
	owner        = "owner name"
}
```
### Output Variables
```plaintext
output "instance_ip_addr" {
	value = aws_instance.instance.public_ip
}
```
## Types
### Primitive Types
- string 
- number
- bool
### Complex Types
- list(type)
- set(type)
- map(type)
- object({attr_name = type})
- tuple([types])
## Validation
- Type checking happens automatically
- Custom conditions can also be enforced
## Sensitive Data
- Mark variables as sensitive, `sensitive = true`. Can use command `-var` to retrieve from secret manager at runtime.