## AWS Shared responsibility model
In AWS you do not treat your AWS environment as a single object. Rather, you treat the environment as a collection of parts that build upon each other.

AWS is responsible for some parts of your environment and you (the customer) are responsible for other parts.

The `shared responsibility model` divides into customer responsibilities (commonly referred to as `security in the cloud`) and AWS responsibilities (commonly referred to as `security of the cloud`).

![[Pasted image 20250409090854.png]]
## Customers: Security IN the cloud
Customers are responsible for the security of everything that they create and put in the AWS Cloud.

When using AWS services, you, the customer, maintain complete control over your content. You are responsible for managing security requirements for your content, including which content you choose to store on AWS, which AWS service you use, and who has access to that content. You control how access right are granted, managed, and revoked.

The security steps that you take will depend on factors such as the services that you use, the complexity of your systems, and your company’s specific operational and security needs.

Steps include selecting, configuring, and patching the operating systems that will run on Amazon EC2 instances, configuring security groups, and managing user accounts.
## AWS: Security OF the cloud
AWS is responsible for security of the cloud. AWS operates, manages, and controls the components at all layers of infrastructure. This includes areas such as the host operating system, the virtualization layer, and even the physical security of the data centers from which services operate.

AWS is responsible for protecting the global infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure includes AWS [Regions](aws_region.md), [Availability Zones](aws_az.md), and [Edge Locations](aws_edge_locations.md).

AWS manages the security of the cloud, specifically the physical infrastructure that hosts your resources, which include:
- Physical security of data centers
- Hardware and software infrastructure
- Network infrastructure
- Virtualization infrastructure

Although you cannot visit AWS data centers to see this protection firsthand, AWS provides several reports from third-party auditors.