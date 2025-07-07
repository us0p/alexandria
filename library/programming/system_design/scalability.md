## Vertical Scaling
When you increase the capability of you server by providing it more computational power.
The con is that it there's a limit of our current technology, and obviously, money.
## Horizontal Scaling
Increase the capability of your server by providing more machines instead of increasing the computational power, now you're not limited to our current level of technology and you can use cheaper machines.
The con is that your architecture becomes more complex.
## Load Balancing
Used to distribute traffic among the now many machines that compose the architecture in an horizontal scaling.
Because of this load balancer we can make our servers use private ip addresses decreasing attack surface.
It receives the requests from the web and then forward it to an available machine. It balances the load on each server strategies:
- Based on the load of each machine, creates a even distribution of load among the machines but increase complexity by querying the server to know how busy each server is.
- Round Robin, send each request to a different machine at the time and once it gets to the last machine it rounds back to the first and so on. It is simpler to implement, but it can cause a lot of stress on a particular machine as it doesn't have any mean of measuring the load on a particular server. It can also be configured in the DNS server, and it will return a different IP address each time the DNS is queried, but remember, each client caches the returned the IP address which means that a particular client can be stuck with a particular server for a unspecified period of time, potentially increasing the load on that server.

To avoid single point of failure in load balancers, you can have more than one and they can function in active-active mode.
In active-active mode, you have a pair of load balancers that are actively listening for connections and either one can receive packets from the internet. They communicate between them selves by sending heart-beats, this way one can know if the other has stop functioning.
Or you can have the active-passive mode, that when the active goes down, the passive promotes himself to active and takes over its IP address so it can now receive all the connections.

Geography based load balance: the dns server redirects the user to different load balancers in different availability zones. 
## Sticky Sessions
When we split our traffic among many servers there's another problem that arises, sessions.

Each user has a session, that cannot be shared with other users and it must be consistent in any other server that this user access.

So we need a way of providing a session that is consistent across all the servers.

We can use two approaches:
- Shared storage: like database servers, and to avoid a single point of failure we can also distribute the load among more than one server.
- Cookies: can have some reference to the end server it was using so the session of that user can be redirected to that particular server every time.
## Cache
Is a simple key-value store and it should reside as a buffering layer between your application and your data storage.

Whenever your application has to read data it should at first try to retrieve the data from your cache. Only if it's not in the cache should it then try to get the data from the main data source. This is because a cache hols every dataset in RAM and requests are handled as fast as technically possible.

Need to take care with cache invalidation and cache size.

Always do **in-memory** cache like **Memcached** or **Redis**.

There are two patterns of caching your data.
1. **Cache database queries**: Whenever you do a query to your database, you store the result dataset in cache. A hashed version of your query is the cache key. This pattern has several issues. The main issue is the expiration. It is hard do delete a cached result when you cache a complex query. When one piece of data changes like a table cell, you need to delete all cached queries who may include that table cell.
2. **Cached Objects**: In general, see your data as an object like you already do in your code. Let your class assemble a dataset from your database and then store the complete instance of the class or the assembled dataset in the cache. This allows you to easily get rid of the object whenever something did change and makes the overall operation of your code faster and more logical. It also makes asynchronous processing possible. You can have an army of worker server who assemble your objects and the application just consumes the latest cached object and nearly never touches the database anymore.
## Database Replication
Replicate the data from one database to another.

It's commonly applied to SQL databases. It's harder to scale if your application is data intensive (lots of writes and reads).

It uses one of the following strategies to do so:
1. **Mater-Slave**: The master database receives read and writes and replicates the writes to the slaves databases which serves only reads. If the master goes down, one of the slaves is elected to be the new master. The system will not accept any reads during this down time.
2. **Master-Master**: All writes to one master are replicated to the other master and their slaves. In this strategy you don't have a single point of failure in the writes to your database but you increase the execution time of a write and you also have a problem of commiting one transaction and not both, leaving both masters in an different state.

We can also apply a load balancer to our databases to split read/write queries among all the available servers.
## Database Partitioning
Split the data based on a key or pattern in different databases.

It's commonly applied to NoSQL databases.

Easier to scale if your application is data intensive.

For example, we store all the users with names starting with A-M in database 1, and all the users with names starting with N-Z in database 2.
## High Availability
Refers to some kind of relationships between a pair or more servers that are somehow checking each other availability so that if one of them dies, the other takes on the entire burden of the service.

Can be applied to databases or load balancers.
## Clones
Are machines that are replicated to share the application load. They receive the requests from the load balancer.

Every server contains exactly the same code base and does not store any user-related data, like sessions or profile pictures, on local disc or memory.
## Sessions
Need to be stored in a data store which is accessible to all your applications servers. It can be an external database or an external persistent cache, like Redis.
## Asynchronism
There are two ways asynchronism can be done:
1. Do the time-consuming work in advance and serve the finished work with a low request time. Very often, this paradigm is used to turn dynamic content into static content. Pages of a website, maybe built with a massive framework are pre-rendered and locally stored as static HTML files on every change. Often these computing tasks are done on a regular basis, maybe by a script which is called every hour by a cronjob.
2. Do the time-consuming work in the background by putting it in a job queue and immediately signaling the user that the job is under processing. The queue is then constantly checked by workers who process the tasks and signals the user again once the job is done. The basic idea is to have a queue of tasks or jobs that a worker can process.