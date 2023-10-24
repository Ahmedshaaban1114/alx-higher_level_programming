#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except Exception as i:
        print("Exception: ", i, file=sys.stderr)
        is_int = False
    return is_int
