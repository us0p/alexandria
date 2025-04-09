# Availability Zone - AZ
Is a single data center or a group of data centers within a [Region](aws_region.md).

A [Region](aws_region.md) consists of three or more Availability Zones.

Availability Zones are located tens of miles apart from each other. This is close enough to have low latency (the time between when content requested and received) between Availability Zones. However, if a disaster occurs in one part of the Region, they are distant enough to reduce the chance that multiple Availability Zones are affected.

A best practice is to run applications across at least two Availability Zones in a Region.

Planning for failure and deploying applications across multiple Availability Zones is an important part of building a resilient and highly available architecture.

Many of the AWS services run at the [Region](aws_region.md) level, meaning they run synchronously across multiple Availability Zones without any additional effort on your part.

Regional services are by definition already highly available at no additional cost of effort on your part.
