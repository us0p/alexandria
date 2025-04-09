aws service offerings
- compute
- storage
- network security
- blockchain
- machine learning
- artificial intelligence
- robot development plaftorms
- video production
- management systems
- obital satellites

ec2 -> virtual servers

pay for what you need, pay only for what you use.

on-premise servers can't be scaled up or down as needed.
on cloud environments you can scale up or down as the stress on your servers varies.

cloud computing is the on-demand delivery of IT resources over the internet
with pay-as-you-go pricing

Deployment models for cloud computing
When selecting a cloud strategy, a company must consider factors such as:
- required cloud application components
- preferred resource management
- tools
- legacy IT infrastructure requirements.

The three cloud computing deployment models are:
- cloud-based: You can build applications on low-level infrastructure that
  requires your IT staff to manage them. Alternatively, you can build them
  using higher-level services that reduce the management, architecting, and
  scaling requirements of the core infrastructure.
- on-premises: Resources are deployged on premises by using virtualization
  and resource management tools.
- hybrid: You might want to use this approach if you have a legacy 
  application that are better maintained on premises or government 
  regulations require your business to keep certain records on premises.

## Cloud benefits
- Trade upfront expense for variable expense: upfront expenses are 
  resources that you would need to investin before using them. Variable 
  expense means you only pay for computing resources you consume.
- Stop spending money to run and maintain data centers: The aggregated 
  cloud usage from a large number of customers results in lower 
  pay-as-you-go prices.
- Stop guessing cpacity: With cloud computing, you don't have to predict 
  how much infrastructure capacity you will need before deploying an 
  application.
- Benefit from massive economies of scale: by using cloud computing, you 
  can achieve a lower variable cost than you can get on your own.
- Increase speed and agility: cloud provides you with more time to 
  experiment and innovate. When computing in data centers, it may take 
  weeks to obtain new resources that you need. By comparison, cloud 
  computing enables you to access new resources within minutes.
- Go global in minutes: The global footpring of the AWS Cloud enables you 
  to deploy applications to customers around the world quickly, while 
  providing them with low latency.

## EC2
Provides secure, resizable compute capacity in the cloud as Amazon EC2 
instances.  
Every application needs raw computing capacity to provide the functionality
the users need.  
When working with cloud, capacity of these servers are virtual, and the 
service you use to gaind access to those servers with virtual capacity is 
the EC2.  
It runs on top of physical host machines manage by aws using virtualization
technology.  
When you spin up an ec2 instance you aren't necessarily taking an entire 
host for yourself.  
Instead, you're sharing the host with multiple other instances otherwise 
known as virtual machines and a hypervisor running on the host machine is 
responsible for sharing the underline physical resources between the
virtual machines.  
This idea of sharing undeline hardware is called `Multitenancy`.
The hypervisor is responsible for coordinating this `Multitenancy` and it's
manage by aws.  
The hypervisor is responsible for isolating the virtual machines from each
other as they share resources from the host.
EC2 instances aren't aware of other instances on the same host.
When you use EC2 you need only to setup the instance with configurations like:
- OS (windows or linux)
- What will run inside the instance
- Network aspects and also what type of request reaches your server or 
  whether they are public or private accessible.
You can scale the number of instances up or down at will.
You can resize your instance or vertical scale it up.

This form of service is also known as Compute as a service or `CaaS`.

## EC2 instances types
Each instance type is grouped under a instance family that are optmized for
certain types of tasks.
Each type offers a variation of:
- cpu
- memory
- storage
- network capacity
You can mix these resources as you need.

EC2 instance families are:
- General purpose: good balance between compute, memory and networking 
  resources, often used for web servers or code repositories.
  Good choice for application in which the resource needs for compute, 
  memory, and networking are rougly equivalent.
- Compute optimized: ideal for compute intense tasks like gaming servers, 
  high performance computing (HPC), scientific modeling.
  Ideal for high performance web servers, compute-intensive applications 
  servers, and dedicated gaming servers. You can also use compute optimized
  instances for batch processing workloads that require processing many 
  transactions in a single group.
- Memory optimized: memory intensive tasks, designed to deliver fast 
  performance for workloads that process large datasets in memory.
  Some examples are, high-performance database or workloads that involves 
  performing real-time processing of a large amount of unstructured data.
- Accelerated computing: often used for floating point number calculations,
  graphics processing, data pattern maching as they use hardware 
  accelerators.
  It uses hardware accelerators, or coprocessors, to perform some functions
  more efficiently than is possible in software running on CPUs.
- Storage optimized: high performance for locally stored data.
  Designed for workloads that require high, sequential read and write 
  access to large datasets on local storage.
  Some workloads suitable for storage optimized instances include 
  distributed file systems, data warehousing applications, and 
  high-frequency online transaction processing (OLTP) systems.

