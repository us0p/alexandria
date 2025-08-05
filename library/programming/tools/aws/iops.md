# Input/Output Operations Per Second (IOPS)
Represents the number of read and writes a storage system like an [EBS volume in AWS](aws_ebs_intro.md) can handle **in one second**.

An **I/O operation** is typically:
- A read (getting data from storage)
- Or a write (saving data to storage)

>These operations are often measured in small blocks of data, like **4 KB** or **16 KB** depending on the workload.
## Example
Imagine you have an EBS volume with **5,000 IOPS**:
- It can perform **5,000 read/write operations per second**.
- If each operation is 4 KB, that’s **20 MB/sec of I/O throughput**.
- If your workload exceeds 5,000 operations/sec, you’ll start to see **latency or throttling**.