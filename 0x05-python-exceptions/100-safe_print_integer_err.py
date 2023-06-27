#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'\n".format(type(value).__name__), file=sys.stderr)
        return False
