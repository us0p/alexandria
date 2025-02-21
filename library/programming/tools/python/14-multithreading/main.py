# Process
# a process is an instance of a computer program that is being executed.
# any process has 3 components:

# 1. An executable program.
# 2. The associated data needed by the program (variables, buffers, etc).
# 3. The execution context of the program (state of the process).

# A thread is an entity within a process that can be scheduled for 
# execution. Also, it is the smallest unit of processing that can be 
# performed in an OS. In simple words, a thread is a sequence of such 
# instructions within a program that can be executed independently of 
# other code.

# A thread contains the following information in a Thread Control Block
# TCB:
# - Thread identifier: Unique id (TID) assigned to every new thread.
# - Stack pointer: Points to the thread's stack in the process. The stack
#   contains the local variables under the thread's scope.
# - Program counter: a register that stores the address of the instruction
#   currentrly being executed by a thread.
# - Thread state: Can be: Running, Ready, Waiting, Starting or Done.
# - Thread's register set: Register assigned to thread for computations.
# - Parent process pointer: A pointer to the Process Control Block (PCB) of
#   the process that the thread lives on.

# PCB - is the control block of a program, it has access to the process
# memory.

# Multiple threads can exist within one process where:
# - Each thread contains its own register set and local variables (stored in 
#   the stack).
# - All threads of a process share global variables (stored in heap) and the 
#   program code.

# Multithreading is defined as the ability of a processor to execute multiple 
# threads concurrently. In a simple, single-core CPU, it is achieved using 
# frequent switching between threads. This is termed context switching. In 
# context switching, the state of a thread is saved and the state of another 
# thread is loaded whenever any interrupt (due to I/O or manually set) takes 
# place. Context switching takes place so frequently that all the threads 
# appear to be running parallelly (this is termed multitasking).

# Not that if your task is CPU intensive (require many calculations or so),
# you should rather use multiprocessing. Multithreading is better suited for
# taks that are IO intensive as they require less resources compared to a
# process, also, if you try to perform multiple CPU intensive taks in
# multiple threads, the first thread will block the cpu access from the other
# leading to a decrease in performance as the remaining threads will have
# to fully wait the current thread finigh its processing.

from threading import Thread, Lock, local

# class Thread is used to spawn new threads.
# target is the function to be executed by the thread.
# args are the arguments to be passed to the target function.
t1 = Thread(target=lambda x: print("square:", x ** 2), args=(10,))
t2 = Thread(target=lambda x: print("cube:", x ** 3), args=(10,))

# start thread
t1.start()
t2.start()

# stops the execution of the current program and wait until the
# thread is done.
# waits t1 to finish.
# then waits t2 to finish.
t1.join()
t2.join()

# Thread Pool
# A thread pool is a collection of threads that are created in advance 
# and can be reused to execute multiple tasks.
from concurrent.futures import ThreadPoolExecutor

# The pool managed the execution of the tasks in its worker threads.
pool = ThreadPoolExecutor(max_workers=2)
worker = lambda: print("Worker thread running")

pool.submit(worker) # add a task to the pool.
pool.submit(worker)

# wait for all taks to finish before continuing the main thread.
pool.shutdown(wait=True) 

print("main thread continues to run")

# Synchronization between threads
# Thread synchronization is defined as a mechanism which ensures that 
# two or more concurrent threads do not simultaneously execute some 
# particular program segment known as critical section.
# Critical section refers to the parts of the program where the shared 
# resource is accessed.

# Concurrent access to shared resources can lead to race condition.

# Locks.
x = 0
def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(100_000):
        # acquire lock, a lock can be blocking (default) or non-blocking.
        lock.acquire()
        increment()
        # release a lock, reset a locked lock to unlocked. If any other
        # threads are blocked waiting for the lock to become unlocked,
        # allow exactly one of them to proceed. Raises a ThreadError if
        # lock is aready unlocked.
        lock.release()

def main_task():
    global x
    x = 0
    lock = Lock() # Creates a semaphore object.
    t1 = Thread(target=thread_task, args=(lock,))
    t2 = Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for i in range(10):
        print(f"Iteration {i}: x = {x}")

main_task()

thread_local = local()

# threading.local() is sometimes referred to as thread local storage. It
# creates an object that looks like global but is specific to each
# individual thread.
# You only want to create one of local object, not one for each thread. 
# The object itself takes care of separating accesses from different 
# threads to different data.
