#!/usr/bin/python3
""" import python modules """
import sys


if __name__ == "__main__":
    cnt = 1
    if len(sys.argv) == 1:
        print("{}".format("0 arguments."))
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("{}: {:s}".format(cnt, sys.argv[1]))
    else:
        print("{} {:s}:".format(len(sys.argv), "arguments"))
        for i in range(1, len(sys.argv)):
            print("{}: {:s}".format(i, sys.argv[i]))


