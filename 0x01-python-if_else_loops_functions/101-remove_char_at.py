#!/usr/bin/python3
def remove_char_at(str, n):
    modified_str = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        else:
            modified_str += str[i]
    return modified_str
