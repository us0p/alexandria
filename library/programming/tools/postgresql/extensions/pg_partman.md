Extension that helps managing time or number/id based table partitioning easier.

As of version 5.0.1, the minimum version of PostgreSQL required is 14 and trigger-based partitioning is no longer supported. All partitioning is done using built-in declarative partitioning.

>A default partition to catch data outside the existing child boundaries is automatically created for all partition sets. The `check_default()` function provides monitoring for any data getting inserted into the default table

Requiring a superuser to use `pg_partman` is completely optional. To run as a non-superuser, the role(s) must have ownership of all partition sets they manage and permissions to create objects in any schema that will contain partition sets that it manages.
## `partman` schema
It's not required but recommended and can be whatever you wish, but it cannot be changed after installation. 
```PostgreSQL
CREATE SCHEMA partman;
CREATE EXTENSION pg_partman SCHEMA partman;
```
## `create_parent()`
Main function to create a partition set with one parent table and inherited children.

Parent table must already exist and be declared as partitioned **before** calling this function.

>Apply all defaults, indexes, constraints, privileges & ownership to parent table so they will propagate to children.

A default partition (handles data that are outside the bounds of the current partitions) and template table are created by default unless otherwise configured.

```PostgreSQL
create_parent(
	-- existin parent table. must be schema qualified, even if in public schema.
    p_parent_table text, 
	
	-- the column to partition by.
	-- When control is text/uuid, p_time_encoder and p_time_decoder must be set.
    p_control text, 

	-- time or integer range interval for each partition.
	-- Value msut be given as text.
	-- If the interval is >= 2, p_type must be range.
	-- If the interval is 1, p_type must be list.
    p_interval text, 

	-- Type of partitioning to be done.
    p_type text DEFAULT 'range',

	-- Tesll pg_partman that the control column is an integer, but actually represents an epoch time value.
	-- Valid values are:
		-- 'seconds'
		-- 'miliseconds'
		-- 'microseconds'
		-- 'nanoseconds'
		-- 'none'
    p_epoch text DEFAULT 'none',

	-- How many additional partitions to always stay ahead of the current partition.
	-- If partitioning ever falls behind premake, running run_maintenance() and data insertion should automatically catch things up.
    p_premake int DEFAULT 4, 

	-- Allows the first partition of a set to be specified instead of it being automatically determined.
	-- For subpartitioning, this only applies during initial setup and not during ongoing maintenance.
    p_start_partition text DEFAULT NULL, 

	-- determine whether a default table is created.
    p_default_table boolean DEFAULT true, 

	-- Set whether maintenance is managed automatically when run_maintenance() is called without a table parameter or in the background.
    p_automatic_maintenance text DEFAULT 'on', 

	-- Optional array parameter to set the columns that will have additional constraints. Used in conjunction with apply_constraints().
    p_constraint_cols text[] DEFAULT NULL, 

	-- If you do not pass a value here, a template table will automatically be made for you in same schema that partman was installed to.
	-- If you pre-created a template table and used it here, the initial child tables will obtain these properties.
    p_template_table text DEFAULT NULL, 

	-- allog partman to use pg_jobmon extension to monitor that partitioning is working correctly.
    p_jobmon boolean DEFAULT true, 

	-- By default, time-based partitioning will truncate the child table starting values to line up at the beginning of typical boundaries.
	-- If a partitioning interval that doesn't fall on those boundaries is desired, this option may be required to ensure the child table has the expected boundaries, especially if you also set p_start_partition.
	-- The valid values allowed for this parameter are the interval values accepted by built-in date_trunc().
    p_date_trunc_interval text DEFAULT NULL, 

	-- Setting to false allows the control column to be NULL.
	-- Allowing this is not advised without very careful review and explicit use-case defined as it can cause excessive data in the DEFAULT child partition.
    p_control_not_null boolean DEFAULT true, 

	-- name of function that encodes a timestamp into a string representing your partition bounds.
	-- the function must handle NULL input safely.
    p_time_encoder text DEFAULT NULL, 

	-- name of function that decodes a text/uuid control value into a timestamp.
	-- The function must handle NULL input safely.
    p_time_decoder text DEFAULT NULL
)
RETURNS boolean
```
## `run_maintenance_proc()`
Run this function as a scheduled job to automatically create child tables for partition sets configured to use it.

The function also maintains the partition retention system for any partitions sets that have it turned on.

Every run checks for all tables listed in the `part_config` table with `automatic_maintenance` set to true and either creates new partitions or runs their retention policy.

New partitions are only created if the number of child tables ahead of the current one is less than the `premake` value.

Can be called instead of `run_maintenance` to cause PostgreSQL to commit after each partition set's maintenance has finished.

Greatly reduces contention issues with long running transactions when there are many partitions to maintain.
```PostgreSQL
run_maintenance_proc(
	-- Ho many seconds to wait between each partition set's maintenance run.
    p_wait int DEFAULT 0, 

	-- By default ANALYZE is not run after new child tables are created.
	-- For large partition sets, ANALYZE can take a while which can cause contention while the analyze finishes.
    p_analyze boolean DEFAULT NULL, 

	-- Control where the function uses pg_jobmon extension to log what it does.
    p_jobmon boolean DEFAULT true
)
```
## `part_config`
Stores all configuration data for partition sets managed by the extension.

You can get more info about the detailed properties of the table [here](https://github.com/pgpartman/pg_partman/blob/development/doc/pg_partman.md#configuration-tables)