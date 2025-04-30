Anything you enter in `psql` that begins with an unquoted backslash is a meta-command that is processed by `psql` itself. Meta commands are often called slash or backslash commands.

The format of a `psql` command is the backslash, followed immediately by a command verb, then any arguments. The arguments are separated by any number of whitespaces.
## Common commands
- `\d [pattern]`: describes the relation or composite type matching `pattern`. It can be a table, view, materialized view, index, sequence, or foreign table. By default, only user-created objects are shown.
- `\du [pattern]`:  List database roles. By default, only user-created roles are shown. If pattern is specified, only those roles whose names match the pattern are listed.
- `\l [pattern]`: List the databases in the server. If `pattern` is specified, only databases whose names match the pattern are listed.
- `\x` Toggles expanded table formatting mode.
- `\? [topic]`: Show help information. The optional `topic` defaulting to `commands` selects which part of `psql` is explained.

You can use a short version of the `\d` command represented in the available relations as follow:

| command | action            |
| ------- | ----------------- |
| `\dE`   | Foreign table     |
| `\di`   | Index             |
| `\dm`   | Materialized view |
| `\ds`   | Sequence          |
| `\dt`   | Table             |
| `\dv`   | View              |