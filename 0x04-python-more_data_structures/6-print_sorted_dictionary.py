#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    orderedList = list(a_dictionary.keys())
    orderedList.sort()
    for i in orderedList:
        print("{}: {}".format(i, a_dictionary.get(i)))
