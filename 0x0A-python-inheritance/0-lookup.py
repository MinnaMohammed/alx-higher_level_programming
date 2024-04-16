#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """lookup method

    Returns:
        list: A list containing the names of the attributes and methods.
    """
    return dir(obj)
