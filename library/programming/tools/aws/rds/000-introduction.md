# Amazon Relational Database Service - RDS
Designed to simplify the setup, operation, and scaling of relational databases in the cloud.
Provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.
It supports six database engines:
- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- SQL Server
It also ensures the database is up-to-date with the latest patches, automatically backs up your data and offers encryption at rest and in transit.
- Manages backups, software patching, automatic failure detection, and recovery.
- Automated backups can be turned on, or manually create your own backup snapshots. You can use these backups to restore a database.
- You can get high availability with a primary DB instance and a synchronous secondary DB instance that you can fail over to when problems occur. You can also use read replicas to increase read scaling.

enhanced monitoring
Amazon RDS performance insights
Also supports Amazon CloudWatch metrics
CloudWatch Database Insights consolidates logs and metrics from your applications, databases, and operating systems.
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