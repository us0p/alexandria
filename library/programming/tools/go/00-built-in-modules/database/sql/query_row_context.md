# `*DB.QueryRowContext`
Executes a query that is expected to return at most one row.  

It always returns a non-nil value.  
  
Errors are deferred until Row's `Scan` method is called.  
  
If the query selects no rows, the `*Row.Scan` will return `ErrNoRows`.  
  
Otherwise, `*Row.Scan` scans the first selected row and discards the rest.
## Examples
### Separate columns
```golang
import (
    "context"
    "database/sql"
    "log"
    "time"
)

func main() {
    // database and ctx initialization ...

    id := 123
    var username string
    var created time.Time
    err := db.QueryRowContext(
        ctx,
        "SELECT username, created_at FROM users WHERE id=?",
        id
    ).Scan(
        &username,
        &created
    )

    switch {
    case err == sql.ErrNoRows:
        log.Printf("no user with id %d\n", id)
    case err != nil:
        log.Fatalf("query error: %v\n", err)
    default:
        log.Printf(
            "username is %q, account created on %s\n",
            username,
            created
        )
    }
}
```
### Reading into a structure
```golang
import (
    "context"
    "database/sql"
    "log"
    "time"
)

type User struct {
    ID        int
    Username  string
    CreatedAt time.Time
}

func main() {
    // database and ctx initialization ...

    id := 123
    var user User
    err := db.QueryRowContext(
        ctx,
        "SELECT id, username, created_at FROM users WHERE id=?",
        id
    ).Scan(
        &user.ID,
        &user.Name,
        &user.CreatedAt,
    )

    switch {
    case err == sql.ErrNoRows:
        log.Printf("no user with id %d\n", id)
    case err != nil:
        log.Fatalf("query error: %v\n", err)
    default:
        log.Printf(
            "username is %q, account created on %s\n",
            username,
            created
        )
    }
}
```
