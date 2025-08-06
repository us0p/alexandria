_Mutex_ is an abbreviation for _mutual exclusion_, as in a mutex allows only one thread to access some data at any given time.

To access the data in a mutex, a thread must first signal that it wants access by asking to acquire the mutex’s _lock_.

The lock is a data structure that is part of the mutex that keeps track of who currently has exclusive access to the data.

Therefore, the mutex is described as _guarding_ the data it holds via the locking system.