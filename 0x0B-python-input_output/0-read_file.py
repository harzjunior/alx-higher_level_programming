#!/usr/bin/python3
"""
0-read_file.py module
"""

def read_file(filename=""):
    # Open the file in read-only mode with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        # Iterate over each line in the file
        for line in file:
            # Print each line to stdout without adding an additional newline character
            print(line, end='')
