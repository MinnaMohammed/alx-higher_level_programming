#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    if a == 0 and b < 0:
        raise ValueError("Cannot raise 0 to a negative power")
    if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example usage:
print(pow(-98, -10))
