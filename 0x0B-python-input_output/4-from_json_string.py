#!/usr/bin/python3
"""
4-from_json_string module
"""

import json

def from_json_string(my_str):
    """
    from_json_string - returns an object represented by a JSON string.
    Args:
        my_str: JSON string to be converted to an object
    Returns:
        Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
