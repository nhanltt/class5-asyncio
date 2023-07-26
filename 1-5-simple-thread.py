# Explaination: Function sleep() is synchronous function.
# To run it in asynchronous way, we need to create a thread to run this function 
# and other thread will run asynchronous event loop

# Result:
# Task A: Computing 10 + 1
# Time: 0.00
# Task B: Computing 10 + 1
# Time: 0.00
# Task A: Computing 11 + 2
# Task B: Computing 11 + 2
# Time: 1.02
# Time: 1.02
# Task B: Computing 13 + 3
# Task A: Sum = 13

# Time: 2.03
# Task B: Sum = 16

# Time: 3.04 sec

import time
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

# Function: count time used for running code from start to a line of code.
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# Function: sum all items in an array for a task
async def sum(name, numbers):
    # create 2 thread ti run
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total} + {number}')
        # run sleep() in another thread
        await loop.run_in_executor(_executor, sleep)
        total += number
    # print the result of sum
    print(f'Task {name}: Sum = {total}\n')


start = time.time()

# create an event loop 
loop = asyncio.get_event_loop()

# create a list of tasks to do in event loop 
tasks = [
    loop.create_task(sum("A", [1,2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
# run tasks in event loop until all task is complete
loop.run_until_complete(asyncio.wait(tasks))
# close event loop
loop.close()

# see the time from start to end 
end = time.time()
print(f'Time: {end - start:.2f} sec')