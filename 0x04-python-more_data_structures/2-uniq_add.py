#!/usr/bin/python3

def uniq_add(my_list=[]):
    newList = set(my_list)
    num = 0

    for i in newList:
        num += i

    return (num)
