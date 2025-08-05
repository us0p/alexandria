## Amazon Elastic Block Store (EBS)
A service that provides block-level storage volumes that you can use with 
EC2 instances. If you stop or terminate an EC2 instance, all the data on 
the attached EBS volume remains available.
Because EBS volumes are for data that needs to persist, it's important to 
back up the data. You can take incremental backups of EBS volumes by 
creating EBS snapshots.

An EBS snapshot is an incremental backup. This means that the first backup
taken of a volume copies all the data. For subsequents backups, only the 
blocks of data that have changed since the most recent.
Incremental backups are different from full backups, in which all the data 
in a storage volume copies each time a backup occurs. 
## EBS characteristics
- Sizes up to 16 TiB
- Survive termination of their EC2 instance
- Solid state by default
- HDD options