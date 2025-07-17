# `*DB.QueryContext`
Execute a query that returns rows.  
  
It can receive the query placeholders as arguments.
```golang
import (
    "database/sql"
    "context"
    "log"
    "fmt"
)

func main() {
    // database and context initialization...

    age := 27
    rows, err := db.QueryContext(
        ctx,
        "SELECT name FROM users WHERE age=?",
        age
    )
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    names := make([]string, 0)
    
    for rows.Next() {
        var name string
        if err := rows.Scan(&name); err != nil {
            // check for a scan error.
            log.Fatal(err)
        }
        names = append(names, name)
    }

    // If the database is being written to, ensure to check for Close
    // errors that may be returned from the driver.

    // The query may encounter an auto-commit error and be forced to 
    // rollback changes.
    // err = rows.Close() 

    // If not checking the errors of each scan, Rows.Err() will report
    // the last error encountered by Rows.Scan.
    // if err := rows.Err(); err != nil {
    //     log.Fatal(err)
    // }}
}
```
