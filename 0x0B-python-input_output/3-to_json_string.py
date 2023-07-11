#!/usr/bin/python3
"""
3-to_json_string module
"""
import json

def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation of an object (string).
    Args:
        my_obj: object to be converted to JSON
    Returns:
        JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
