Is a schema named `information_schema`. It automatically exists in all databases. The owner of this schema is the initial database user in the cluster.

By default this schema is not in the schema search path, so you need to access all objects in it through qualified names.
## Data Types
The columns of the information schema views use special data types that are defined in the information schema. You shouldn't use these types for work outside the information schema.

Every column in the information schema has one of these five types:
- `cardinal_number`: Nonnegative integer.
- `character_data`: A character string without maximum length.
- `sql_identifier`: A character string. This type is used for SQL identifiers. `character_data` is used for any other kind of text data.
- `time_stamp`: A domain over the type `timestamp with time zone`.
- `yes_or_no`: A character string that contains either `YES` or `NO`. The information schema was invented before the type `boolean` was added to the SQL standard, so this convention is necessary to keep the information schema backward compatible.
## `columns`
This view contain information about all table or view columns in the database. System columns are not included. A user can only see columns that it has access to.