#!/usr/bin/python3
'''is_kind_of_class module'''


def is_kind_of_class(obj, a_class):
    '''checks if obj is an instance of, or if the obj is an instance
    of a class that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True or False.
    '''
    return(isinstance(obj, a_class))
