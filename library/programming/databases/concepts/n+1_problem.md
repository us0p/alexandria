# N+1 Problem
Typically, this happens when you structure your code so that you first do 
a query to get a list of records, then subsequently do another query for 
each of those records.

## Example
You have a recipie table with 4 items.
You have an ingredidient table with N items, each ingredient belongs to a 
recipie.
When you SELECT * FROM recipie, you have your first query.
Depending on how your code is structured, for each recipie you'll SELECT *
FROM ingredients WHERE recipie_id = ?, that's N queries.
Thus your have the N+1 problem.

You might expect that many small queries would be fast and one large, 
complex query will be slow. This is rarely the case. In practice, the 
opposite is true. Each query has to be sent to the database, the database 
has to perform the query, then it sends the results back to your app. The 
more queries you perform, the more time it takes to get the results back, 
with each trip to the database server taking time and resources. In 
contrast, a single query, even if it's complex, can be optimized by the 
database server and only requires one trip to the database, which will 
usually be much faster than many small queries.

## Causes of the N+1 Problem
- Lazy Loading: Many ORM frameworks use lazy loading by default. Lazy 
  loading means that related data is fetched from the database only when 
  it is accessed. This can lead to N+1 queries when developers access 
  related data for each item in a collection.
- Inefficient Queries: Developers may write code that fetches related data 
  in a loop, resulting in multiple database queries when a single 
  optimized query would suffice.
- Lack of Batch Fetching: Batch fetching, a technique provided by some ORM 
  frameworks, allows you to retrieve related data for multiple objects in 
  a single query.

## How to prevent N+1 Problems
To avoid this problem you should fetch all the elements at once, usually
joining the related table in the first query.
