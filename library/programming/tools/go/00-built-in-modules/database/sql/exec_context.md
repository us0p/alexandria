# `*DB.ExecContext`
Executes a query without returning any rows.  
  
It can also receive parameters for query placeholders.
```go
import (
    "database/sql"
    "context"
)

func main() {
    // database and ctx initialization above...

    id := 47
    result, err := db.ExecContext(
        ctx,
        "UPDATE user SET age = age + 1 WHERE id = ?",
        id
    )

    // ...
}
```
- `result` is of type Result and has only metadata from the operation.
- It's database dependant.
