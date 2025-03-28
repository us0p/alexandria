# Amazon Relational Database Service - RDS
Designed to simplify the setup, operation, and scaling of relational databases in the cloud.
Provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.
## Supported engines
It supports six database engines:
- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- SQL Server
## AWS Responsibilities
It also ensures the database is up-to-date with the latest patches, automatically backs up your data and offers encryption at rest and in transit.
- Manages backups, software patching, automatic failure detection, and recovery.
- Automated backups can be turned on, or manually create your own backup snapshots. You can use these backups to restore a database.
- You can get high availability with a primary DB instance and a synchronous secondary DB instance that you can fail over to when problems occur. You can also use read replicas to increase read scaling.
- You can control access by using AWS Identity and Access Management (IAM) to define users and permissions.
- You can also help protect your databases by putting them in a VPC.

With RDS you are only responsible for the application optimization, AWS takes care of the [rest](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html#Welcome.Concepts.comparison)

You are responsible for query tuning, which is highly dependent on database design, data size, data distribution, application workload, and query patterns. Monitoring and tuning are highly individualized processes that you own for your RDS databases.

You can use RDS Performance Insights and other tools to identify problematic queries.

[Amazon RDS application architecture: example](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html#Welcome.Concepts.DBInstance.architecture)

Support for RDS features varies across AWS Regions and specific version of each DB engine.
[Supported features in RDS by AWS Region and DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDSFeaturesRegionsDBEngines.grids.html)

## Multi-AZ deployments
You can run you DB instance in several AZ, an option called Multi-AZ deployment. When you choose this option, Amazon automatically provisions and maintains one or more secondary standby DB instance in a different AZ. Your primary DB instance is replicated across AZ to each secondary DB instance.
- Provides data redundancy and failover support
- Eliminates I/O freezes
- Minimize latency spikes during system backups
- Serving read traffic on secondary DB instance (Multi-AZ DB clusters deployment only)
[Configuring and managing a Multi-AZ deployment for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
## RDS monitoring
You can track the performance and health of your DB instances using various automated and manual tools:
### Amazon RDS DB instance status and recommendations
View details about the current status of your instance by using the RDS console, AWS CLI, or RDS API.
[Recommendations from RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)
### Amazon CloudWatch metrics for Amazon RDS
You can use CloudWatch service to monitor the performance and health of a DB instance. CloudWatch performance charts are shown in the RDS console.
RDS automatically sends metrics to CloudWatch every minute for each active database. You don't get additional charges for RDS metrics in CloudWatch.
Using CloudWatch alarms, you can watch a single Amazon RDS metric over a specific time period. You can then perform one or more actions based on the value of the metric relative to a threshold that you set.
[Monitoring Amazon RDS metrics with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html)
### Amazon RDS Performance insights and operating-system monitoring
Performance insights assesses the load on your database, and determine when and where to take action.
RDS Enhanced Monitoring looks at metrics in real time for the operating system.
[Monitoring DB load with Performance Insights on RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
[Monitoring OS metrics with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
## How are you charged for RDS
When you use RDS, you can choose to use on-demand DB instances or reserved DB instances.
[DB instance billing for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_DBInstanceBilling.html)
[RDS pricing information](https://aws.amazon.com/rds/pricing)
## Resources
[RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
[Release notes for Amazon relational database service (RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/Welcome.html)
[Back to Basics: How to implement a Multi-Region Disaster Recovery Strategy Using AWS DRS](https://www.youtube.com/watch?v=OT1EJ_kyP_g)
[Optimizing PostgreSQL Running on Amazon EC2 Using Amazon EBS](https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/optimizing-postgresql-on-ec2-using-ebs.html?did=wp_card&trk=wp_card)
[Automate the replication of RDS instances across AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-replication-of-amazon-rds-instances-across-aws-accounts.html?did=pg_card&trk=pg_card)
[Migrating on-premises PostgreSQL databases to Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/introduction.html?did=pg_card&trk=pg_card)
[Enable encrypted connections for PostgreSQL DB instances](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-encrypted-connections-for-postgresql-db-instances-in-amazon-rds.html?did=pg_card&trk=pg_card)
[Schedule jobs for Amazon RDS for PostgreSQL and Aurora PostgreSQL by using Lambda and Secrets Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager.html?did=pg_card&trk=pg_card)
[Use CCM and QPM to optimize recovery performance and execution plans in Aurora PostgreSQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/ccm-and-qpm-aurora-postgresql/welcome.html)
[Connect by using an SSH tunnel in pgAdmin](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/connect-by-using-an-ssh-tunnel-in-pgadmin.html?did=pg_card&trk=pg_card)
[Load BLOB files into TEXT by using file encoding in Aurora PostgreSQL - Compatile](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/load-blob-files-into-text-by-using-file-encoding-in-aurora-postgresql-compatible.html?did=pg_card&trk=pg_card)
[Implementing managed PostgreSQL for multi-tenant SaaS applications on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/welcome.html)
[Increasing application scalability, performance, and availability by using RDS Proxy](https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-proxy/introduction.html?did=pg_card&trk=pg_card)
[Migrate an on-premises PostgreSQL database to Aurora PostgreSQL](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-postgresql-database-to-aurora-postgresql.html?did=pg_card&trk=pg_card)
[Rotate database credentials without restarting containers](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/rotate-database-credentials-without-restarting-containers.html?did=pg_card&trk=pg_card)
[Back to basics: Disaster recovery on regional databases](https://www.youtube.com/watch?v=A4Z5wvkHIZE)
[Back to Basics: Using AWS config and conformance packs to optimize your database](https://www.youtube.com/watch?v=GOLFuz-h9yc)
[Back to Basics: Secure Database Replication Between AWS Accounts](https://www.youtube.com/watch?v=caiNIgDxuNc)
[Enforce automatic tagging of RDS databases at launch](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enforce-automatic-tagging-of-amazon-rds-databases-at-launch.html?did=pg_card&trk=pg_card)
[Database caching strategies using Redis](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/welcome.html?did=wp_card&trk=wp_card)
[Encrypt an existing RDS for PostgreSQL DB instance](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/encrypt-an-existing-amazon-rds-for-postgresql-db-instance.html?did=pg_card&trk=pg_card)
[Automate backups for RDS for PostgreSQL DB instances by using AWS Batch](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch.html?did=pg_card&trk=pg_card)
[Transport PostgreSQL databases between two Amazon RDS DB instances using pg_transport](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg_transport.html?did=pg_card&trk=pg_card)
[Migrate from PostgreSQL on EC2 to RDS for PostgreSQL using pglogical](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-postgresql-on-amazon-ec2-to-amazon-rds-for-postgresql-using-pglogical.html?did=pg_card&trk=pg_card)
[Tuning PostgreSQL parameters in RDS and Aurora](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-postgresql-parameters/introduction.html)
[Streamline PostgreSQL deployments on EKS by using PGO](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-postgresql-deployments-amazon-eks-pgo.html?did=pg_card&trk=pg_card)
[Back to Basics: Disaster Recovery Patterns for Serverless Applications](https://www.youtube.com/watch?v=257chgorDAo)
[Back to Basics: Building Data Domains for Simplified Data Collaboration at Scale](https://www.youtube.com/watch?v=iENbT3xrJHQ)
[Disaster recovery strategy for databases on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/welcome.html)
[Automatically stop and start an RDS DB instance using AWS System Manager Maintenance Windoes](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-stop-and-start-an-amazon-rds-db-instance-using-aws-systems-manager-maintenance-windows.html?did=pg_card&trk=pg_card)
[Back to Basics: Database Sharding to Horizontally Scale Databases](https://www.youtube.com/watch?v=9q-ZA6WtVy4)
[Creating and connecting to a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
[The business value of RDS](https://d1.awsstatic.com/product-marketing/RDS/IDC%20Business%20Value%20of%20Amazon%20RDS%20Whitepaper%202024.pdf)
[PostgreSQL security best practices](https://d1.awsstatic.com/Amazon%20Aurora%20PostgreSQL%20and%20Amazon%20RDS%20for%20PostgreSQL%20Security%20Whitepaper.pdf)
[Maintenance activities for PostgreSQL databases in RDS and Aurora to avoid performance issues](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/introduction.html)