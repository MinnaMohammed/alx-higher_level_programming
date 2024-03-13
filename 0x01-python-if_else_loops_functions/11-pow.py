#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        power = b * -1
    else:
        power = b
    for i in range(0, power - 1):
        a *= a
    if power != b:
        return 1 / a
    else:
        return a
