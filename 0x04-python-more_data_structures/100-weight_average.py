#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    sum = 0

    for tuple in my_list:
        num += tuple[0] * tuple[1]
        sum += tuple[1]

    return (num / sum)
