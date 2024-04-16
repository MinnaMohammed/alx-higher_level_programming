#!/usr/bin/python3
'''inherits_from module'''


def inherits_from(obj, a_class):
    '''
    checks if obj inherits directly or indirectly from a_class
    and that obj is not an exact instance of a_class but rather
    an instance of a subclass of a_class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj inherits from a_class, otherwise False.
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
