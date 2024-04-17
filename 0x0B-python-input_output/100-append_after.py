#!/usr/bin/python3
"""
Module for append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a text to a file, after each line containing a specific string.

    Args:
        filename (str): The name of the file to update.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each found line.

    Returns:
        None
    """
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


if __name__ == "__main__":
    append_after()
