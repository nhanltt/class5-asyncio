# Explaination: This program use asyncio to sum items in an array
# Task A and B take resources respectively 
# When task A sleep, task B run
# Then program can save time, from 5s in the previous program
# to 3s in this program
# But program use main coroutine, no need to create event loop first

# Result 
# Task A: Computing 10 + 1
# Time: 0.00
# Task B: Computing 10 + 1
# Time: 0.00
# Task A: Computing 11 + 2
# Time: 1.02
# Task B: Computing 11 + 2
# Time: 1.02
# Task A: Sum = 13

# Task B: Computing 13 + 3
# Time: 2.03
# Task B: Sum = 16

# Time: 3.04 sec

import asyncio
import time

# Function: count time from start to a operation
# while sleep, return resource to main loop
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

# Function: sum all items in an array for a task
async def sum(name, numbers):
    total = 10
    for number in numbers:
        print(f'Task {name}: Computing {total} + {number}')
        await sleep() # see the time for sum each item
        total += number
    # print the result of sum
    print(f'Task {name}: Sum = {total}\n') 

# Function: main corountine for event loop
async def main():
    # create tasks to do in event loop, wait for event loop run
    await asyncio.gather(sum("A", [1,2]), sum("B", [1, 2, 3]))

if __name__=="__main__":
    start = time.time()
    # run event loop
    asyncio.run(main()) 
    end = time.time()
    # see the time from start to end
    print(f'Time: {end - start:.2f} sec')