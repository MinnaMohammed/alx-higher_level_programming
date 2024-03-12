#!/usr/bin/python3
for i in range(0, 9):
    if i == 0:
        comma = ""
    for j in range(1, 10):
        if j <= i:
            continue
        print("{}{:d}{:d}".format(comma, i, j), end="")
        comma = ", "
print()
