A **cronjob** is a **scheduled task** that runs automatically at specified times or intervals, using the Unix/Linux **cron** system.
- **Cron** = the background daemon (service) that checks schedules and runs jobs.
- **Cron job** = the actual scheduled command or script.
- Defined using a **cron expression** (the 5-field syntax we just explored).
- Runs unattended — once scheduled, the system handles execution.
## Cronjob Notation
```plaintext
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday=0 or 7)
│ │ │ │ │
* * * * *
```
### Special cron characters
| **Character** | **Usage**            | **Example**    | **Meaning**         |
| ------------- | -------------------- | -------------- | ------------------- |
| `*`           | Any value (wildcard) | `* * * * *`    | Every minute        |
| `,`           | List of values       | `0,30 * * * *` | At minute 0 and 30  |
| `-`           | Range of values      | `1-5 * * * *`  | Minutes 1 through 5 |
| `/`           | Step values          | `*/10 * * * *` | Every 10 minutes    |
### Examples
| **Expression** | **Meaning**                       |
| -------------- | --------------------------------- |
| `* * * * *`    | Every minute                      |
| `0 * * * *`    | Every hour (at minute 0)          |
| `0 0 * * *`    | Midnight every day                |
| `0 9 * * 1-5`  | 9 AM Monday–Friday                |
| `0 12 1 * *`   | Noon on the 1st of every month    |
| `*/15 * * * *` | Every 15 minutes                  |
| `15 14 1 * *`  | 2:15 PM on the 1st of every month |
| `0 22 * * 1-5` | 10 PM, Monday–Friday              |
