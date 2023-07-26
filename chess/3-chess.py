import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30

# Solution and Explaination:
# For each move pair with 1 opponent 
# server go chess for 5s and wait for opponent go for 55s
# For 30 move pair with 1 opponent
# server use total 30*(5+55) = 1800 seconds
# For 30 move pair with 24 opponent
# server use total 24*1800 = 43200 seconds 
# equal to 12 hours

def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")