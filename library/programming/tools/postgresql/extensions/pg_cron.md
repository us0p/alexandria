Simple cron-based job schedules for PostgreSQL (10 or higher) that runs inside the database as an extension.

It uses the same syntax as a regular [cron](cronjobs.md).

It can run multiple jobs in parallel, but it runs at most one instance of a job at a time. If a second run is supposed to start before the first finishes, then the second run is queued and started as soon as the first run completes.

>By default the pg_cron background worker expects its metadata tables to be created in the "postgres" database.

>By default, pg_cron uses `libpq` to open a new connection to the local database, which needs to be allowed by `pg_hba.conf`.
## Viewing job run details
You can view the status of running and recently completed job runs in the `cron.job_run_details`

```PostgreSQL
SELECT
	*
FROM cron.job_run_details
ORDER BY start_time DESC
LIMIT 5;
```

The records in `cron.job_run_details` are not cleaned automatically. If you have jobs that run every few seconds, it can be a good idea to clean up regularly:
## Scheduling a job
```PostgreSQL
SELECT
	cron.schedule(
		'delete-job-run-detail',
		'0 12 * * *', 
		$$DELETE FROM cron.job_run_details 
		WHERE end_time < NOW() - INTERVAL '7 days'$$
	);
```
## Remove a job
```PostgreSQL
SELECT cron.unschedule(5);
```
## Updating a scheduled job
To update a job you need to remove it and add it again.
## Enable/Disable a job
```PostgreSQL
SELECT cron.enable(5);   -- re-enable jobid 5
SELECT cron.disable(5);  -- disable jobid 5
```