## EC2 prices
**On-demand pricing:** pay for the duration your instance is running for, 
which can be per hour or per second, depending on the instance type and the
OS that you're running. This kind of pricing is good when you're starting a 
new project and want to experience and thes ideas without long term 
commitment.
Another good use is to determine a base line for your average usage.
Ideal for short-term, irregular workloads that cannot be interrupted.
Sample use cases for On-Demand instances include developing and testing 
applications and running applications that have unpredictable usage 
patterns.
It's not recommended for workloads that last a year or longer because these
workloads can experience cost savings using Reserved Instances.

**Reserved Instances:** billing discount applied to the use of On-Demand 
Instances in your account.
There are two available types of Reserved Instances:
- Standard Reserved Instances: good fit if you know the EC2 isntance type 
  and size you need and in which AWS Region you plan to run them.
- Convertible Reserved Instances: If you need to run your EC2 instances in 
  different Availability Zones or different instance types. You trade in a 
  deeper discount when you require flexibility to run your EC2 instances.
At the end of a Reserved Instance term, you can continue using the Amazon 
EC2 instance withour interruption. However, you are charged On-Demand rates
until you do one of the following:
- Terminate the instance.
- Purchase a new Reserved Instance that matches the instance attributes 
  (instance family and size, Regions, platform, and tenancy).
suited for steady-state workloads or ones with 
predictable usage and offer you up to a 75% discount versus On-Demand 
pricing. You qualify for a discount once you commit to a once or three-year
term.

**Savings Plans:** low prices on ec2 usage, in exchange for a commitment to
a consistent amount of usage measured in dollars per hour for a onr or 
three-year term.
This flexible pricing model can therefore provide savings of up to 72% 
compared to On-Demand rates. 
Any usage beyond the commitment is charged ar regular On-Demand rates.
Good option if you need flexibility in your Amazon EC2 usage over the 
duration of the commitment term.
The savings with EC2 instances Savings Plans are similar to the savings 
provided by Standard Reserverd Instances.
Unlike Reserved instances, however, you don't need to specify up front what
EC2 instance type and size, OS, and tenancy to get a discount.
Further, you don't need to commit to a certain number of EC2 instances over
a term. Additionally, sacings plans don't include EC2 capacity reservation 
option.
This can lower prices on your EC2 usage, regardless of instance family, 
size, OS, tenancy, or AWS region.
This also applies to AWS Fargate and AWS Lambda usage, which are serverless
compute options.
You can use AWS Cost Explores to visualize and mange your AWS costs and 
usage over time.
AWS Cost Explores also provides customized recommendations for Savings 
Plans. These recommendations estimate how much you could save on your 
montly Amazon EC2 costs, based on previuos usage and the hourly commitment
amount in a 1-yer or 3-year Savings Plan.

**Spot Instances:** ideal for workloads with flexible start and end times, 
or that can withstand interruptions.
Spot Istances are unused Amazon EC2 computing capacity and offer you cost 
savings at up to 90% of On-Demands prices.
If you make a Spot request and EC2 capacity is available, your Spot 
Instance launches. However, if the capacity is unavailable, the request is
not successful until capacity becomes available. The unavailable capacity 
might delay the launch of your background processing job.
If capacity is no longer available or demand for Spot Instances increases, 
your instance my be interrupted.

**Dedicated Hosts:** physical hosts dedicated for your use for EC2. These 
are usually for meeting certain compliance requirements and nobody else 
will share tenancy of that host.
You can use your existing per-socket, per-core, or per-VM software licenses
to help maintain license compliance.

## Scaling Amazon EC2
Involves beginning with only the resources you need and designing your 
architecture to automatically resopnd to changing demand by scalling out or
in. As a result, you pay  for only the resources you use.

The service that provides this functionality for EC2 instances is Amazon 
EC2 Auto Scalling.
It add or remove EC2 instances in response to changingg application demand.

You can use two approaches:
- **Dynamic Scaling:** responds to changing demand.
- **Predictive Scaling:** automatically schedules the right number of EC2 
  instances based on predicted demand.

To scale faster, you can use dynamic scalling and predictive scaling 
together.

The `size of your Auto Scaling group` set the minimum number of EC2 
instances that launch immediately after you have created the Auto Scaling 
group. This means that at all times, it's also known as `minimum capacity`.
The `desired capacity` set the number of instances, it can be greater than
the `minimum capacity` but if you do not specify ythe desired number of EC2
instances in an Auto Scaling group, the desired capacity defaults to your 
`minimum capacity`.
The `maximum capacity` sets the maximum number of instances to provide.

## Elastic Load Balancing (ELB)
Automatically distributes incoming application traffic across multiple 
resources, such as Amazon EC2 instances.
It acts as a single point of contact for all incoming web traffic to your 
Auto Scaling group.
This means that as you add or remove EC2 instances, these requests route to
the load balancer first.
Them the requests spread across multiple resources that will handle them.
Elast Load Balancing is a regional construct, this means that is runs at 
the Region level rather than on individual EC2 instances, the service is 
automatically highly available with no additional effort on your part.
ELB is automatically scalable. As your traffic grows, ELB is designed to 
handle the additional throughput with no change to the hourly cost.

