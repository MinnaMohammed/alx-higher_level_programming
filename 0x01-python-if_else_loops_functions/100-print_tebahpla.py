#!/usr/bin/python3
cnt = 0
for i in reversed(range(97, 123)):
    if cnt % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
    cnt += 1
