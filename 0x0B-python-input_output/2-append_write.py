#!/usr/bin/python3
"""
Module for append_write function.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a file and return the number of characters.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    append_write()
