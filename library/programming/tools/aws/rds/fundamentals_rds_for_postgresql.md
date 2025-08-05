
- Starting with PostgreSQL 12.5 RDS for Postgre supports `pg_partman` and `pg_cron` extensions.
--- 

## RDS monitoring options
- CloudWatch metrics: CPU/Memory/IOPS/Network, Per-minute metric storage on CloudWatch.
- RDS Enhanced Monitoring: Process/thread list and queries that are running, per-second metric storage on CloudWatch logs.
- RDS Performance insights and amazon CloudWatch database insights: SQL/state/host (enables visualization of database load), pre-built, opinionated dashboards allowing you to see a fleet of instances and which ones are unhealthy and act based on that.
## Parameter group
Database parameters specify how the database is configured. For example, database parameters can specify the amount of resources, such as memory, to allocate to a database.

A DB parameter group acts as a container for engine configuration values that are applied to one or more DB instances.
## RDS security and compliance
RDS instances are in a [VPC](aws_networking.md#Amazon%20Virtual%20Private%20Cloud%20(VPC)) which you can control using [firewalls](firewall.md) and [security groups](aws_networking.md#Security%20Groups) to determine who has access to the instances.

There are multiple authentication and authorization features including [IAM](aws_iam.md) and Active Directory.

Resources and access permissions can also be managed using [IAM](aws_iam.md) Active Directory access, but there's one key point to note.

The rules which are created in the database are ultimately responsible for how they access the objects inside the database. So, the permissions you give to your roles and users will define how the object access will work inside the database.
## Data Encryption
- Encryption at-rest with Amazon KMS.
	- Must be enabled when the DB instance is created.
- Encryption in-transit through TLS/SSL.
	- Supported by default but not enforced. Can be enforced by using parameter groups settings and connection policies.
## RDS Performance Factors
If you see a bottleneck in:
- Compute (CPU)
- Memory (GB of RAM)
- Network Performance (MB/s Throughput)

Then your bottleneck is probably related to your **instance class**.

If you see a bottleneck in IO throughput, then it's most likely related to the **storage type** of the instance.
### Scale storage for larger data sets
- Can scale EBS storage up to 64TiB and IOPS to 256K.
- No downtime for storage scaling.
- Storage auto-scaling option.
## Database server instance types
- **General purpose**: 
	- `T4g`: Usually good for smaller workloads.
	- `M6i`: Optimized for CPU intensive workloads.
- **Memory Optimized**: `R6i`, optimized for high throughput, memory optimized workloads.
- **Graviton**: `M7g/R7g`: Offer the best price performance for most workloads.
## Storage types
RDS uses EBS volumes.
## Auto-scaling
If you have 90% of your storage utilized, **if auto-scaling is enabled**, it'll automatically kick in and will increase it by 10% of the storage.

RDS storage modification for auto-scaling enabled DB instance happen when:
- Free available space is less than or equal to 10% of the allocated storage.
- The low-storage condition last at least five minutes.
- At least six hours have passed since the last storage modification, or storage optimization has completed on the instance, whichever is longer.

The additional storage is in increments of whichever of the following is greater:
- 10 GiB
- 10 percent of currently allocated storage
- Predicted storage growth exceeding the current allocated storage size in the next 7 hours based on the `FreeStorageSpace` metrics from the past hour.
## Configuration files in PostgreSQL
`postgresql.conf`
- Main configuration file to set various PostgreSQL parameters.
- Resides in PostgreSQL data directory.
- Changes typically requires server restart or configuration reload through `pg_reload_conf()`.

`pg_hba.conf`
- Controls client authentication.
- Specify host connectivity, authentication methods & database access required.

Those files are for standard Postgre.

In RDS, this configuration file change is managed by **parameter groups**.

These parameter groups have two types of parameters.
- **static**: parameters which need a reboot of the instance.
- **dynamic**: parameters that do not required a reboot of the instance.
## Connecting to RDS for PostgreSQL
In standard Postgre, the `pg_hba.conf` file tells you who can connect to which database from which host with which authentication method.

In RDS, this is driven by **security groups**.

RDS for PostgreSQL supports different type of authentication methods:
- Password
- Kerberos
- IAM
## High availability
Can be enabled by selecting multi-az
- Synchronous replicates the data to another AZ.
- Physically distinct, independent infrastructure.
- Automatic failover and reinstatement to another AZ in cases of failure.
- Fully managed.

You can make two deployments:
- One primary instance with a standby in another AZ, applies automatic failover if primary goes down.
- Multi-AZ DB cluster with one primary and two readable standby(s), this is semi-synchronous.

Note that the replication system is synchronous, which means that until the time the standby EBS does not commit, the result is not returned to the client.

If the standby is down, the primary doesn't connect to the standby, which means, no performance downtime for the primary.
## RDS multi-az failover (one standby)
**Automatic** failover when:
- Loss of availability in primary AZ
- Loss of network connectivity to primary
- Compute unit failure on primary
- Storage failure on primary
**No automatic** failover when:
- Database operations such as long running queries, deadlocks or database corruption errors.
## Benefits of RDS Multi-AZ
- Certain maintenance activities are applied on the standby first
- Backup operations are taken on the standby
- Database availability is limited to the time failover time (1-2 mins)
- DB endpoint doesn't change after failover
- 99-95% monthly up-time percentage SLA.
## RDS Multi-AZ with two readable standbys
- Readable standbys: **semi-synchronous replication**
- Automatic failover in typically **under 35 secs**.
- Uses separate endpoints for reads and writes.
- Gain up to 2x faster commit transaction commit latency.
- Equipped with fast `NVMe` SSD for local storage, ideal for high speed and low-latency storage.

In semi-synchronous operation with two standbys we don't need to wait for the two standby machines to commit. We're able to commit as soon as one of the server commits.
## Disaster recovery with Amazon RDS
RDS offers disaster recovery with multiple features:
- Setup of external replicas.
## RDS Snapshots
- Build on EBS snapshots.
- Can be manual or automated
	- Automated:
		- Created daily in backup window.
		- Transaction logs stored on S3 every 5 minutes.
		- Maximum retention: 35 days.
	- Manual:
		- Created through tools (Console, CLI, SDK, etc).
		- No retention policy by default.
		- Often created for compliance reasons or for checkpoints.
		- No possibility to replaying WAL logs, because manual snapshot is just a "picture in time" which means that there's no possibility of doing a point in time restore.
- Always incremental
- Can copy them across different AWS regions or accounts
- Consideration on database performance impact:
	- **Single-AZ**: less than 1 sec pause in I/O during creation.
	- **Multi-AZ**: snapshot taken on standby. No performance impact while blocks are being backed up.

**Key points of restoring a database from a snapshot**:
- A new database instance is always created.
- You can restore in the same or different Account/Regions.
- **Use cases**:
	- Test database upgrades or application changes.
	- Clone environments.

**Point-In-Time-Restore**:
- A new database instance is always created.
- Requires automated snapshots.
- Available within the same account.
- Can enable cross-Region automated backups
- **Use cases**:
	- Recover from application error, manual error, or corruption.
	- Recover from the loss of a single-AZ database instance.

To enable cross-region automated backups for RDS you can check the option "backup replication", to send it across regions, automated backups should be enabled.
## RDS read replicas
- Relieve pressure on your primary node with additional read capacity.
- Bring data close to your applications in different regions.
- Promote a read replica to standalone for faster recovery in the event of disaster.

Read replicas is asynchronous, so if you want to promote it, you will have to do it manually.

You can use both in region as well as cross region replicas.

You can also set up external replicas for disaster recovery using logical replication. Logical replication is allowed for both RDS and Aurora Postgre which basically uses logical decoding to form a logical decoded stream which can be used by another Postgre sever.

>High availability = synchronous replication = multi-az setup
>Disaster recovery = asynchronous replication = read replicas

The multi-az setup will be of the same instance class always.

RDS db instance support 5 read replicas in-region.

You can create up to three levels of read replica in a chain(cascade) from a source DB instance.
## Event Subscriptions
Notifies events that occurs in the database, like failovers.
## HA x DR
HA is designed to minimize downtime in the event of failures (hardware, zone, etc). It uses replication and failover mechanisms to ensure the database remains available.

Traditional HA: multi-az with **non-readable** standby
- 1 primary + 1 standby in different AZ (same region)
- semi-synchronous replication
- standby is not readable
- failover is automatic

Newer HA: Multi-AZ DB cluster with Readable standbys
- 1 writer + 2 or more standbys in different AZ (same region)
- semi-synchronous replication
- standby is readable
- failover is automatic

DR is designed for recovery from major disasters like region failures or data corruption. It relies on replicas or backups in another region or system.
- One or more read-only replicas
- same or **cross-region**
- asynchronous replication
- failover is manual, promotion required

Replicas receive changes from the source database after they happen. There can be a delay (replication lag).

In a HA + DR setup, you could have a cluster in region A with a primary and 2 readable-replicas with semi-sync replication and automatic failover.

Then you could create read-replicas in a separate **region** and this replicas would receive replication from the cluster in region A in an async manner.

If region A goes down, you would need to manually promote region B to be the new primary, there's no automatic failover between regions.

```plaintext
Region A (HA Cluster - Multi-AZ)
┌────────────┐   semi-sync   ┌────────────┐
│   Writer   │ ─────────────>│ Standby 1  │
│            │<───────────── │ (Readable) │
│            │ ─────────────>│ Standby 2  │
└────────────┘               └────────────┘

         │
         │ async
         ▼

Region B (DR Cluster - Cross-region)
┌──────────────┐
│ Read Replica │  (Readable, Asynchronous)
└──────────────┘
```
## Monitoring
## CloudWatch
RDS integrates with CloudWatch, and automatically sends metrics to CloudWatch for each active database every minute.

You can monitor individual metrics over a specified time period and take actions based on the metric value relative to a predefined threshold by using CloudWatch alarms.
## Performance Insights
Expands on existing RDS monitoring features to help you detect and troubleshoot database performance issues.

With the performance insights dashboard, you can visualize the database load and filter the load by waits, SQL statements, hosts, or users.

If you have more than one database on a DB instance, Performance Insights will aggregate the performance data.

Turning Performance Insights on or off doesn't cause downtime, a reboot, or a failover. Performance Insights agent consumes limited CPU and memory on the DB host. When the DB load is high, the agent limits the performance impact by collecting data less frequently.

If enabled, Performance Insights can be accessed in the "monitoring" tab of the details of your database instance and by selecting "Performance Insights" in the rightmost dropdown.

The performance insights dashboard is divided into three sections:
- **Counter Metrics**: displays data for performance counters. The default metrics shown are `blks_read.avg` and `xact_commit.avg`, you can choose which performance counters to display in the gear icon.
- **Database Load**: represents the average number of active sessions for the database engine. This metrics is collected every second. An active session is a connection that has submitted work to the database engine and is waiting for a response. 
- **Top Load Items**: Shows top items contributing to database load. By default, the top SQL queries that are contributing to the database load are shown. You can choose to display top wait states, hosts, or users instead.

When PI is activated, it automatically sends the following three metrics to CloudWatch:
- `DBLoad`: Number of active sessions for the DB engine.
- `DBLoadCPU`: The number of active sessions where the wait event type is CPU.
- `DBLoadNonCPU`: The number of active sessions where the wait event type is not CPU.
## RDS Enhanced Monitoring
You can view all system metrics and process information for your Amazon RDS DB instances on the console.
# Troubleshooting
## Replication Lag
Phenomenon that can occur when using read replicas.

**Troubleshooting process**
- Confirm replication lag issue
	1. Examine the CloudWatch metric, **Replication Lag**, for the **read replica**, ensuring that it's not consistently increasing.
	2. Review database logs, messages such as "Streaming replication has stopped" or "Streaming replication has been terminated", signals potential replication problems.
	3. Verify the replication state field for the read replica in RDS console. If it displays "Error", the **Replication Error** field in RDS console or the **event log** can help determine the exact error.
- Collect data
	1. Examine CloudWatch graphs of source RDS instance to understand which activity might contribute to replication lag.
	2. Examine CloudWatch graphs of the read replica to understand possible causes of replication lag. The `ReplicaLag` metric will display the extent to which the read replica is lagging behind.
	3. Access logs for the read replica.
- Analyze data
	1. Examine `ReplicaLag` metric on the read replica, and identify the date and time when the replication lag first started.
	2. Analyze CloudWatch graphs on the source instance to comprehend the workload leading up to the replication lag.
	3. Compare configuration differences between the source and replica instances.
- Apply possible solutions
	1. If a heavy write workload on the source instance is identified. Break your tasks into smaller bundles and distributes them evenly across multiple transactions instead of performing many write activities simultaneously.
	2. If read replica instance class or storage is smaller, it's recommended to scale up so the replica has the same or higher instance.
	3. If long-running queries are identified in log files, try query tuning options to reduce interference with the [WAL](wal.md) replication process.
	4. If long-running active transaction persistent identifiers (PIDs) are identified, you can choose to end the query with `SELECT pg_terminate_backend(PID);`.
	5. Increase the value of the parameter `wal_keep_segments` on the source instance. This increases the number of WAL files that the source instance retains. If not large enough, a read replica might start lagging, and streaming can stop.
	6. If the status of the read replica is **terminated**, it indicates that replication has been stopped for more than 30 consecutive days. Need to re-create read replica from source instance.
- Verify if error has been resolved.
## Read Replica "canceling statement due to conflict with recovery"
Long running queries that conflict with about-to-be-applied WAL entries can be canceled by the replica database.

The error occurs when standby queries conflict with WAL entries that are about to be applied. To resolve this, the queries are cancelled so that WAL can be applied on the standby.
- Confirm error
	1. Check error log of the read replica instance for the following messages "ERROR: Canceling statement due to conflict with recovery. Detail: User query might have needed to see row versions that must be removed". The specific canceled query will follow these messages.
- Collect data
	1. After turning on query logging, examine PostgreSQL logs on the read replica, because it is the queries on the read replica that are being cancelled.
- Analyze
	1. Inspect logs on read replica to determine how frequently the SQL query is cancelled. Also, look for instances where the same SQL query runs successfully and observe the duration of those occurrences.
- Apply solutions, consider setting the following parameters on the read replica.
	1. `hot_standby_feedback`: specifies whether the replica instance sends feedback to the primary instance about queries that are currently running in the replica instance. Resolves error messages by postponing the VACUUM operation on related tables. However, this setting might cause table bloat at the source instance.
	2. `max_standby_streaming_delay`: Pauses the WAL replay in the replica if the source data is modified when read queries are running on the replica. Sets the maximum delay before canceling queries when a hot standby server is processing streamed WAL data. This parameter might result in replication lag.
	3. `max_standbyy_archive_delay`: Also pauses WAL replay in the replica if the source data is modified while read queries are running on the replica. Maximum delay before canceling queries when a hot standby server processes the archived WAL data. This parameter can also cause replication lag.
	4. `vacuum_defer_cleanup_age`: Can be set in the **source instance**, determines the number of transactions by which vacuum and hot cleanup should be deferred, if any. Without setting this parameter, dead row versions might be removed as soon as possible. However, this setting might cause table bloat at the source instance.
- Verify the error has been resolved
## Autovacuum Skipping Tables or Dead Tuples on an Amazon RDS
Database tables and indexes might be getting bloated. This bloating could be causing longer query completion time, leading to a delayed results returned in the mobile application.
- Confirm the issue, specific symptoms:
	- consistent increase in the `n_dead_tup` column for one or multiple tables in PostgreSQL view `pg_stat_user_tables`.
	- `last_autovacuum` and `last_autoanalyze` columns in the same view might not be updating for one or more tables.
	- Finally, autovacuum log entries might reveal a high value in the entry "X are dead but not yet removable" compared to the total tuples for individual or multiple tables, indicating a potential issue.
- Collect data
	- Run the following query to check the number of dead tuples and the last time autovacuum ran on the tables
```SQL
SELECT
  relname AS TableName,
  n_live_tup AS LiveTuples,
  n_dead_tup AS DeadTuples,
  last_autovacuum AS Autovacuum,
  last_autoanalyze AS Autoanalyze
FROM pg_stat_user_tables;
```
- Configure the `log_autovacuum_min_duration` parameter to set a threshold (in ms) for logging autovacuum activities. Autovacuum actions that exceed this threshold will be logged in the `postgresql.log` file. To capture all autovacuum activity, set the parameter's value to 0. This will ensure that even the shortest duration autovacuum actions are logged to provide a comprehensive analysis. 
- Analyze data
	- To determine if there any long-running transactions currently existing in your database, the following query, which identifies transactions that have been running for mare than 5 minutes
```SQL
SELECT
  now() - query_start as Running_Since,
  pid,
  datname,
  usename,
  application_name,
  client_addr,
  left(query, 60)
FROM pg_stat_activity
WHERE state in ('active', 'idle in transaction')
  AND (now() - query_start) > interval '5 minutes';
```
- Run the following SQL query to determine what locks currently exist in your database
```SQL
SELECT
  locktype,
  database,
  relation,
  virtualxid,
  transactionid,
  virtualtransaction,
  pid,
  mode,
  granted
FROM pg_locks;
```
- Apply possible solutions
	- Autovacuum will not clean up dead tuples if one or more transactions are accessing outdated versions of the data. As a result, autovacuum logging reports the number of tuples that are dead but not yet removable. To address this issue, we recommended that you review your transactions as advised in the previous sections and reduce long-running transactions through query tuning wherever possible. Additionally, make sure that any sessions that are idle in transaction are cleaned up promptly by the application logic.
	- To run a vacuum on a table, the autovacuum process must acquire a SHARE UPDATE EXCLUSIVE lock. This can conflict with certain other locks. Autovacuum will skip a table if a transaction has a lock on it or cancel an existing vacuum on a table if another transaction requires a lock on the table.
- Verify issue is no longer appearing
	- Review PostgreSQL view `pg_stat_user_tables` to confirm whether the `n_dead_up` column has decreased for individual or multiple tables.
	- Additionally, check the same view to ensure that the `last_autovacuum` and `last_autoanalyze` columns are now being updated for individual or multiple tablesa
	- Examine the autovacuum log entries to verify if lower values are now appearing under "X are dead but not yet removable" compared to the total tuples for individual or multiple tables.
## Increasing `MaximumUsedTransactionID` CloudWatch metric
PostgreSQL databases can manage up to two billion in-flight unvacuumed transactions before taking drastic measures to prevent data loss.

When the number of unvacuumed transactions approaches the limit, the log issues a warning that vacuuming is required.

If the limit is reached, PostgreSQL switches the database to read-only mode and necessitates an offline, single-user, standalone vacuum.

Performing this vacuum can result in multiple hours or even days of downtime.

CloudWatch generates the metric for `MaximumUsedTransactionID` by using the following query:
```PostgreSQL
SELECT max(age(datfrozenxid)) FROM pg_database;
```

If this value consistently rises above the threshold defined by the **autovacuum_freeze_max_age** parameter, it indicates that the autovacuum process might not be completing VACUUM operations in a timely manner.

To determine if autovacuum worker processes are running and to assess the duration of their operation, run the following query:

```PostgreSQL
SELECT
	datname, 
	usename, 
	pid,
	current_timestamp - xact_start AS xact_runtime,
	query AS query
FROM pg_stat_activity
WHERE upper(query) LIKE '%VACUUM%'
ORDER BY xact_start;
```

To confirm the number of autovacuum workers configured on the RDS instance, run the following command:
```PostgreSQL
SHOW autovacuum_max_workers;
```

To confirm the maximum amount of memory allocated for maintenance operations, such as vacuum, run the following command:
```PostgreSQL
SHOW maintenance_work_mem;
```

To prevent transaction ID wraparound within the table, run the following command to confirm the maximum age (in transactions) that a table's `pg_class.relfrozenxid` field can reach before a VACUUM operation is forced:
```PostgreSQL
SHOW autovacuum_freeze_max_age;
```

To determine which databases are aging, run the following query:
```PostgreSQL
SELECT
  datname,
  age(datfrozenxid)
FROM pg_database
ORDER BY 2 DESC
LIMIT 20;
```

To identify which tables are aging in the first database from the previous query, connect to that database and run the following query:
```PostgreSQL
SELECT
   c.oid::regclass AS table_name,
   GREATEST(age(c.relfrozenxid), age(t.relfrozenxid)) AS age,
   pg_size_pretty(pg_table_size(c.oid)) AS table_size
FROM pg_class c
LEFT JOIN pg_class t ON c.reltoastrelid = t.oid
WHERE c.relkind = 'r'
ORDER BY 2 DESC
LIMIT 20;
```

Additionally, be sure to review the CloudWatch metrics for Read IOPS and Write IOPS of the RDS instance. If you observe high Read IOPS and your application workload is low, it's possible that autovacuum is performing a significant amount of disk reads to complete the vacuum operation.

To gain further insights into autovacuum operations, activate logging by setting `rds.force_autovacuum_logging_level` to "log" and `log_autovacuum_min_duration` to "1000." This will help you monitor and understand the performance of autovacuum processes.

To analyze the data, perform the following steps:

1. Based on the results obtained from querying `pg_stat_activity` as described in the previous collect data section, examine the output to identify any long-running autovacuum sessions.
2. Compare the number of autovacuum work processes you observed in the `pg_stat_activity` query with the value of `autovacuum_max_workers` obtained earlier.
3. Determine which tables are aging and how many tables are nearing the age returned by `autovacuum_freeze_max_age`. If a large number of tables are aging, it indicates that autovacuum will soon launch VACUUM operations.

Consider the following possible solutions to successfully resolve the issue: 

1. Increase the value of `autovacuum_max_workers` to a larger number than the current setting. Be aware that this is a static parameter, so a reboot is required for the changes to take effect. Additionally, note that running more VACUUM operations simultaneously will demand more instance resources. Therefore, ensure your current RDS instance has sufficient capacity; otherwise, you might need to scale the instance type and storage, or make other adjustments to accommodate the increased resource requirements.
2. Increase the value of `maintenance_work_mem` to a larger amount. Keep in mind that VACUUM operations can only use up to a maximum of 1GB of memory. Additionally, be aware that when autovacuum runs, memory allocation might reach up to `autovacuum_max_workers` times the `maintenance_work_mem value`. Therefore, ensure your RDS PostgreSQL instance has enough RAM available to accommodate these requirements.

Additionally, you also have the option to manually run **VACUUM FREEZE** on a table or multiple tables that have aged past the `autovacuum_freeze_max_age` value or are even approaching the two billion age mark.
## Major Version Upgrade Failures
When you initiate a major upgrade of the Amazon RDS for PostgreSQL DB instance through the Amazon RDS console or AWS CLI, the status of the instance will change from "Available" to "Upgrading".

However, sometimes the RDS for PostgreSQL upgrade will encounter issues and the upgrade will fail. When that happens, the instance status will return back to "Available" yet the Engine Version will still display the pre-upgraded version number.

During the major version upgrade process, Amazon RDS for PostgreSQL will complete a number of prechecks to identify any issues that might cause the upgrade to fail. The precheck procedure checks all potential incompatible conditions across all databases in the instance.

If the precheck encounters an issue, it creates a log event indicating the upgrade precheck failed. The precheck process details are in an upgrade log named `error/pg_upgrade_precheck.log`.
# PostgreSQL Security
Security for RDS and Aurora PostgreSQL can be managed at three levels:
- AWS identity and Access Management (IAM): Control who can perform management actions on clusters of instances. Your AWS account must have IAM policies that grant the permissions required to perform Amazon RDS management operations.
- Amazon Virtual Private Cloud (Amazon VPC): Aurora DB clusters must be created using Amazon VPC. Devices and Amazon Elastic Compute Cloud (Amazon EC2) instances can open connections to the endpoint and port of the DB instance for Aurora DB clusters in a virtual private cloud (VPC). You must use an Amazon VPC security group to control these connections. These endpoint and port connections can be made using SSL. In addition, firewall rules can control whether devices running at your company can open connections to a DB instance.
- Standard PostgreSQL security management: To authenticate login and permissions for an Aurora DB cluster, you can take the same approach as with a standalone instance of PostgreSQL. Commands such as CREATE ROLE, ALTER ROLE, GRANT, and REVOKE work just as they do in on-premises databases, as does directly modifying database schema tables.
## `rdsadmin` default privileges
When each new object is created, the `rdsadmin` role is automatically created as a security measure. The database administrator (DBA) is assigned the role of `rdsadmin`. DBAs have default privileges to manage the database and other users. This gives the DBA the ability to create other users and roles. The DBA can also determine which users can change passwords.

When you create an RDS DB instance, the DBA has the following default privileges:
- `LOGIN`
- `RDS SUPERUSER`
- `INHERIT`
- `CREATEDB`
- `CREATEROLE`
- `VALID UNTIL 'infinity'`

>This user account cannot be renamed or changed by the DBA or any other `rdsadmin` user.
## Restricting password management
DBAs can restrict password management to a special role by enabling the `rds.restrict_password_commands` parameter in the DB parameter group. This gives the user more control over password management on the client side.

The `rds_superuser` role has a membership for the `rds_password` role by default. This cannot be changed. However, a DBA can assign other roles membership for the `rds_password` role by using the GRANT SQL command.

AWS recommends that membership to `rds_password` be restricted to a few roles that will be used solely for password management. These roles require the CREATE ROLE attribute to modify other roles.
## Connecting to PostgreSQL over SSL
SSL support is available in all AWS Regions for Amazon RDS and Aurora when connecting to PostgreSQL.

Amazon RDS creates an SSL certificate for your Aurora DB cluster when the cluster is created or for your PostgreSQL instance when the instance is created.
## Requiring an SSL connection
You can require that connections to your Amazon RDS instance or Aurora PostgreSQL DB cluster use SSL by using the `rds.force_ssl` parameter.
- **Update `rds.force_ssl`**: By default, the `rds.force_ssl` parameter is set to 0 (off). You can set it to 1 (on) to require SSL for connections to your DB cluster. Updating the `rds.force_ssl` parameter also sets the PostgreSQL SSL parameter to 1 (on) and modifies your DB cluster’s `pg_hba.conf` file to support the new SSL configuration.
- **Set parameter value**: You can set the `rds.force_ssl` parameter value by updating the DB cluster parameter group for your DB cluster.  You must reboot your DB cluster for the change to take effect. The exception is if you are working with a DB cluster other than the primary. If this is true and the SSL parameter is already set to 1, you don't need to reboot your DB cluster.
## Object Security Privileges
Permission to objects inside the database are all managed by the user, or more accurately, the role that user has been assigned.

PostgreSQL enables you to assign different privileges on different objects.

Each object can have separate privileges that provide flexible control of the database.
### **Owners**
Objects need owners. Whenever a user creates an object, they become the owner by default. Users can also create an object on behalf of another user. The owner has full control over the object. Only the owner of an object can drop the object.
### Privileges
- `rds_superuser`: Role with most privileges in the database.
	- Can add extensions.
	- Can view and end other connections.
	- Can grant `rds_superuser` and `rds_replication` to other roles.
- `GRANT` and `REVOKE`: Commands that assign privileges to the roles for objects.
- **DB privileges**: allow a user to take specific actions
	- `CREATE`: The user can create a new database.
	- `CONNECT`: The user can connect to the database. 
	- `TEMP`: The user can create temporary tables while using the database.
- **Schema privileges**
	- `CREATE`: The user can create a new schema.
	- `USAGE`: The user can use the schema, and see objects such as tables. To see information for that schema, the role must have schema usage privileges.
- **Table privileges**: Finer controls based on user roles.
	- `SELECT`
	- `INSERT`
	- `UPDATE`
	- `DELETE`
	- `TRUNCATE`
	- `REFERENCES`
	- `TRIGGER`
- **Function privileges**: The only privilege for a function `EXECUTE` allows a user to run a function.
- **Sequence privileges**: Objects that have an auto-increment field.
	- `USAGE`: The user can run `currval` (current value) and `nextval`.
	- `SELECT`: The user can run `currval`.
	- `UPDATE`: The user can run `nextval` and `setval`. This allows the user to reset the sequences if needed.
- **Column Privileges**: Some table privileges can be applies at a column level.
	- `INSERT`
	- `UPDATE`
	- `DELETE`
## Row-level Security
Enables restrictions to row-level data based on a user’s identity or role. The restriction logic is located in the database tier rather than in the application tier. Row-level security is enforced at the table level.

For example, a company might have a global table that lists sales information for all its offices worldwide. If a DBA only wants sales managers to see the information specific to their location or Region, the DBA can lock down the table. This is done by row-level security to keep them from seeing information about the areas outside their Region.

```PostgreSQL
-- Template for creatin a policy for row-level security.
CREATE POLICY name ON table_name
	[ FOR { ALL | SELECT | INSERT | UPDATE | DELETE } ]
	[ TO { role_name | PUBLIC | CURRENT_USER | SESSION_USER } [, ...] ]
	[ USING ( using_expression) ]
	[ WITH CHECK ( check_expression) ]

-- Creating a policy for SELECT, the user can only see the rows they own.
CREATE POLICY poll ON foo
	FOR SELECT USING (row_owner = CURRENT_USER);

-- policy for INSERT, only the current user can insert new rows
CREATE POLICY pol2 ON foo
	FOR 
		INSERT WITH CHECK -- prevents users for inserting rows for other users.
			(row_owner = CURRENT_USER);

-- policy for UPDATE
CREATE POLICY pol3 ON foo
	FOR UPDATE USING (row_owner = CURRENT_USER)
		WITH CHECK (row_owner = CURRENT_USER);
		
-- policy for DELETE
CREATE POLICY pol4 ON foo
	FOR DELETE USING (row_owner = CURRENT_USER);


-- Create policies for all CRUD methods
CREATE POLICY poll ON bar
	FOR ALL
USING (a IN (SELECT col1 FROM foo WHERE row_owner = CURRENT_USER));
```