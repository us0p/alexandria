# Only multiprocessing execute instructions at literally the same time.
# threading and asyncio both run in a single processor and therefore only
# one at the time.

# In threading, the operating system actually knows about each thread and 
# can interrupt it at any time to start running a different thread. This 
# is called pre-emptive multitasking since the operating system can 
# pre-empt your thread to make the switch.
# Pre-emptive multitasking is handy in that the code in the thread doesn’t 
# need to do anything to make the switch. This switch can happen in the 
# middle of a single Python statement, even a trivial one like x = x + 1.
# You might expect that having one thread per task would be the fastest 
# but the extra overhead of creating and destroying the threads erases any
# time savings.

# asyncio, on the other hand, uses cooperative multitasking. The tasks must
# cooperate by announcing when they are ready to be switched out. That 
# means that the code in the task has to change slightly to make this 
# happen.
# One of the advantages of asyncio is that it scales far better than 
# threading. Each task takes far fewer resources and less time to create 
# than a thread, so creating and running more of them works well.

# With multiprocessing, Python creates new processes. A process is usually 
# defined as a collection of resources where the resources include memory, 
# file handles and things like that. One way to think about it is that each
# process runs in its own Python interpreter.
# Because they are different processes, each of taks in a multiprocessing 
# program can run on a different core. Running on a different core means 
# that they actually can run at the same time.
# Bringing up a separate Python interpreter is not as fast as starting a 
# new thread in the current Python interpreter. It’s a heavyweight 
# operation and comes with some restrictions and difficulties.

# I/O-Bound Process
# Your program spends most of its time talking to a slow device, like a 
# network connection, a hard drive, or a printer.
# Speeding it up involves overlapping the times spent waiting for these 
# devices.

# CPU-Bound Process
# You program spends most of its time doing CPU operations.
# Speeding it up involves finding ways to do more computations in the same
# amount of time.
