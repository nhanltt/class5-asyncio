# Explaination: This program use asyncio but in the wrong way.
# At this function: 
# async def sleep():
#     print(f'Time: {time.time() - start:.2f}')
#     time.sleep(1)
# is defined as async function but use sync library time.sleep() insight.
# This cause coroutine is not release resource to event loop
# and then, program run consequently.

# Result 
# ..\1-2-simple-async-wrong.py:38: DeprecationWarning: There is no current event loop
#   loop = asyncio.get_event_loop()
# Task A: Computing 10 + 1
# Time: 0.00
# Task A: Computing 11 + 2
# Time: 1.00
# Task A: Sum = 13

# Task B: Computing 10 + 1
# Time: 2.01
# Task B: Computing 11 + 2
# Time: 3.01
# Task B: Computing 13 + 3
# Time: 4.01
# Task B: Sum = 16

# Time: 5.02 sec

import asyncio
import time

# Function: count time from start to a operation
# but use sync library insife async def!
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# Function: sum all items in an array for a task
async def sum(name, numbers):
    total = 10
    for number in numbers:
        print(f'Task {name}: Computing {total} + {number}')
        await sleep() # see the time for sum each item
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