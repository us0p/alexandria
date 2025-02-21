# PACELC - (Partition, Availability, Consistency Else Latency, Consistency)
One of the questions that CAP Theorem wasn’t able to answer was “what 
happens when there is no Partition, What Logical Combination then a 
Distributed System have?“. So to answer this, In addition to Consistency, 
Availability, and Partition Tolerance it also includes Latency as one of 
the desired properties of a Distributed System.
It states that in the case of Network Partition a distributed system can 
have tradeoffs between Availability and Consistency Else if there is no 
Network Partition then a distributed system can have tradeoffs between 
Latency and Consistency.

## Latency in PACELC Theorem
One of the major pitfalls of the CAP Theorem was it did not make any 
provision for Performance or Latency, in other words, CAP Theorem didn’t 
provide tradeoffs when the system is under normal functioning or 
non-partitioned.
Consider a scenario, in which you are making a request to Signup up and 
getting the confirmation after an hour. According to the CAP theorem, this 
system is available but such latency is unacceptable in any real-world 
application.

Note that prioritizing consistency may result in increcased latency, while 
in others, prioritizing latency may lead to reduced consistency.
