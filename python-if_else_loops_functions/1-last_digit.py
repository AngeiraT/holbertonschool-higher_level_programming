#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastnum = number % -10
else:
    lastnum = number % 10
if lastnum > 5:
    print(f"Last digit of {number} is {lastnum} and is greater than 5")
if lastnum == 0:
    print(f"Last digit of {number} is {lastnum} and is 0")
else:
    print(f"Last digit of {number} is {lastnum} and is less than 6 and not 0")
