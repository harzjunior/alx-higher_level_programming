#!/usr/bin/python3
"""
1-write_file module
"""

def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout.
    Args:
        filename: name of the file to be read (default: "")
    Returns: None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
