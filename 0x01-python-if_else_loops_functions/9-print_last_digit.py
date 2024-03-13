#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number * -1
    else:
        num = number
    last_digit = num % 10
    return last_digit
