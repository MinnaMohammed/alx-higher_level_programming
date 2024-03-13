#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        power = b * -1
    else:
        power = b
    for i in range(power):
        result *= a
    if power != b:
        return 1 / result
    else:
        return result
