# `sql/DB`
This type represents a database handle with a pool of zero or more  underlying connections. It's safe for concurrent use by multiple  goroutines.
## `sql/Open`
Opens a database specified by its database driver needed info.  
  
Returns an instance of `*sql.DB`.  
  
Note that this function doesn't open a database connection, this is  deffered until a query is made.
## `*DB.PingContext`
Verifies a connection to the database is still alive, establishing a  connection if necessary.
## Examples
```go
import (
    "database/sql"
    "driver"
    "context"
)

func main() {
    db, err := sql.Open(driver, "db_connection_options")
    if err != nil {
        // This is not a connection error but a DNS parse error or 
        // another initialization error.
    }

    // you can set connection options:
    db.SetConnMaxLifetime(0)
    db.SetMaxIdleConns(50)
    db.SetMaxOpenConns(50)

    ctx := context.Background()

    err := db.PingContext(ctx)
    if err != nil {
        // no connection is available
    }
    // If this is reached, there's still a connection available.
}
```
