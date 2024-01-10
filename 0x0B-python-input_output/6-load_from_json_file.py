#!/usr/bin/python3
"""define function"""
import json


def load_from_json_file(filename):
    """define function"""
    with open(filename) as f:
        return json.load(f)
