#!/usr/bin/python3
"""Define function"""
import json


def save_to_json_file(my_obj, filename):
    """define f"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
