# Expalaination: Program create list of 10 tasks
# when event loop run, 10 coroutines start to run and done at the same time

# Result:
# Wed Jul 26 14:48:38 2023 hello 0 started
# Wed Jul 26 14:48:38 2023 hello 1 started
# Wed Jul 26 14:48:38 2023 hello 2 started
# Wed Jul 26 14:48:38 2023 hello 3 started
# Wed Jul 26 14:48:38 2023 hello 4 started
# Wed Jul 26 14:48:38 2023 hello 5 started
# Wed Jul 26 14:48:38 2023 hello 6 started
# Wed Jul 26 14:48:38 2023 hello 7 started
# Wed Jul 26 14:48:38 2023 hello 8 started
# Wed Jul 26 14:48:38 2023 hello 9 started
# Wed Jul 26 14:48:42 2023 hello 0 done
# Wed Jul 26 14:48:42 2023 hello 2 done
# Wed Jul 26 14:48:42 2023 hello 6 done
# Wed Jul 26 14:48:42 2023 hello 9 done
# Wed Jul 26 14:48:42 2023 hello 8 done
# Wed Jul 26 14:48:42 2023 hello 5 done
# Wed Jul 26 14:48:42 2023 hello 7 done
# Wed Jul 26 14:48:42 2023 hello 4 done
# Wed Jul 26 14:48:42 2023 hello 1 done
# Wed Jul 26 14:48:42 2023 hello 3 done
# Time: 4.01 sec

import asyncio
import time 

# Function: hello function, work asynchronously
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    # create 10 coroutine function 
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

if __name__=="__main__":
    start = time.time()
    # run event loop
    asyncio.run(main()) 
    end = time.time()
    # see the time from start to end
    print(f'Time: {end - start:.2f} sec')