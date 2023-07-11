#!/usr/bin/python3
"""
1-write_file.py
"""

def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8) and returns the number of characters written.
    Args:
        filename: name of the file (default: "")
        text: text to be written to the file
    Returns:
        The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
