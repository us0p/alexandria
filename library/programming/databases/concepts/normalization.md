# Normalization
Database normalization is a process used to organize a database into tables and columns. The idea is that a table should be about a specific topic and that only those columns which support that topic are included. This limits the number of duplicate data contained within your database.

This makes the database more flexible by eliminating issues stemming from database modifications.

- Normal Forms 1 to 3 are the core basics.
- Normal forms 4 and 5 handle exceptions.
## Deletion Anomalies
Happens when deleting a piece of data unintentionally removes other important data that you didn't mean to lose.
## Update Anomalies
Happens when data redundancy causes inconsistencies during an update, meaning you update a value in one place, but fail to update it elsewhere.
Usually occurs when the same piece of information is stored in multiple rows.
## Insertion Anomalies
Happens when you can't insert data into a table without having other data already present, even if that other data isn't relevant yet. Happens when unrelated ta is crammed into the same table.
## Transitive Dependencies
Occurs when a non-key attribute depends on another non-key attribute, instead of directly depending on the primary key.

>If A -> B and B -> C, then A transitively determines C.
## Multi-valued dependency
Occurs when, in a table, one attribute determines multiple independent values of another attribute, and those values don't depend on each other.

>If A determines a set of values for B and independently determines a set of values for C, then: A ->-> B and A->->C.
## 1 Normal Form
### Using row order to convey information is not permitted
There's no such a thing as row order in a database table.
![[Pasted image 20250410071711.png]]

Same information, in 1NF.
![[Pasted image 20250410071845.png]]
### Mixing data types within the same column is not permitted
Having different data types within the same column isn't permitted in relational databases.
![[Pasted image 20250410072013.png]]
### Having a table without a primary key is not permitted.
Each row in a table must be uniquely identified.

Here the primary key could be the name of each Beatle.
![[Pasted image 20250410071845.png]]
### Storing a repeating group of data on a single row is not permitted
Repeating group is when you have multiple values of the same type stored in a single record, often in a single column or as multiple similar columns.

Example of multiple values of the same type in a single column.
![[Pasted image 20250410072745.png]]

Example of multiple similar columns.
![[Pasted image 20250410072907.png]]

A representation in 1NF would be
![[Pasted image 20250410073004.png]]
## 2 Normal Form
Each non-key attribute must depend on the entire primary key.

Storing non-key columns that aren't dependent of the primary key in a table can lead to insert, update, and delete anomalies.

In this example, `Item_Quantity` is related to the primary key `Player_ID, Item_Type` as each combination of `Player_ID, Item_Type` should have a single quantity.
But `Player_Rating` isn't. `Player_Rating` is a property of the player alone, therefore, it's not dependent on the entire primary key.
![[Pasted image 20250410074029.png]]

Same example, respecting 2NF
![[Pasted image 20250410074725.png]]
## 3 Normal Form
Dependency of a non-key attribute in another non-key attribute is not permitted.
Every attribute in a table should depend on the key, the whole key, and nothing but the key.

Example of a table which isn't in 3NF
![[Pasted image 20250410075212.png]]

Same example in 3NF
![[Pasted image 20250410075515.png]]
## 4 Normal Form
Multi-valued dependencies in a table must be multi-valued dependencies on the key.

In this example, the table represents the available combinations of `Model, Color, and Style`.
When we try to add a new `Color: Green` to the `Model: Prairie`, we can create an inconsistency because of the multi-valued dependency:
`Model ->-> Color` and `Model ->-> Style`.
![[Pasted image 20250410080829.png]]

Same example in 4NF
![[Pasted image 20250410081201.png]]
## 5 Normal Form
The table (which must be in 4NF) cannot be describable as the logical result of joining some other tables together.

In the following example, the table represents the relation of personal preference of ice cream brand and flavor of each person.

If Suzy starts to like the brand Frost's and she likes the flavors Strawberry and Mint Chocolate, the following table is inconsistent as it doesn't represents her taste for Frost's Mint Chocolate flavor.
![[Pasted image 20250410081641.png]]

Same example in 5NF
![[Pasted image 20250410082533.png]]