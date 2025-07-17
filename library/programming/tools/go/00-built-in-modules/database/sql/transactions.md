# `*DB.BeginTx`
Starts a new transaction.  
  
The provided context is used until the transaction is commited or rolled 
back. If the context is canceled, the sql package will roll back the 
transaction.  
  
The provided **TxOptions** is optional and may be nil if defaults should 
be used. If a non-default isolation level is used that the driver doesn't 
support, an error will be returned.
## Example
```golang
import (
    "context"
    "database/sql"
    "log"
)

func main() {
    // database and ctx initialization...

    tx, err := db.BeginTx(
        ctx,
        &sql.TxOptions{Isolation: sql.LevelSerializable}
    )

    if err != nil {
        log.Fatal(err)
    }

    id := 37
    _, execErr := tx.Exec(
        "UPDATE users SET status = ? WHERE id = ?",
        "paid",
        id
    )
    if execErr != nil {
        _ = tx.Rollback()
        log.Fatal(execErr)
    }

    if err := tx.Commit(); err != nil {
        log.Fatal(err)
    }
}
```