ELB and EC2 Auto Scaling are separate services that work together to 
provide high performance and availability.

## Amazon Simple Notification Service (SNS)
Is a publish/subscribe service. Using SNS topics, a publisher publishes 
messages to subscribers.
In SNS, subscribers can be web servers, email addresses, Lambda functions, 
or several other options.

## Amazon Simple Queue Service (SQS)
Is a message queuing service. Using SQS, you can send, store, and receive 
messages between software components, without losing messages or requiring
other services to be available. In SQS, an application sends messages into
a queue. A user or service retrieves a messae from the queue, processes it,
and then deletes it from the queue.

## Serverless computing
Serverless means that your code runs on servers, but you do not need to 
provision or manage theses servers.
With serverless computin, you can focus more on innovating new products and
features instead of maintaining servers.
Another benefit of serverless computing is the flexibility to scale 
serverless applications automatically. Serverless computing can adjust the 
aplications' capacity by modifying the units of consumptions, such as 
throughput and memory.

## AWS Lambda
Is a service that lets you run code without needin to provision or manage 
servers.
While using Lambda, you pay only for the compute time that you consume. 
Charges apply onlyy when your code is running.
You set your code to trigger from an event source, such as AWS services, 
mobile applications, or HTTP endpoints.

## Containers
Containers provide you with a standard way to package your application's 
code and dependencies into a single object. You can also use containers for
processes and workflows in which there are essential requirements for 
security, reliability, and scalability.
When running containerized applications, it’s important to consider 
scalability. Suppose that instead of a single host with multiple 
containers, you have to manage tens of hosts with hundreds of containers. 
Alternatively, you have to manage possibly hundreds of hosts with thousands
of containers. At a large scale, imagine how much time it might take for 
you to monitor memory usage, security, logging, and so on.

## Amazon Elastic Container Service (ECS)
Is a highly scalable, high-performance container management system that 
enables you to run and scale containerized applications on AWS.
ECS supports Docker containers.
AWS supports the use of open-source Docker Community Edition and 
subscription-based Docker Enterprise Edition.
With ECS you can use API calls to launch and stop Docker-enabled 
applications.

## Amazon Elastic Kubernetes Service (EKS)
Fully managed service that you can use to run Kubernetes on AWS.

## AWS Fargate
Serverless compute engine for containers. Works with both ECS and EKS.
When usin Fargate, you do not need to provision or manage servers. Fargate 
manages your server infrastructure for you.
You pay only for the resources that are required to run your containers.
## Ways to interact with AWS services
- **AWS Management Console:** web-based interface for accessing and 
  managing AWS services. You can quickly access recently used services and 
  search for other services by name, keyword or acronym. The console 
  includes wizards and automated workflows that can simplify the process of
  completing tasks. You can also use the AWS Console mobile application to 
  perform tasks such as monitoring resources, viewing alarms, and accessing
  billing information.
- **AWS Command Line Interface (CLI):** use to save time when making API 
  requests. It enables the controls of multiple AWS services directly from 
  the command line within one tool. By using AWS CLI, you can automate the 
  actions that your services and applications perform through scripts.
- **Software Development Kits (SDK):** use to access and manage AWS 
  services. SDKs make it easier for you to use AWS services through API 
  designed for your programming language or platform.

## AWS Elastic Beanstalk
Is a service that helps you provision EC2-based environments.
Instead of clicking around the console or writing multiple commands to 
build out your network, EC2 instances, scaling and Elastic Load Balancers, 
you can instead provide your application code and desired configurations to
the AWS Elastic Beanstalk service, which then takes that information and 
builds out your environment for you. AWS Elastic Beanstalk also makes it 
easy to save environment configurations, so they can be deployed again 
easily.
- Adjust capacity
- Load balancing
- Automatic scaling
- Application health monitoring

## AWS Cloud Formation
Allows you to treat your infrastructure as code, it's not limited to 
EC2-based solutions. Allows you to define a wide variety of AWS resources 
in a declarative way using JSON or YAML text-based documents called 
CloudFormation templates.
Once you define your resources in a CloudFormation template, CloudFormation
will parse the template and begin provisioning all the resoures you defined
in parallel. You can run the same CloudFormation template in multiple 
accounts or multiple regions, and it will create identical environments 
across them.
This means that you can build an environment by writing lines of code 
instead of using the AWS Management Console to individually provision 
resources.
It determines the right operations to perform when managing your stack and 
rolls back changes automatically if it detects errors.

## AWS Direct Connect
Service that lets you establish a dedicated private connection between your
data center and a VPC.

!["direct connect"](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1732824000/pyQOXWbI_QH3VNbAxvPixQ/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Module%204%20-%20AWS%20Direct%20Connect.png)

