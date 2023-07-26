# simple-sync program sum all items in an array with init total value is 10
# program run consequently
# compute for task A first, then task B

# Result:
# Task A: Computing 10 + 1
# Time: 0.00
# Task A: Computing 11 + 2
# Time: 1.01
# Task A: Sum = 13

# Task B: Computing 10 + 1
# Time: 2.02
# Task B: Computing 11 + 2
# Time: 3.03
# Task B: Computing 13 + 3
# Time: 4.04
# Task B: Sum = 16

# Time: 5.05 sec

import time 

# Function: count time used for running code from start to a line of code.
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# Function: sum all items in an array for a task
def sum(name, numbers):
    total = 10
    for number in numbers:
        print(f'Task {name}: Computing {total} + {number}')
        sleep() # see the time for sum each item
        total += number
    # print the result of sum
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

# Tasks program must do
tasks = [sum("A", [1, 2]),
        sum("B", [1, 2, 3]),
        ]

end = time.time()
print(f'Time: {end - start:.2f} sec')