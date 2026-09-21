import time
import random

def delay(s,l):
    while True:
        elapsed = time.time() - s
        if elapsed > l:
            break

def go_and_stop():
    print ("go")
    start = time.monotonic()
    input("enter")
    stop = time.monotonic()
    reaction = stop - start
    return reaction

counter = 0
lowest = None
while counter < 5:
    start = time.time()
    timer_length = random.randint(2,5)
    delay(start,timer_length)
    reaction = go_and_stop()
    print(reaction)
    counter += 1
    if lowest is None or reaction < lowest:
        lowest = reaction
print("Game Over")
print("Your highscore is:", lowest)