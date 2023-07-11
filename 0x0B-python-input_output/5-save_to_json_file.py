#!/usr/bin/python3
"""
5-save_to_json module
"""

import json

def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an object to a text file, using a JSON representation.
    Args:
        my_obj: object to be saved as JSON
        filename: name of the file to save the JSON representation
    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
