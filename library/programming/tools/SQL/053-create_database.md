# CREATE DATABASE
Is used to create a new database in the server.

Each database is separate from others.
## PostgreSQL Database Templates
When you use the `CREATE DATABASE` command, PostgreSQL creates the new database using a copy of the native `template1` database.
## Syntax
```SQL
CREATE DATABASE name
	[ [ WITH ] [ OWNER [=] user_name]       -- string
		[ Template [=] template ]           -- string
		[ ENCODING [=] encoding ]           -- string
		[ LC_COLLATE [=] lc_collate ]       -- string
		[ LC_CTYPE [=] lc_type ]            -- string
		[ TABLESPACE [=] tablespace_name ]  -- string
		[ ALLOW_CONNECTIONS [=] allowconn ] -- bool
		[ CONNECTION LIMIT [=] connlimit ]  -- int
		[ IS_TEMPLATE [=[] istemplate ] ]   -- bool
```
- `CONNECTION LIMIT`: Used to limit the number of connection for the entire DB instance.