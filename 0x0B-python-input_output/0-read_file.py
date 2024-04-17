#!/usr/bin/python3
"""
Module for read_file function.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file()
