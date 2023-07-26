# Explaination: Program compute factorial for n
# 3 coroutines run at the same time, but done in different time 
# the results is printed after all tasks is done 

# Result:
# Computing factorial (2), currently i=2...
# Computing factorial (3), currently i=2...
# Computing factorial (4), currently i=2...
# Computing factorial (3), currently i=3...
# Computing factorial (4), currently i=3...
# Computing factorial (4), currently i=4...
# [2, 6, 24]
# Time: 3.03 sec
import asyncio
import time 

# Function: compute for factorial of n
async def factorial(n):
    f = 1
    for i in range(2, n+1):
        print(f"Computing factorial ({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *=i 

    return f

# Function: main corotine
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L)

if __name__=="__main__":
    start = time.time()
    # run event loop
    asyncio.run(main()) 
    end = time.time()
    # see the time from start to end
    print(f'Time: {end - start:.2f} sec')