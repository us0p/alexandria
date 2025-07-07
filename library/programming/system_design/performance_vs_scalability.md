# Performance vs Scalability
A service is scalable if it results in increased performance in a manner proportional to resources added.

Generally, increasing performance means serving more units of work, but it can also be used to handle larger units of work, such as when datasets grow.

Another way of looking:
- If you have a **performance** problem, your system is slow for a single user.
- If you have a **scalability** problem, your system is fast for a single user but slow under heavy load.

In distributed systems there are other reasons for adding resources to a system; for example, to improve the reliability of the offered service, introducing redundancy is an important first line of defense against failures.

An always-on service is said to be scalable if adding resources to facilitate redundancy does not result in a loss of performance.

Why is scalability so hard? Because scalability cannot be an after-thought. It requires applications and platforms to be designed with scaling in mind, such that adding resources actually results in improving the performance or that if redundancy is introduced the system performance is not adversely affected.

A second problem area is that growing a system through scale-out generally results in a system that has to come to terms with heterogeneity. Heterogeneity means that some nodes will be able to process faster or store more data than other nodes in a system and algorithms that rely on uniformity either break down under these conditions or underutilize the newer resources.


