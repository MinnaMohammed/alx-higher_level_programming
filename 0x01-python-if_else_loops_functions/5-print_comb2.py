#!/usr/bin/python3
for num in range(0, 100):
    if num == 0:
        comma = ""
    if num < 10:
        zero = '0'
    else:
        zero = ''
    print("{}{:s}{:d}".format(comma, zero, num), end="")
    comma = ", "
print()
