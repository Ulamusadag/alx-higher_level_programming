#!/usr/bin/python3
"""Defines a file converting"""
import json


def to_json_string(my_obj):
    """Function converts to json

    Args:
        my_obj (str): nvghkg
    Returns:
        json representation
    """
    return json.dumps(my_obj)
