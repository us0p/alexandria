# `*DB.PrepareContext`
Creates a prepared statement for later queries or executions.  
  
Multiple queries or executions may be run concurrently from the returned 
statement.  
  
The caller must call the statement's `*Stmt.Close` method.  
  
You fetch the results of the query by calling:
- `ExecContext`
- `QueryContext`
- `QueryRowContext`
  
```golang
import(
    "database/sql"
    "context"
    "log"
)

func main() {
    // databas and ctx initialization...
    age := 27
    stmt, err := db.PrepareContext(
        ctx,
        "SELECT name FROM users WHERE age = $1"
    )
    if err := nil {
        log.Fatal(err)
    }

    rows, err := stmt.QueryContext(ctx, age)
    // process rows
}
```
