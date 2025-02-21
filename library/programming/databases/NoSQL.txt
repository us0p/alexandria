NoSQL - Not Only SQL
It’s used for non-relational databases. A NoSQL database is a collection of 
collections that stores a specific set of unstructured data.
NoSQL databases scale horizontally (Add more machines).
There are some nosql database implementation that allow the use of SQL to
query the data thus the name Not Only SQL.
NoSQL is a data management approach.

NoSQL Databases:
There are many types of NoSQL databases, the most common are:
- Key -> Value (e.g.: Redis);
- Document (e.g.: MongoDB);
- Wide Column (e.g.: Cassandra);

NoSQL databases are designed to be more stable and resilient with continuous
availabillity and zero down time, this is due to the fact that most NoSQL
databases are cloud based.
In NoSQL databases is normal to have duplicated data, as this makes the querying
of your data faster because you don't need to join many documents together.
NoSQL databases doesn't require a schema before the use, which makes easier to
develop and maintain your application as your data grow.
In NoSQL theres no default query language and every DBMS have it's own implementation
which makes it harder to work with new databases.
NoSQL databases isn't ACID compliant which means that is possible to receive inconsistent
information or different values at the same time, deppending of which server happens
to be querying.
NoSQL database are BASE comlient which are eventually consistent.
