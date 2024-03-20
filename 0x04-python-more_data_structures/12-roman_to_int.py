#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is not True or roman_string is None:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    prev = ''
    for char in roman_string:
        if char in dic:
            if prev != '' and dic[char] > dic[prev]:
                summ += dic[char] - 2*(dic[prev])
            else:
                summ += dic[char]
            prev = char
    return (summ)
