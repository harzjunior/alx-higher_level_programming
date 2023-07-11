#!/usr/bin/python3
"""
append_write module
"""

def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF8) and returns the number of characters added.
    Args:
        filename: name of the file (default: "")
        text: text to be appended to the file
    Returns:
        The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
