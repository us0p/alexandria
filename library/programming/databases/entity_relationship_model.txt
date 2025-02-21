ERD - Entity Relationship Diagram
Entity relationship diagram is a high-level data model that describes the logical 
structure of a database. It is a graphical representation of entities and their 
relationships to each other, typically used in modeling the organization of 
data within databases or information systems.

To build your ERD's you'll usually use some tool like: https://dbdiagram.io/home

Entities: Is an object such as (Person, Place, or thing) which will be tracked 
          in the database.
Attributes: Entity properties or traits of the entity.
Relationship: Describes how each entity relates with the others.

You can visualize Entities as being the rows of your database and the Attributes
as being the columns.

Cardinality:
Are lines drawed between entities and represents the number of minimum or maximum
elements that each relationship may hold. They are:

--------------|-: One
---------------<: Many
--------------||: One (and only one)
-------------O-|: Zero or one
--------------|<: One or many
--------------O<: Zero or many

The symbol each line holds can apper in the left (representing the number of 
left entity elements the right entity has) or in the right (representing the 
number of right entity elements the left entity has).
Of course, they can appear at the same time, representing the relationship
between two entities.

A primary key is a certain attibute that uniquely identifies every record
in a certain table.
Each entity can only have one primary key.
Composite primary keys is a term used when you join two columns in a table
to form a unique identifier.

A foreign key is they primary key of another table present in another one.
They don't have to be unique in the table that references them.

Bridge tables are used as a proxy between many to many relationships,
they store the key of both ends and any other information the table might
need as well.