## Amazon Route 53
Is a DNS web service. Amazon Route 53 connects user requests to 
infrastructure running in AWS. It can route users to infrastructure outside
of AWS.
Another feature of Route 53 is the ability to manage the DNS records for 
domain names. You can register new domain names directly in Route 53.

The following example describes how Route 53 and Amazon CloudFront work 
together to deliver content to customers.

## Route 53 routing policies
- Latency-based routing
- Geolocation DNS
- Geoproximity routing
- Weighted round robin

!["CloudFront and Route 53"](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1733162400/ukxv5YovX_2x68VXheSfAg/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Module%208%20-%20Amazon%20Route%2053.png)

- A customer requests data from the application by going to the company's 
  website.
- Amazon Route 53 uses DNS resolution to identifyy the company's 
  corresponding IP address, e.g. 192.0.2.0. This information is sent back 
  to the customer.
- The customer's request is sent to the nearest edge location through 
  Amazon CloudFront.
- Amazon CloudFront connects to the Application Load Balancer, which sends 
  the incoming packet to an Amazon EC2 instance.

## Instance stores
Block-level storage volumes behave like physical hard drives. An instance 
store provides temporary block-level storage for an Amazon EC2 instance. An
instance store is disk storage that is physically attached to the host 
computer for an EC2 instance, and therefore has the same lifespan as the 
instance.
AWS recommends instances stores for use cases that involve temporary data 
that you do not need in the long term.

## Amazon Elastic Block Store (EBS)
A service that provides block-level storage volumes that you can use with 
EC2 instances. If you stop or terminate an EC2 instance, all the data on 
the attached EBS volume remains available.
Because EBS volumes are for data that needs to persist, it's important to 
back up the data. You can take incremental backups of EBS volumes by 
creating EBS snapshots.

!["EBS snapshot"](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1733162400/ukxv5YovX_2x68VXheSfAg/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/EBS_snapshots.png)

An EBS snapshot is an incremental backup. This means that the first backupt
taken of a volume copies all the data. For subsequents backups, only the 
blocks of data that have changed since the most recent.
Incremental backups are different from full backups, in which all the data 
in a storage volume copies each time a backup occurs. 

## EBS characteristics
- Sizes up to 16 TiB
- Survive termination of their EC2 instance
- Solid state by default
- HDD options

## Object storage
In object storage, each object consists of data, metadata, and a key.
The data might be an image, video, text document, or any other type of 
file.
Metadata contains information about what the data is, how it's used, the 
object size, and so on. An object key is its unique identifier.
Unlike block storage services, in object storage services, when a file is 
modified, the entire object is updated.
It's a good model if you consume the files as whole, as each file is 
treated as an object.
It's not a good model if you need to consume and update pieces of your 
files, as for each update, a new object would need to be created.

## Amazon Simple Storage Service (S3)
Is a service that provides object-level storage. It stores data as objects 
in buckets.
You can upload any type of file to S3. S3 offers unlimited storage space. 
The maximum file size for an object in S3 is 5TB.
When you upload a file to S3, you can set permissions to control visibility
and access to it.
You can also use S3 versioning feature to track changes to your objects 
over time.

## S3 storage classes
When selecting an S3 storage class, consider these two factors:
- How often you plan to retrieve your data
- How available you need your data to be

The storage classes are:
- **Standard:** Provides high availability for objects. It has a higher 
  cost than other storage classes intended for infrequently accessed data 
  and archival storage.
  - Designed for frequently accessed data.
  - Stores data in a minimum of three Availability Zones.
- **Standard-Infrequent Access (Standard-IA):** Ideal for data infrequently
  accessed but requires high availability when needed. It provides the same
  level of availability as Standard but with lower storage price and higher
  retrieval price.
  - Ideal for infrequently accessed data.
  - Similar to S3 standard but has lower storage price and higher retrieval
  price.
- **One Zone-Infrequent Access (One Zone-IA):** It stores data in a single 
  Availability Zone. This makes it a good storage class to consider if the 
  following conditions apply:
  - You want to save costs on storage.
  - You can easily reproduce your data in the event of an Availability Zone
  failure.
  - Stores data in a single Availability Zone.
  - Has a lower storage price than S3 Standard-IA.
- **Intelligent-Tiering:** Here, S3 monitors objects' access patterns. If 
  you haven't accessed an object for 30 consecutive days, S3 automatically 
  moves it to the infrequent access tier, Standard-IA. If you access an 
  object in the infrequent access tier, S3 automatically mover it to the 
  frequent access tier, Standard.
  - Ideal for data with unknown or changing access patterns.
  - Requires a small monthly monitoring and automation fee per object.
- **Glacier Instant Retrieval:** When you decide between the options for 
  archival storage, consider how quickly you must retrieve the archived 
  objects. You can retrieve objects stored in the S3 Glacier Instant 
  Retrieval storage class within milliseconds, with the same performance as
  Standard.
  - Works well for archived data that required immediate access.
  - Can retrieve objects within a few milliseconds.
