# Materialized View
Stores a query's results rather than calculating them on the fly like regular [views](038-views.md).

While a regular SQL view is a saved SQL query that generates its results dynamically each time it is accessed, a materialized view pre-computes and stores the data in a table-like structure.

>Materialized views must be refreshed manually in order to update its data. It's a good choice when you don't need up to date data.

```postgresql
CREATE MATERIALIZED VIEW view_name AS <query>;
```
## Refreshing a materialized view in SQL
### Manual Refresh
Refreshed only when explicitly requested by the user.

This approach gives the most control over when data is updated, making it suitable for scenarios where data changes infrequently, or updates are performed during off-peak hours.

```postgresql
REFRESH MATERIALIZED VIEW view_name;
```
### Periodic Refresh
The materialized view is automatically refreshed at specified intervals during the refresh period, ensuring data is up-to-date without user intervention.

This method is useful for time-sensitive applications where data needs to be relatively current.

```postgresql
CREATE MATERIALIZED VIEW view_name
REFRESH COMPLETE START WITH (SYSDATE) NEXT (SYSDATE + 1/24)
AS
-- ...
```
### On-demand refresh
Occurs whenever the underlying data changes, typically through a trigger mechanism. This ensures that the materialized view always contains the updated data.
## Full vs Incremental Refreshes
- **Full Refresh**: Reloads the entire dataset, replacing all existing data in the view.
	- Simpler to implement.
	- Slower as it updates the whole data set.
- **Incremental Refresh**: Updates only the changed portions of the view.
	- Faster as it updates only the modified data.
	- Requires additional setup.
	- **Not directly applicable to PostgreSQL**
## Best Practices for Materialized Views
- **Choosing the Right Queries to Materialize**: Materialize complex, resource-intensive queries such as joins, aggregations, and subqueries.
- **Using Materialized Views to Optimize Query-Heavy Workloads**: Leverage materialized views for BI reports and dashboards where quick response times are essential. You can also index the columns used in materialized views for faster filtering and sorting.
- **Storage Overhead**: Materialized views store query results physically on disk, which increases storage requirements. To avoid consuming unnecessary storage space, only materialize views for resource-intensive queries and partition the materialized views for large datasets.
- **Update Costs and Refresh Overhead**: Keeping materialized views in sync with the underlying tables can be resource-intensive, especially for views that require frequent updates or involve complex calculations. To avoid the refresh overhead, use incremental refresh where supported or set the appropriate refresh intervals when database usage is lower.