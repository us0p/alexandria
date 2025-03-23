Database Indexes

An index is a data structure that you build and assign on top of an existing 
table that basically looks through your table and tries to analyze and 
summarize it to create shortcuts.
Thus, indexes speed up our queries at the cost of space. The more indices you
have, the more storage requirements.

Indexes are created accordingly to the most common queries executed against 
your table. You need to know the query and data access pattern to create a 
useful index.

Mostly an index is created on the columns specified in the WHERE clause of these
queries as the database retrieves & filters data from the tables based on those 
columns. If you don’t create an index, the database scans all the rows, 
filters out the matching rows & returns the result. With millions of records, 
this scan operation may take many seconds.

Clustered Index
Clustered indexes are created over the primary keys.
A clustered index is collocated with the table data in the same table space or 
same disk file.
This kind of index physically organizes the data on disk as per the logical 
order of the indexed key.

Physical Data Organization
Physically, data is organized on disk across thousands or millions of data blocks. 
For a clustered index, it’s not mandatory that all the disk blocks are 
contiguously stored. Physical data blocks are managed by the OS. A database system 
does not have any absolute control over how physical data space is managed, but 
inside a data block, records can be managed.

Records are stored on the disk block in any arbitrary order. Whenever new records 
are added, they get added in the next available space, this is handled by the OS and
it's the OS who decides whether that record can still fit into the same position 
or a new position has to be allocated for that record.

So position of records are completely handled by OS & no definite relation exists 
between the order of any two records. In order to fetch the records in the logical 
order of the indexed key, disk pages contain an index section in the footer, the 
index contains a list of offset pointers in the order of the key. Every time a record 
is altered or created, the index is adjusted.

This ordering or co-location of related data is waht actually makes a clustered index 
faster. When data is fetched from disk, the complete block containing the data is read 
by the system since our disk IO system writes & reads data in blocks.
The complete data can be found in the current block of data, thus clustered_index 
reduces the number of disk IO by collocating related data as much as possible in the same 
data block. This reduced disk IO causes improvement in performance.

Since a clustered index impacts the physical organization of the data, there can be only 
one clustered index per table.

Secondary Index:
Any index other than a clustered index is called a secondary index. Secondary indices 
does not impact physical storage locations unlike primary indices.

When to use secondary indexes:
You might have several use cases in your application where you don’t query the database 
with a primary key. In such cases you need secondary indices on these columns if the 
frequency of such queries is very high.

Secondary Index Structure:
Secondary indexes are also maintained in a B Tree and are sorted as per the key on which 
the index was created. The leaf nodes contain a copy of the key of the corresponding table 
data in the primary index.
You can assume that the secondary index has reference to the primary key’s address, although 
it’s not the case. 
Retrieving data through the secondary index means you have to traverse two B+ trees — one is 
the secondary index B+ tree itself, and the other is the primary index B+ tree.

Composite indexes:
Is an index created over many columns. Allowing you search capabilities over all the
compounded columns.
The columns used in composite indices are concatenated together, and those concatenated 
keys table data are stored in sorted order using a B+ Tree. When you perform a search, 
concatenation of your search keys is matched against those of the composite index. Then if 
there is any mismatch between the ordering of your search keys & ordering of the composite 
index columns, the index can’t be used.

Let’s say we have an index defined on 4 columns — col1, col2, col3, col4. With a composite 
index, we have search capability on col1, (col1, col2) , (col1, col2, col3) , (col1, col2, 
col3, col4). So we can use any left side prefix of the indexed columns, but we can’t omit 
a column from the middle & use that like — (col1, col3) or (col1, col2, col4) or col3 or 
col4 etc. These are invalid combinations.

If you have queries containing a WHERE clause on multiple columns, write the clause in the 
order of the columns of the composite index. The index will benefit that query.
Composite indices can help you in JOIN & SELECT queries as well.

Covering Index:
A covering index is a special kind of composite index where all the columns specified in the 
query somewhere exist in the index. So the query optimizer does not need to hit the database 
to get the data — rather it gets the result from the index itself.
