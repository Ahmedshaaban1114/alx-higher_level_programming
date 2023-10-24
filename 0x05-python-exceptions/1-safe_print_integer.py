#!/usr/bin/python3
def safe_print_integer(value):
    i = 0
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError)
    return False
