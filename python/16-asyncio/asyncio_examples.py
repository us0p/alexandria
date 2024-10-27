# The asyncio package is billed by the Python documentation as a library to
# write concurrent code. However, async IO is not threading, nor is it 
# multiprocessing. It is not built on top of either of these.

# async IO is a single-threaded, single-process design: it uses cooperative 
# multitasking. async IO gives a feeling of concurrency despite using a 
# single thread in a single process. Coroutines can be scheduled 
# concurrently, but they are not inherently concurrent.

# Coroutines
# A coroutine is a specialized version of a python generator function.
# it's a function that can suspend its execution before reaching return, and
# can indirectly pass control to another coroutine for some time.

# The syntax async def, async with and async for introduces a native
# coroutine or an asynchronous generator.
# The keyword await passes function control back to the event loop. (It
# suspends the execution of the surrouding coroutine).
# If Python encounters an await f() expression in the scope of g(), it'll
# ask the event loop to suspend execution of g() until whatever it's 
# waiting on—the result of f()—is returned. In the meantime, go let 
# something else run.

# It's only possible to use await in the body of coroutines.
# It's only possible to use await on awaitable objects.
# An awaitable object is another coroutine or an object defining an
# __await__() method that returns an iterator.

# Most programs will contain small, modular coroutines and one wrapper 
# function that serves to chain each of the smaller coroutines together.
# this wrapper and its chained coroutines are then executed.

# You need not to concern yourself with thread safety when it comes to
# async IO.
from asyncio import create_task, get_event_loop, sleep, gather, run
from time import perf_counter

async def count():
    print("One")
    await sleep(1)
    print("Two")

async def main():
    await gather(count(), count(), count())

def asyncio_hello():
    s = perf_counter()
    run(main())
    elapsed = perf_counter() - s
    # count() executed inside main are executed throughtly with a delay of
    # 1s.
    # when each task reaches an await, the function gives the control back
    # to the event loop and lets other functions be executed during its
    # down time.
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
asyncio_hello()

import asyncio
import itertools as it
import os
import random
import time

async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()

async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)

async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    # Synchronous loop for each single producer
    for _ in it.repeat(None, n):  
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")

async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()

async def main_queue(nprod: int, ncon: int):
    q = asyncio.Queue()
    # asyncio.create_task() is used to schedule the execution of a coroutine
    # object.
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers too
    for c in consumers:
        c.cancel()

def demonstrate_asyncio_queue():
    random.seed(444)
    start = time.perf_counter()
    # sets 5 producers and 10 consumers.
    asyncio.run(main_queue(5, 10))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
demonstrate_asyncio_queue()

# When you call a coroutine on its own, without await, or without any calls
# to asyncio.run() the result is an awaitable coroutine object.
# Under the hood coroutines in Python are just enhanced generators.

# One critical feature of generators as it pertains to async IO is that 
# they can effectively be stopped and restarted at will.

# There’s a second and lesser-known feature of generators that also 
# matters. You can send a value into a generator as well through its 
# .send() method. This allows generators (and coroutines) to call (await) 
# each other without blocking.

# Along with plain async/await, Python also enables async for to iterate 
# over an asynchronous iterator.

# A natural extension of this concept is an asynchronous generator. Recall 
# that you can use await, return, or yield in a native coroutine. Using 
# yield within a coroutine became possible in Python 3.6, which introduced 
# asynchronous generators with the purpose of allowing await and yield to 
# be used in the same coroutine function body:

async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

# Last but not least, Python enables asynchronous comprehension with async 
# for. 

async def main():
    g = [i async for i in mygen()] # this iteration is not concurrent;
    f = [j async for j in mygen() if not (j // 3 % 5)] # nor is this one;
    return g, f

# neither asynchronous generators nor comprehensions make the iteration 
# concurrent. All that they do is provide the look-and-feel of their 
# synchronous counterparts, but with the ability for the loop in question 
# to give up control to the event loop for some other coroutine to run.

# The async for and async with statements are only needed to the extent 
# that using plain for or with would “break” the nature of await in the 
# coroutine.

# The event loop is something like a while True loop that monitors 
# coroutines, taking feedback on what’s idle, and looking around for 
# things that can be executed in the meantime. It is able to wake up an 
# idle coroutine when whatever that coroutine is waiting on becomes 
# available.

# asyncio.run(), introduced in Python 3.7, is responsible for getting the 
# event loop, running tasks until they are marked as complete, and then 
# closing the event loop.

# There’s a more long-winded way of managing the asyncio event loop, with 
# get_event_loop().

def demonstrate_long_running_evl():
    loop = get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

# 1: Coroutines don’t do much on their own until they are tied to the 
#    event loop.
# 2: By default, an async IO event loop runs in a single thread and on a 
#    single CPU core. Usually, running one single-threaded event loop in 
#    one CPU core is more than sufficient. It is also possible to run event 
#    loops across multiple cores.
# 3. Event loops are pluggable. That is, you could, if you really wanted, 
#    write your own event loop implementation and have it run tasks just 
#    the same.

# threading or asyncio
# Even in cases where threading seems easy to implement, it can still lead 
# to infamous impossible-to-trace bugs due to race conditions and memory 
# usage, among other things.
# Threading also tends to scale less elegantly than async IO, because 
# threads are a system resource with a finite availability. Creating 
# thousands of threads will fail on many machines, and it's not  recommend 
# trying it in the first place. Creating thousands of async IO tasks is 
# completely feasible.

# Is you don't await the sub-coroutines within the wrapper coroutine,
# when you run asyncio.run(wrapper()), run() will call
# loop.run_until_complete(wrapper()), the event loop is only concerned
# that wrapper() is done, not that tasks that get created withing wrapper()
# are done. Without await, the loop running the wrapper's sub-coroutines
# will cancel the sub-coroutines, possibly before they are completed.
# If you need to get a list of currently pending tasks, you can use
# asyncio.Task.all_tasks().

# Separately, there’s asyncio.gather(). gather() is meant to neatly put a 
# collection of coroutines (futures) into a single future. As a result, it 
# returns a single future object, and, if you await asyncio.gather() and 
# specify multiple tasks or coroutines, you’re waiting for all of them to 
# be completed. The result of gather() will be a list of the results 
# across the inputs.

# You probably noticed that gather() waits on the entire result set of the 
# Futures or coroutines that you pass it. Alternatively, you can loop over 
# asyncio.as_completed() to get tasks as they are completed, in the order 
# of completion. The function returns an iterator that yields tasks as they 
# finish.

async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))

async def demonstrating_on_demand_loop():
    t = create_task(coro([3, 2, 1]))
    t2 = create_task(coro([10, 5, 0]))
    print('Start:', time.strftime('%X'))
    for res in asyncio.as_completed((t, t2)):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')
    print('End:', time.strftime('%X'))
    print(f'Both tasks done: {all((t.done(), t2.done()))}')
asyncio.run(demonstrating_on_demand_loop())
