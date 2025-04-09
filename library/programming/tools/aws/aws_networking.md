## Amazon Virtual Private Cloud (VPC)
It's a networking service that you can use to establish boundaries around your AWS resources.
A VPC lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.

These resources can be public facing so they have access to the internet, or private with no internet access.

The public and private grouping of resources are known as [subnets](#Subnets) and they are ranges of IP addresses in your VPC.
## Internet Gateway
To allow public traffic from the internet to access your VPC, you attach an `internet gatway` to the VPC.

![[Pasted image 20250409082905.png]]

Without an internet gateway, no one can access the resources within your VPC. If you have a VPC that includes only private resources you can use a virtual private gateway.
## Virtual Private Gateway
Is the component that allows protected internet traffic to enter into the VPC. It enables you to establish a `virtual private network` connection between your VPC and a private network, such as an on-premises data center or internal corporate network. It allows traffic into the VPC only if it is coming from an approved network.

![[Pasted image 20250409082934.png]]
## Subnets
Is a section of a VPC in which you can group resources based on security or operational needs. Subnets can be public or private.

- **Public subnets** contain resources that need to be accessible by the public, such as an online store’s website.
- **Private subnets** contain resources that should be accessible only through your private network, such as a database that contains customers’ personal information and order histories. 

In a VPC, subnets can communicate with each other. For example, you might have an application that involves Amazon EC2 instances in a public subnet communicating with databases that are located in a private subnet.

![[Pasted image 20250409083940.png]]
## Network traffic in a VPC
When a customer requests data from an application hosted in AWS, this request is sent as a packet. It enters into a VPC through an internet gateway.

Before a packet can enter into a subnet or exit from a subnet, it checks for permissions. These permissions indicate who sent the packet and how the packet is trying to communicate with the resources in a subnet.

The VPC component that checks packet permissions for subnets is a `network access control list (ACL)`.
## Network `ACL`
It's a `virtual firewal` that controls inbound and outbound traffic at the subnet level.

Imagine that you are in an airport. In the airport, travelers are trying to enter into a different country.
You can think of the travelers as packets and the passport control officer as a network ACL. The passport control officer checks travelers’ credentials when they are both entering and exiting out of the country. If a traveler is on an approved list, they are able to get through. However, if they are not on the approved list or are explicitly on a list of banned travelers, they cannot come in.

Each AWS account includes a default network ACL. When configuring your VPC, you can use your account's default network ACL or create custom network ACL.

By default, your account's default network ACL allows all inbound and outbound traffic, but you can modify it by adding your own rules.

For custom network ACL, all inbound and outbound traffic is denied until you add rules to specify which traffic to allow.

Additionally, all network ACL have an explicit deny rule. This rule ensures that if a packet doesn't match any of the other rules on the list, the packet is denied.
## Stateless packet filtering
ACL perform stateless packet filtering. They remember nothing and check packets that cross the subnet border each way; inbound and outbound.

The network ACL checks the packet response against its list of rules to determine whether to allow or deny.

After a packet has entered a subnet, it must have its permissions evaluated for resources within the subnet, such as EC2 instances.

![[Pasted image 20250409083236.png]]
## Security groups
Is a virtual firewall that controls inbound and outbound traffic.

By default, a security group denies all inbound traffic and allows all outbound traffic.

You can add custom rules to configure which traffic should be allowed; any other traffic would then be denied.

If you have multiple components instances within the same VPC, you can associate them with the same security group or use different security groups for each instance.
## Stateful packet filtering
Security groups perform stateful packet filtering. They remember previous decisions made for incoming packets.

Consider the same example of sending a request from an EC2 instance to the internet. When a packet response for that request returns to the instance, the security group remembers your previous request. The security group allows the response to proceed, regardless of inbound security group rules.

![[Pasted image 20250409083304.png]]

With both network ACL and security groups, you can configure custom rules for the traffic in your VPC.
## Domain Name System - DNS
You can think of DNS as being the phone book of the internet. DNS is the process of translating a domain name to an IP address.
- When you enter the domain name into your browser, this request is sent to a customer DNS resolver.
- The customer DNS resolver asks the company DNS server for the IP address that corresponds to the website.
- The company DNS server responds by providing the IP address for the website, e.g. 192.0.2.0.