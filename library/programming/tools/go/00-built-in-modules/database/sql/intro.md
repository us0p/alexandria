# `database/sql`
Provides a generic interface around SQL databases.  
  
The SQL package must be used in conjunction with a [database driver](https://go.dev/wiki/SQLDrivers).  
  
Drivers that do not support context cancellation will not return until  after the query is completed.  
## Dealing with `NULL`
If a database column is nullable, one of the types supporting null values  should be passed to Scan.  
  
For example, if the name column in the names table is nullable.
```go
import "database/sql"

func main() {
    // Database and ctx initialization...

    id := 1
    var name sql.NullString
    err := db.QueryRowContext(
        ctx,
        "SELECT name FROM names WHERE id = $1",
        id
    ).Scan(&name)

    if name.Valid {
        // use name.String
    } else {
    }
    // value is NULL
}
```
  
Default `database/sql` Nullable types implementation:
- `NullByte`
- `NullBool`
- `NullFloat64`
- `NullInt64`
- `NullInt32`
- `NullInt16`
- `NullString`
- `NullTime`
  
User types supporting NULL can be created by implementing  interfaces `sql/driver.Valuer` and `sql.Scanner`.
  
>You can also pass pointer types. Be careful for performance issues as it requires extra memory allocations.