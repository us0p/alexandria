# Multiprocessing
# Refers to ability of a system to support more than one processor at the
# same time.
# A multiprocessing system can have:
# - multiprocessor, a computor with more than one centrar processor.
# - multi-core processor, a single computing component with two or more
#   independent actual processing units (called "cores").

# This is different than concurrence as each process runs independently
# and have its own memory space.

# Note that you should use multiprocessing only when your task will be
# CPU intensive. As each process will have it's own resources, separate
# tasks wont have to wait others to finish.
# You could also use this for IO taks, but processes require much more
# results than threads and for IO tasks, working with thread produces
# a better output than working with multiple processes.
# In simple therms, you should use multiprocessing for CPU intensive 
# tasks and multithreading for IO intensive tasks.

from multiprocessing import Process
from os import getpid
from threading import Thread

# create processes
# target is the function that will be executed in the process.
# args are the arguments to be passed to the target function. 
p1 = Process(target=lambda x: print(f"Square: {x ** 2}"), args=(10,))
p2 = Process(target=lambda x: print(f"Cube: {x ** 3}"), args=(10,))

# start processes.
p1.start()
p2.start()

# wait until process 1 finish.
p1.join()

# wait until process 2 finish.
p2.join()

def worker(w_id: int):
    print(f"PID of process running worker{w_id}: {getpid()}")

def different_process_execution_demonstration():
    print()
    print(f"PID of main process: {getpid()}")
    p1 = Thread(target=worker, args=(1,))
    p2 = Thread(target=worker, args=(2,))
    p3 = Process(target=worker, args=(3,))
    p4 = Process(target=worker, args=(4,))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("Processes p1 to p4 finished execution")
    print(f"Is p1 alive: {p1.is_alive()}")
    print(f"Is p2 alive: {p2.is_alive()}")
    print(f"Is p3 alive: {p3.is_alive()}")
    print(f"Is p4 alive: {p4.is_alive()}")

different_process_execution_demonstration()
