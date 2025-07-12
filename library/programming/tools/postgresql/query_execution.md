![[Pasted image 20250708150426.png]]
## Parse Statement
Parses the SQL
## Traffic Cop
Identifies if this is a query that need to be optimized and executed or merely an utility command
## Query Optimization
### Rewrite Query
Handles things like views and rules
### Optimizer
#### Generate Paths
A number of paths which are possible ways of executing the query and finds the cheapest path.
#### Generate Plan
The sequence of steps, or which path of actions the server needs to execute to actually retrieve that data.
### Executor
Executes the plan
## Decisions the optimizer has to make
- Scan Method
	- Seq Scan
	- Index Scan
	- Bitmap Index Scan
- Join Method
	- Nested Loop
		- With Inner Sequential Scan
			- Very simple join method
			- Only good for small tables
			- No Setup Required
		- With Inner Index Scan
	- Hash Join
		- Used in small tables as the hash must fits in memory.
	- Merge Join
		- Sort tables and after that merge tables together.
		- Ideal for Large Tables.
		- An Index can be used to eliminate the Sort.
- Join Order

>Order of joined relations is insignificant. PostgreSQL has a cots based optimizer so it doesn't matter the position of the statements.

Autovacuum cannot `ANALYZE` temporary tables because these tables are only visible to the creating session.

For values that aren't to common, which often represent 5% or less of your data, it's worthy to start looking at indexes. If not, it's not worthy to access and read all of those index pages to find the data.

For more common data the planner will probably choose to use a sequential scan.

Bitmap Index Scan creates a bitmap of all the matches from the index and then uses that to access the heap. Lest common values end up in this bitmap index scan.

![[Pasted image 20250708162810.png]]

For really rare values the Index Scan is used. Because the values are so sparse, it's worthy to access the index pages to find the values, this will obviously depend on the size of your table.

![[Pasted image 20250708163945.png]]

![[Pasted image 20250708164626.png]]

![[Pasted image 20250708164742.png]]

![[Pasted image 20250708164828.png]]
![[Pasted image 20250708165005.png]]
![[Pasted image 20250708165106.png]]
![[Pasted image 20250708165741.png]]
![[Pasted image 20250708165805.png]]