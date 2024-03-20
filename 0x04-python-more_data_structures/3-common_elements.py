#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for x, y in zip(set_1, set_2):
        if x == y:
            new_set.add(x)
    return new_set