- **Glacier Flexible Retrieval:** Low-cost storage class that is ideal for 
  data archiving. You can retrieve your data from S3 Glacier Flexible 
  Retrieval from 1 minute to 12 hours.
  - Low-cost storage designed for data archiving.
  - Able to retrieve objects within a few minutos to hours.
- **Glacier Deep Archive:** Supports long-term retention and digital 
  preservation for data that might be accessed once or twice in a year. 
  This storage class is the lowest-cost storage in the AWS Cloud, with data
  retrieval from 12 to 48 hours. All objects from this storage class are 
  replicated and stored across at least three geographically dispersed 
  Availability Zones.
  - Lower-cost object storage class ideal for archiving.
  - Able to retrieve objects within 12 hours.
- **Outposts:** Delivers object storage to your on-premises AWS Outposts 
  environment. It's designed to store data durably and redundantly across 
  multiple devices and servers on your Outposts. It works well for
  workloads with local data residency requirements that must satisfy 
  demanding performance needs by keeping data close to on-premises 
  applications.
  - Creates S3 buckets on S3 Outposts.
  - Makes it easier to retrieve, store, and access data on AWS Outposts.

## S3 Characteristics
- Unlimited Storage
- Individual objects up to 5000GBs
- Specialized in write once/read many
- 99.999999999% durability
- Web enabled, every object already has an URL
- Regionally distributed
- Offers cost savings
- Serverless

## Amazon Elastic File System (EFS)
Scalable file system used with AWS Cloud services and on-premisses 
resources.
As you add and remove files, EFS grows and shrings automatically. It can 
scale on demand to petabytes without dirupting applications

In file storage, multiple clients can access data that is stored in shared 
file folders. In this approach, a storage server uses block storage with a 
local file system to organize files. Clients access data through file 
paths.
Compared to block storage and object storage, file storage is ideal for use
cases in which a large number of services and resources need to access the 
same data at the same time.

## Amazon EBS x Amazon EFS
**EBS:**
- Stores data in a single Availability Zone
- To attach an EC2 instance to an EBS volume, both the EC2 instance and EBS
  volume must reside within the same AZ.

**EFS:**
- Stores data in and across multiples AZs.
- The duplicate storage enables you to access data concurrently from all 
  the AZs in the Region where a file system is located. Additionally, 
  on-premises servers can access EFS using Direct Connect.

## Amazon Relational Database Service (RDS)
Is a service that enables you to run relational databases in the AWS Cloud.
It's a managed service that automates tasks such as hardware provisioning, 
database setup, patching, and backups.
You can integrate RDS with other services to fulfill your business and 
operational needs, such as using Lambda to query your database from a 
serverless application.
RDS is available on six database engines:
- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

## Amazon Aurora
It's an enterprise-class relational database. it is compatible with MySQL 
and PostgreSQL. It is up to five times faster than standard MySQL and up to
three times faster than standard PostgreSQL.

## Amazon DynamoDB
Is a key-value database service. It delivers single-digit millisecond 
performance at any scale.
DynamoDB is serverless, which means that you do not have to provision, 
patch, or mange servers.
You also do not have to install, maintain, or operate software.

As the size of your database shrinks or grows, DynamoDB automatically 
scales to adjust for changes in capacity while maintaining consistent 
performance.
This makes it a suitable choice for use cases that require high performance
while scaling.

## Amazon RDS vs Amazon DynamoDB
**RDS:**
- Automatic high availability; recovery provided
- Customer (AWS user) ownership of data
- Customer (AWS user) ownership of schema
- Customer (AWS user) control of network

**DynamoDB:**
- Key-value
- Massive throughput capabilities
- PB size potential
- Granular API access

## Amazon Redshift
Is a data warehousing service that you can use for big data analytics.
It offers the ability to collect data from many sources and helps you to 
understand relationships and trends across your data.
It's massively scalable.
Redshift nodes in multiple petabyte sizes is very common. In fact, in 
cooperation with Amazon Redshift Spectrum, you can directly run a single 
SQL query against exabytes of unstructured data running in data lakes. 
Redshift uses a variety of innovations that allow you to achieve up to 10 
times higher performance than traditional databases, when it comes to these
kinds of business intelligence workloads. 

In order to handle the velocity of real time read/write functionality, most
relational databases tend to function fabulously at certain capacities. The
problem with historical analytics, data that answers questions like, "Show 
me how production has improved since we started", is the data collection 
never stops.
In fact, with modern telemetry and the explosion of IoT, the volume of data
will overwhelm even the beefiest traditional relational database. Not just 
the volume, but the variety of data can be a problem. You want to run 
business intelligence or BI projects against data coming from different 
data stores like your inventory, your financial, and your retail sales 
systems? 
A single query against multiple databases sounds nice, but traditional 
databases don't handle them easily. 
Once data becomes too complex to handle with traditional relational 
databases, you've entered the world of data warehouses. Data warehouses are
engineered specifically for this kind of big data, where you are looking at
historical analytics as opposed to operational analysis. 

