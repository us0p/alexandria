Returns the permission granted to users in the tables of the current database:
- `grantee`: The one that received the permission
- `privilege_type`: The privilege the user has in this table
- `table_schema`: The schema for the table
- `table_name`: The name of the table

You can also check the permissions for functions and sequences in the following views:
- `information_schema.role_routine_grants`: Permissions for function execution.
- `information_schema.role_sequence_grants`: Permissions for sequences utilization.