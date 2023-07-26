import asyncio
import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30

# my_compute_time = 5
# opponent_compute_time = 55
# opponents = 24
# move_pairs = 2

# Solution and Explaination:
# For each move pair with 1 opponent 
# server go chess for 5s and don't wait for opponent,
# server go chess with another opponent immediately
# Then, for 24 opponents with the first move pairs, server use total 24*5 = 120 seconds
# For 30 move pairs, server use total 120*30 = 3600 seconds
# equal to 1 hour

# Again notice that I declare the main() function as a async function
async def main(x):
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # Don't use time.sleep in a async function. I'm using it because in reality you aren't thinking about making a
        # move on 24 boards at the same time, and so I need to block the event loop.
        time.sleep(my_compute_time)
        print(f"Waiting on opponent on board {x}.")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


async def async_io():
    # Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")