## AWS Database Migration Service (DMS)
Enables you to migrate relational databases, nonrelational databases, and 
other types of data stores.
With DMS, you move data between a source and a target database. The source 
and target databases can be of the same type or not.
During the migration, your source database remains operational, reducing 
downtime for any applications that rely on the database.

If the databases are of the same type, they are called, 
`Homogenous databases`, e.g. MySQL to RDS for MySQL, Oracle to RDS for 
Oracle.

The source can be:
- On-premises
- Amazon EC2
- Amazon RDS

The target can be:
- Amazon EC2
- Amazon RDS

You must then create a migration task with connections between the source 
and target databases.

If the database aren't of the same type, the yare called, 
`Heterogeneous databases` and it's a two-step process.
We must first convert the schema structure, data types and database code 
using the AWS Schema convertion tool.
This will convert the Schema and code to match that of the target database.
Then we use DMS to migrate data from the source to the target.

**Some use cases:**
- Development and test database migrations: Enabling developers to test 
  applications against production data without affecting production users.
- Database consolidation: Combining several databases into a single 
  database.
- Continuous replication: Sending ongoing copies of your data to other 
  target sources instead of doing a one-time migration.

## Amazon DocumentDB
Document database service that supports MongoDB workloads (MongoDB is a 
document database program).

## Amazon Neptune
Graph database service. You can use Amazon Neptune to build and run 
applications that work with highly connected datasets, such as 
recommendation engines, frau detection, and knowledge graphs.
Great for social networkings and recommendations.

## Amazon Quantum Ledger Database (QLDB)
Is a ledger database service.
You can use QLDB to review a complete history of all the changes that have 
been made to your application data.
Great for supply chains that need to be tracked with ensurance that nothing
is lost.
Also good for banking and finantial records that requires 100% immutability.

## Amazon Managed Blockchain
Is a service that you can use to create and manage blockchain networks with
open-source frameworks.
Blockchain is a distributed ledger system that lets multiple parties run 
transactions and share data without a central authority.
Same as QLDB but adding descentralization.

## Amazon ElastiCache
Is a service that adds chaching layers on top of your databases to help 
improve the read times of common requests. It supports two types of data 
stores: Redis and MemCached.

## Amazon DynamoDB Accelerator (DAX)
Is an in-memory cache for DynamoDB. It helps improve response times from 
single-digit milliseconds to microseconds.
## AWS Artifact
Depending on your company's industry, you may need to uphold specific 
standards. An audit or inspection will ensure that the company has met 
those standards.
Artifact is a service that provides on-demand access to AWS security and 
compliance reports and select online agreements.
AWS Artifact consists of two main sections: AWS Artifact Agreements and AWS
Artifact Reports.
- **Artifact Agreements:** You can review, accept, and manage agreements 
for an individual account and for all your accounts in AWS Organizations. 
Different types of agreements are offered to address the needs of customers
who are subject to specific regulations, such as the Health Insurance 
Portability and Accountability Act (HIPAA).
- **Artifact Reports:** Provide compliance reports from third-party 
auditors. These auditors have tested and verified that AWS is compliant 
with a variety of global, regional, and industry-specific security 
standards and regulations. AWS Artifact Reports remains up to date with the
latest reports release. You can provide the AWS audit artifacts to your 
auditors or regulators as evidence of AWS security controls.
## Customer Compliance Center
Contains resources to help you learn more about AWS compliance.
In there you can read customer compliance stories to discover how companies
in regulated industries have solved carious compliance, governance, and 
audit challenges.
You can also access compliance whitepapers and documentation on topics such
as:
- AWS answers to key compliance questions
- An overview of AWS risk and compliance
- An auditing security checklist
## AWS Shield
Is a service that protects applications against `DDoS` attacks. It provides
two levels of protection:
- **Standard:** Automatically protects all AWS customers at no cost. It 
  protects your AWS resources from the most common, frequently ocurring 
  types of DDoS attacks. As network traffic comes into your applications,
  AWS Shield Standard uses a variety of analysis techniques to detect 
  malicious traffic in real time and automatically mitigates it.
- **Advanced:** is a paid service that provides detailed attack diagnostics
  and the ability to detect and mitigate sophisticated DDoS attacks. It 
  also integrates with other services such as Amazon CloudFront, Amazon 
  Route 53, and Elastic Load Balancing. Additionally, you can integrate AWS
  Shield with AWS WAF (Web Application Firewall) by writing custom rules to
  mitigate complex DDoS attacks.
