#!/usr/bin/python3
'''is_same_class module'''


def is_same_class(obj, a_class):
    '''
    A function finds if the object is exactly an
    instance of the specified class

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    '''
    return type(obj) is a_class
