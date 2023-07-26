# Expalaination: Program create 2 task hello1 and hello2
# when event loop run, 2 coroutine start to run and done at the same time

# Result:
# Wed Jul 26 14:36:42 2023 hello 1 started
# Wed Jul 26 14:36:42 2023 hello 2 started
# Wed Jul 26 14:36:46 2023 hello 1 done
# Wed Jul 26 14:36:46 2023 hello 2 done
# Time: 4.01 sec
import asyncio
import time 

# Function: hello function, work asynchronously
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately, the task is created
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

if __name__=="__main__":
    start = time.time()
    # run event loop
    asyncio.run(main()) 
    end = time.time()
    # see the time from start to end
    print(f'Time: {end - start:.2f} sec')