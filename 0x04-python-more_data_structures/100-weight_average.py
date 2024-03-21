#!/usr/bin/python3
def weight_average(my_list=[]):
    summ = 0
    den = 0
    for i in my_list:
        summ += (i[0] * i[1])
        den += i[1]
    return summ/den
