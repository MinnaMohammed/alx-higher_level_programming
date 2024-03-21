#!/usr/bin/python3
def weight_average(my_list=[]):
    summ = 0
    den = 0
    for i in my_list:
        if i[1] == '':
            i[1] = 0
        elif i[0] == '':
            i[0] = 0

        summ += (i[0] * i[1])
        den += i[1]
    return summ/den
