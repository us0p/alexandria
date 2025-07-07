# Meta Arguments
- **depends_on**: Used to represent dependencies between resources. If two resources depend on each other (but not each other data), **depends_on** specifies that dependency to enforce ordering.

Terraform automatically generates dependency graph based on references.

```plaintext
resource "aws_instance" "example" {
	# ...

	depends_on = [
		aws_iam_role_policy.example,
	]
}
```

- **count**: Allows for creation of multiple resources/modules from a single block. Useful when the multiple necessary resources are nearly identical.

```plaintext
resource "aws_instance" "server" {
	count = 4 # create four EC2 instances

	# ...

	tags = {
		Name = "Server ${count.index}"
	}
}
```

- **for_each**: Allows for creation of multiple resources/modules from a single block. Allows more control to customize each resource than count.

```plaintext
locals {
	subnet_ids = toset([
		"subet-abcdef",
		"subnet-012345",
	])
}

resource "aws_instance" "server" {
	for_each = local.subnet_ids

	# ...

	tags = {
		Name = "Server ${each.key}"
	}
}
```

- **lifecycle**: Set of meta arguments to control terraform behavior for specific resources.
	- `create_before_destroy`: Help with zero downtime deployments.
	- `ignore_changes`: Prevents Terraform from trying to revert metadata being set elsewhere.
	- `prevent_destroy`: Causes Terraform to reject any plan which would destroy this resource.

```plaintext
resource "aws_instance" "server" {
	# ...

	lifecycle {
		create_before_destroy = true
		ignore_changes = [
			# Some resources have metadata
			# modified automatically outside
			# of Terraform
			tags
		]
	}
}
```