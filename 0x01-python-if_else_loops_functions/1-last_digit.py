#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    newNum = -number % 10
    number = -number
    newNum = -newNum
else:
    newNum = number % 10
if newNum > 5:
    print(f"Last digit of {number : d} is{newNum : d} and is greater than 5")
elif newNum == 0:
    print(f"Last digit of {number : d} is{newNum : d} and is 0")
elif newNum < 6:
    print(f"Last digit of  {number : d} is {newNum : d} and "
          f"is less than 6 and not 0")
