## AWS Identity and access management (IAM)
Enables you to manage access to AWS services and resources securely.
## AWS account root user
When you first create an AWS account, you begin with an identity known as the `root user`.

The `root user` has complete access to all the AWS services and resources in the account.

![[Pasted image 20250409093041.png]]

Do not use the `root user` for everyday tasks. Instead, use the `root user` to create your first IAM user and assign it permissions to create other users.

Only use the root user when you need to perform a limited number of tasks that are only available to the `root user`.Examples of these tasks include changing your `root user` email address and changing your AWS support plan.
## IAM users
An IAM user is an identity that you create in AWS. It represents the person or application that interacts with AWS services and resources. It consists of a name and credentials.

By default, when you create a new IAM user in AWS, it has no permissions associated with it.

To allow the IAM user to perform specific actions in AWS, you must grant the IAM user the necessary permissions.

It's recommended to create individual IAM users for each person who needs to access AWS. Even if you have multiple employees who require the same level of access. 

This provides additional security by allowing each IAM user to have a unique set of security credentials.
## IAM policies
Are documents that allows or denies permissions to AWS services and resources. It enable you to customize users' levels of access to resources.

For example, you can allow users to access all of the Amazon S3 buckets within
your AWS account, or only a specific bucket.

> Follow the security principle of least privilege when granting permissions.
## Example: IAM Policy
Suppose you have to create an IAM user for a newly hired developer. The developer needs access to some files kept in S3 bucket with the ID: `AWSDOC-EXAMPLE-BUCKET`.

![[Pasted image 20250409093334.png]]

In this example, the IAM policy is allowing a specific action within Amazon S3: `ListObject`. The policy also mentions a specific bucket ID: `AWSDOC-EXAMPLE-BUCKET`.

When the owner attaches this policy to the developer's IAM user, it'll allow the developer to view all of the objects in the `AWSDOC-EXAMPLE-BUCKET` bucket.

If the owner wants the developer to be able to access other services and perform other actions in AWS, the owner must attach additional policies to specify these services and actions.
## IAM groups
It's a collection of IAM users. When you assign an IAM policy to a group, all users in the group are granted permissions specified by the policy.

Assigning IAM policies at the group level also makes it easier to adjust permissions when an employee transfers to a different job.
## IAM roles
It's an identity that you can assume to gain temporary access to permissions.

An employee rotates to different workstations throughout the day, when the employee needs to switch to a different task, they give up their access to one workstation and gain access to the next workstation. The employee can easily switch between workstations, but at any given point in time, they can have access to only a single workstation.

Before an IAM user, application, or service can assume an IAM role, they must be granted permissions to switch to the role.

When someone assumes an IAM role, they abandon all previous permissions that they had under a previous role and assume the permissions of the new role.

> IAM roles are ideal for situations in which access to services or resources needs to be granted temporarily, instead of long-term.
## AWS Organizations
If your company has multiple AWS accounts, you can use `AWS Organizations` to consolidate and manage multiple AWS accounts within a central location. 

When you create an organization, AWS Organizations automatically creates a **root**, which is the parent container for all the accounts in your organization.

In AWS Organizations, you can centrally control permissions for the accounts in your organization by using `service control policies (SCPs)`. 

SCP enable you to place restrictions on the AWS services, resources, an individual API actions that users and roles in each account can access.

> Consolidated billing is another feature of AWS Organizations.
## Organizational units
In AWS Organizations, you can group accounts into organizational units (`OUs`) to make it easier to manage accounts with similar business or security requirements.

When you apply a policy to an `OU`, all the accounts in the `OU` automatically inherit the permissions specified in the policy.

By organizing separate accounts into `OUs`, you can more easily isolate workloads or applications that have specific security requirements.

You can apply `SCPs` to the organization root, an individual member account, or an `OU`. An `SCP` affects all IAM users, groups, and roles within an account, including the AWS account root user.

You can't apply IAM policies to the AWS account root user.