#!/usr/bin/python3
"""
Module for class_to_json method.
"""

def class_to_json(obj):
    """
    class_to_json - returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: instance of a Class

    Returns:
        Dictionary description of the object's attributes.
    """
    return obj.__dict__
