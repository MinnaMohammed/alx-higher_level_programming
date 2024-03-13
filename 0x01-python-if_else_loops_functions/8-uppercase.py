#!/usr/bin/python3
def uppercase(str):
    modified_str = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            modified_str += chr(ord(str[i]) - 32)
        else:
            modified_str += str[i]
    print("{:s}".format(modified_str))
