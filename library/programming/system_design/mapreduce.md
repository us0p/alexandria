Programming model for data processing.

It's a process that transform bigger data into smaller data.

The MapReduce process (job), has 3 steps:
1. Map: Starting point, receives input and map to the necessary data only. It's important that this step generates a set of key value pairs for each input received.
2. Sort: Sorts the list of key value pairs produced by the previous step by key. This step is also responsible for grouping repeated key values under the same key.
3. Reduce: Reduces the values for a single key to a single value, for example, it could sum all the values under a single key.