- Terraform's representation of the word. Contains information about every single resource and or data object we have deployed using terraform.
- Can be stored locally or remotely. On a company it's stored remotely in S3 for example.
## Data Object
In terraform, the blocks that correspond to resources are resources blocks and the blocks that correspond to data are the data blocks.
## Local Backend
State file is stored in your computer, it's easier to work with but harder to colaborate.
## Remote Backend
State file is stored online.

There are two ways of creating a remote backend:
1. Terraform Cloud: Managed offering from Hashicorp itself. Free up to 5 users.
2. CSP Option (e.g. AWS): You can store the file in a Clouse Service Provider file share service and enable multiple users to have access to it, lets take the AWS S3 bucket example.
```plaintext
terraform {
	backend "s3" {
		bucket         = "devops-directive-tf-state"
		key            = "tf-infra/terraform.tfstate"
		region         = "us-east-1"
		dynamodb_table = "terraform-state-locking"
		encrypt        = true
	}
}
```

- We're defining the S3 bucket where the state file will actually be stored. And we're also making it encrypted.
- We use the dynamo db table to avoid concurrent changes to the same state file by locking the file while we make changes.

To apply the CSP option, you need to go through a bootstrapping process that's going to enable both the resources one at the time since we can't provide both from the get go.
1. Starts with a local backend.
2. Define the resources that you need (S3 and DynamoDB table).
3. Apply the changes and create the resources.
4. Change the local backend to the remote S3 backend.
5. Re-run terraform init command and import your local state file to S3.