## AWS Key Management Service (KMS)
Enables you to perform encryption operations through the use of 
cryptographic keys. A cryptographic key is a random string of digits used
for locking (encrypting) and unlocking (decrypting) data. You can use KMS
to create, mange, and use cryptographic keys. You can also control the 
use of keys across a wide range of services and in your applications.
You can choose the specific levels of access control that you need for your
keys.
For example, you can specify which IAM users and roles are able to manage 
keys. Alternatively, you can temporarily disable keys so that they are no 
longer in use by anyone. Your keys never leave AWS KMS, and you are always 
in control of them.
## AWS Web Application Firewall
Lets you monitor network requests that come into your web applications.
It works together with CloudFront and Load Balancers. Recall the 
`network access control list (ACL)`. WAF works in a similar way to block or
allow traffic. However, it does this by using a `web access control list`.
Suppose that your application has been receiving malicious network requests
from several IP addresses. You want to prevent these requests from 
continuing to access your application, but you also want to ensure that 
legitimate users can still access it. You configure the web ACL to allow 
all requests except those from the IP addresses that you have specified.
When a request comes into AWS WAF, it checks against the list of rules that
you have configured in the web ACL. If a request does not come from one of 
the blocked IP addresses, it allows access to the application.
## Amazon Inspector
It helps to improve the security and compliance of applications by running 
automated security assessments. It checks applications for security 
vulnerabilities and deviations from security best practices, such as open 
access to Amazon EC2 instances and installations of vulnerable software 
versions.
After Amazon Inspector has performed an assessment, it provides you with a 
list of security findings. The list prioritizes by severity level, 
including a detailed description of each security issue and a 
recommendation for how to fix it.
## Amazon GuardDuty
Is a service that provides intelligent threat detection for your AWS 
infrastructure and resources. It identifies threats by continuously 
monitoring the network activity and account behavior within your AWS 
environment.
After you have enabled GuardDuty for your AWS account, GuardDuty begins 
monitoring your network and account activity. You do not have to deploy or 
manage any additional security software. GuardDuty then continuously 
analyzes data from multiple AWS sources, including VPC Flow Logs and DNS 
logs. 
If GuardDuty detects any threats, you can review detailed findings about 
them from the AWS Management Console. Findings include recommended steps 
for remediation. You can also configure AWS Lambda functions to take 
remediation steps automatically in response to GuardDuty’s security 
findings.

## Cloud Watch
Web service that enables monitoring and managing of various metrics and the
possibility to configure alarm and actions based on data from those 
metrics.

## CloudTrail
Records API calls for your account. The recorded information includes the 
indentity of the API caller, the time of the API call, the source IP 
address of the API caller, and more.

## Trusted Advisor
Web service that inspects your AWS environment and provides real-time 
recommendations in accordance with AWS best practices.
It compares its findings to AWS best practices in five gategories:
1. cost optmization: Includes checks for unused or idle resources that 
   could be eliminated and provide cost savings.
2. performance: Helps improve the performance of services by providing 
   recommendations for how to take advantage of provisioned throughput.
3. security: Includes checks that review permissions and identify which AWS
   security features to enable.
4. fault tolerance: Includes checks to help improve an application's 
   availability and redundancy.
5. service limits

## AWS Free Tier
Enables you to begin using certain services without having to worry about 
incurring costs for the specified period.
Three types of offers are abailable:
- Always free, for example, AWS Lambda allows 1 million free requests and 
  up to 3.2 million seconds of compute time per month.
- 12 Months free following your initial sign-up date to AWS.
- Trials, short term offers that start from the date you activate a 
  particular service. The length of each trial might vary by number of days
  or the amount of usage in the service.

## How AWS pricing works
- **Pay for what you use:** For each service, you pay for exatcly the 
  amount of resources that yyou actually use, without requiring long-term 
  contracts or complex licensing.
- **Pay less when you reserve:** Some services offer reservation options 
  that provide a significant discount compared to On-Demand instance 
  pricing.
- **Pay less with volume-based discounts when you use more:** Some services
  offer tiered pricing, so the per-unit cost is incrementally lower with 
  increased usage.

## AWS Pricing Calculator
Lets you explore AWS services and create an estimate for the cost of your 
use cases on AWS. You can organize your AWS estimates by groups that you 
define. A group can reflect how your company is organized, such as 
providing estimates by cost center.

## Consolidated billing
AWS Organizations provides the option for consolidated billing, which is a 
feature that enables you to receive a single bill for all AWS accounts in 
your organization. By consolidating, you can easily track the combined 
costs of all the linked accounts in your organization. The default maximum 
number of accounts allowed for an organization is 4, but you can contact 
AWS Support to increase your quota.

## AWS Budgets
Lets you create budgets to plan your service usage, service costs, and 
instance reservations.
The information in AWS Budget updates three times a day.
You can also set custom alerts when your usage exceeds (or is forecasted to
exceed) the budgeted amount.

## AWS Cost Explorer
A tools that lets you visualize, understand, and manage your AWS costs and 
usage over time.
It provides a default report of the costs and usage for your top five 
cost-accruing AWS services. You can apply custom filters and groups to 
analyze your data.

## AWS Support 
A group of four different support plans that help you troubleshoot issues, 
lower costs, and efficiently use AWS services.
- Basic: Free
- Developer
- Business
- Enterprise On-Ramp
- Enterprise

