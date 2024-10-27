# Synchronization between processes

from multiprocessing import Process, Value
  
def perform_transactions(): 
    def withdraw(balance):     
        for _ in range(10000): 
            balance.value = balance.value - 1

    def deposit(balance):     
        for _ in range(10000): 
            balance.value = balance.value + 1
  
    # initial balance (in shared memory) 
    balance = Value('i', 100) 
  
    p1 = Process(target=withdraw, args=(balance,)) 
    p2 = Process(target=deposit, args=(balance,)) 
  
    p1.start() 
    p2.start() 
  
    p1.join() 
    p2.join() 
  
    print(f"Final balance = {balance.value}") 
  
def demonstrating_multiprocess_race_condition():
    print("Demonstrating multiprocess race condition")
    for _ in range(10): 
        # expect final value for each interation to be 100.
        perform_transactions()
demonstrating_multiprocess_race_condition()

from multiprocessing import Lock

def perform_transactions_with_lock(): 
    def withdraw(balance, lock):     
        for _ in range(10000): 
            lock.acquire() 
            balance.value = balance.value - 1
            lock.release() 
      
    def deposit(balance, lock):     
        for _ in range(10000): 
            lock.acquire() 
            balance.value = balance.value + 1
            lock.release() 
  
  
    # initial balance (in shared memory) 
    balance = Value('i', 100) 
  
    # creating a lock object 
    lock = Lock() 
  
    p1 = Process(target=withdraw, args=(balance,lock)) 
    p2 = Process(target=deposit, args=(balance,lock)) 
  
    p1.start() 
    p2.start() 
  
    p1.join() 
    p2.join() 
  
    print(f"Final balance = {balance.value}") 
  
def demonstrating_multiprocessing_lock():
    print(f"\nDemonstrating multiprocessing locks")
    for _ in range(10): 
        perform_transactions_with_lock()
demonstrating_multiprocessing_lock()

# Pooling between processes
# The Pool class represents a pool of worker processes. It has methods 
# which allows tasks to be offloaded to the worker processes in a few 
# different ways. It's used to utlize all the cores.

from multiprocessing import Pool
from os import getpid

def square(n): 
    print(f"Worker process id for {n}: {getpid()}") 
    return (n*n) 
  
def demonstrating_multiprocessing_pool():
    print("\nDemonstrating multiprocessing pool")
    mylist = [1,2,3,4,5] 
  
    # creating a pool object 
    p = Pool() 
  
    # map list to target function 
    result = p.map(square, mylist) 
  
    print(result)
demonstrating_multiprocessing_pool()
