#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxx = max(a_dictionary.values())
    value = list(a_dictionary.keys())[list(a_dictionary.values()).index(maxx)]
    return value
