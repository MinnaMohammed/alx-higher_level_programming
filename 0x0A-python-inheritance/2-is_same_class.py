#!/usr/bin/python3
'''is same class'''


def is_same_class(obj, a_class):
    '''
    A function finds if the object is exactly an
    instance of the specified class

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    '''
    return(type(obj) is a_class)
