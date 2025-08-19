# COPY
Is used to efficiently transfer data **between a table and a file** (or standard input/output).

It's much faster than doing individual `INSERT` statements because it works in bulk.

This command requires a **superuser** or `pg_read_server_files`/`pg_write_server_files` roles.
## Syntax
```SQL
-- file_path must always be readable by PostgreSQL server process.
-- file_path can also be STDIN or STDOUT to read/write to the STD streams of the OS.
COPY table_name [(column_list)]
FROM 'file_path' -- used to import file -> table
TO 'file_path' -- used to export table -> file
[WITH]
	FORMAT format_name -- can be 'TEXT' (default), 'CSV', 'BINARY'.
	[DELIMETER 'character'] -- how values are separated.
	[NULL 'null_string'] -- represents how NULL values are represented in the file, defaults to \N.
	[HEADER] -- boolean value, represents if should skip first line.
	[QUOTE 'character'] -- defines the character used to quote fields that contain special characters, defaults to "" for CSV.
	[ESCAPE 'character']  -- Specified character used to escape a quote character inside a quoted value, a special character in CSV mode. defaults the same as QUOTE for CSV, and \ for TEXT
	[ENCODING 'encoding_name']; -- what character encoding the file uses, e.g. UTF-8, LATIN1, etc.
```