The enterprise On-Ramp and enterprise support plans include access to a 
**Technical Account Manager (TAM)**

## AWS Marketplace
Is a digital catalog that includes thousands of software listings from 
independent software vendors. You can use it to find, test and buy software
that runs on AWS.

## Cloud Adoption Framework (CAF)
It organizes guidance into six areas of focus, called **Perspectives**.
Each perspective addresses distinct responsibilities. The planning process 
helps the right people across the organization prepare for the changes 
ahead.

In general, the **Business, People, and Governance** perspectives focus on 
business capabilities, whereas the **Platform, Security, and Operations** 
perspective focus on technical capabilities.

- Business Perspective: Ensures that IT aligns with business needs and that
  IT investments link to key business results.
- People Perspective: Supports development of an organization-wide change 
  management strategy for successful cloud adoption.
- Governance Perspective: Focuses on the skills and processes to align IT 
  strategy with business strategy. This ensures that you maximize the 
  business value and minimize risks.
- Platform Perspective: Includes principles and patterns for implementing 
  new solutions on the cloud, and migrating on-premises workloads to the 
  cloud.
- Security Perspective: Ensures that the organization meets security 
  objectives for visibility, auditability, control, and agility.
- Operations Perspective: Helps you to enable, run, use, operate, and 
  recover IT workloads to the level agreed upon with your business 
  stakeholders.

## 6 strategies for migration (6 r's)
When migrating applications to the cloud, six of the most common migrations
strategies that you can implement are:
- Rehosting: aka "lift-and-shift" involves moving applications without 
  changes.
- Replatforming: aka "lift, tinker, and shift", involves making a few cloud
  optimizations to realize a tagible benefit. Optimization is achieved 
  without changing the core architecture of the application.
- Refactoring: Involves reimagining how an application is architected and 
  developed by using cloud-native features.
- Repurchasing: Involves moving from a traditional license to a 
  software-as-a-service model.
- Retaining: Consists of keeping applications that are critical for the 
  business in the source environment. This might include applications that 
  require major refactoring before they can be migrated, or, work that can 
  be postponed until a later time.
- Retiring: Process of removing applications that are no longer needed.

## AWS Snow Family
Are a collection of physical devices that help to physically transport up 
to exabytes of data into and out of AWS.

- Snow Cone: Small, rugged, and secure edge computing and data transfer 
  device.
- Snowball: offers two types of devices:
    - Snowball Edge Storage Optimized: Devices are well suited for 
      large-scale data migrations and recurring transfer workflows, in 
      addition to local computing with higher capacity needs.
    - Snowball Edge Compute Optmized: Provides powerful computing resources
      for use cases such as machine learning, full motion video analysis, 
      and local computing stacks.
- Snowmobile: An exabyte-scale data transfer service used to move large 
  amounts of data to AWS.

## Artificial Intelligence
- Convert speech to text with Amazon Transcribe.
- Discover patterns in text with Amazon Comprehend.
- Identify potentially fraudulent online activities with Amazon Fraud 
  Detector.
- Build voice and text chatbots with Amazon Lex.
- Remove the difficult work of development of machine learning with 
  SageMaker.
- Amazon Augmented AI (Amazon A2I) provides built-in human review workflows 
  for common machine learning use cases, such as content moderation and 
  text extraction from documents. With Amazon A2I, a person can also 
  create their own workflows for machine learning models built on Amazon 
  SageMaker or any other tools.

## Amazon Q Developer
Machine learning-powered code generator that provides you with code 
recommendations in real time.

## AWS Well-Architected Framework
Helps you understand how to design and operate reliable, secure, efficient,
and cost-effective systems in the AWS Cloud.
It's based on six-pillars
- Operational excellence: Ability to run and monitor sstems to deliver 
  business value and to continually improve supporting processes and 
  procedures. Design principles for operational excellence in the cloud 
  include performing operations as code, annotating documentation, 
  anticipating failure, and frequently making small, reversible changes.
- Security: Ability to protect information, systems, and assets while 
  delivering business value through risk assessments and mitigation 
  strategies.
- Reliability: Ability of a system to, Recover from infrastructure or 
  service disruption, dynamically acquire computing resources to meet 
  demand, mitigate disruptions such as misconfigurations or transient 
  network issues. It includes testing recovery procedures, scaling 
  horizontally to increcase aggregate syystem availability, and 
  automatically recovering from failure.
- Performance efficiency: Ability to use computing resources efficiently to
  meet sstem requirements and to maintain that efficiency as demand changes
  and technologies evolve.
- Cost optmization: Ability to run systems to deliver business value at the
  lowest price point, it includes adopting a consumption model, analyzing 
  and attributing expenditure, and using managed services to reduce the 
  cost of ownership.
- Sustainability: Ability to continually improve sustainability impacts by 
  reducing energy consumption and increasing efficienc across all 
  components of a workload by maximizing the benefits from the provisioned 
  resources and minimizing the total resources required.
