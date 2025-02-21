from multiprocessing import Process, Array, Value

result = []

def square_list(mylist): 
    global result 
    for num in mylist: 
        result.append(num * num) 
    print(f"Result(in process p1): {result}") # [1, 4, 9, 16]
  
def demonstrate_independency_of_processes(): 
    print("Demonstrate independency of processes")
    mylist = [1,2,3,4] 
  
    p1 = Process(target=square_list, args=(mylist,)) 
    p1.start() 
    p1.join() 
  
    print(f"Result(in main program): {result}") # []

demonstrate_independency_of_processes()

# Each process has its own memory space.
# Thus the array squery_list updated in p1 is different from the array
# existing in the main process, that's why the array in the main process
# is empty at the end of the program.

# Sharing memory between processes.
# multiprocessing module provides Array (ctype array allocated from 
# shared memory) and Value (ctype object allocated from shared memory) 
# objects to share data between processes.

def shared_square_list(mylist, result, square_sum): 
    for idx, num in enumerate(mylist): 
        result[idx] = (num * num) 
    
    square_sum.value = sum(result)
    print(f"Result(in process p1): {result[:]}") # [1, 4, 9, 16]
    print(f"Sum of squares(in process p1): {square_sum.value}") # 30

def share_memory_between_processes(): 
    print()
    print("Sharing memory between processes")
    mylist = [1,2,3,4] 

    # creating an array of int data type with space for 4 integers.
    result = Array('i', 4)

    # creating value of int data type.
    square_sum = Value("i")
  
    p1 = Process(target=shared_square_list, args=(mylist,result,square_sum)) 
    p1.start() 
    p1.join() 
  
    print(f"Result(in main program): {result[:]}") # [1, 4, 9, 16]
    print(f"Sum of squares(in main program): {square_sum.value}") # 30

share_memory_between_processes()

# Server process
# Whenever a python program starts, a server process is also started.
# From there on, whenever a new process is needed, the parent process
# connects to the server and requests it to fork a new process.
# A server process can hold Python objects (lists, dictionaries, etc),
# and allow other processes to manipulate them using proxies.

from multiprocessing import Manager

# class Manager is used to control a server process. Hence, managers
# provide a way to create data that can be shared between different
# processes.

# Server process managers are more flexible than using shared memory 
# objects because they can be made to support arbitrary Python object 
# types. Also, a single manager can be shared by processes on different 
# computers over a network. They are, however, slower than using shared 
# memory.

def print_records(records): 
    for record in records: 
        print(F"Name: {record[0]}\nScore: {record[1]}\n") 
  
def insert_record(record, records): 
    records.append(record) 
    print("New record added!\n")

def share_memory_through_server_process():
    print()
    print("Share memory through server process")
    with Manager() as manager:
        # creating a list in server process memory 
        records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)]) 
        new_record = ('Jeff', 8) 
  
        p1 = Process(target=insert_record, args=(new_record, records)) 
        p2 = Process(target=print_records, args=(records,)) 
  
        # running process p1 to insert new record 
        p1.start() 
        p1.join() 
  
        # running process p2 to print records 
        p2.start() 
        p2.join()

share_memory_through_server_process()

# Communication between processes
# multiprocessing module supports two types of communication channel
# between processes:
# - Queue.
# - Pipe.

# Note that data in a pipe may become corrupted if two processes 
# (or threads) try to read from or write to the SAME end of the pipe at 
# the same time. Also note that Queues do proper synchronization between 
# processes, at the expense of more complexity. Hence, queues are said to 
# be thread and process safe!

# Queue
# Any Python object can pass through a Queue.
from multiprocessing import Queue

def square_list_q(mylist, q): 
    # append squares of mylist to queue 
    for num in mylist: 
        q.put(num * num) 
  
def print_queue(q): 
    print("Queue elements:") 
    while not q.empty(): 
        print(q.get()) 
    print("Queue is now empty!") 
  
def demonstrate_multiprocessing_queue(): 
    print()
    print("Demonstrating multiprocessing queue")
    mylist = [1,2,3,4] 
  
    # creating multiprocessing Queue 
    q = Queue() 
  
    p1 = Process(target=square_list_q, args=(mylist, q)) 
    p2 = Process(target=print_queue, args=(q,)) 
  
    p1.start() 
    p1.join() 
  
    p2.start() 
    p2.join()

demonstrate_multiprocessing_queue()

# Pipes
# A pipe can have only two endpoints. Hence, it is preferred over queue
# when only two-way communication is required.

from multiprocessing import Pipe

# The Pipe() function returns a pair of connection objects connected by 
# a pipe. Those objects represent the two ends of the pipe. Each 
# connection object has send() and recv() methods.

def sender(conn, msgs): 
    for msg in msgs: 
        conn.send(msg) 
        print(f"Sent the message: {msg}") 
    conn.close() 
  
def receiver(conn): 
    while True: 
        msg = conn.recv() 
        if msg == "END": 
            break
        print(f"Received the message: {msg}") 
  
def demonstrating_multiprocessing_pipe(): 
    print()
    print("Demonstrating multiprocessing pipes")
    msgs = ["hello", "hey", "hru?", "END"] 
  
    # creating a pipe 
    parent_conn, child_conn = Pipe() 
  
    p1 = Process(target=sender, args=(parent_conn,msgs)) 
    p2 = Process(target=receiver, args=(child_conn,)) 
  
    p1.start() 
    p2.start() 
  
    p1.join() 
    p2.join()

demonstrating_multiprocessing_pipe()
