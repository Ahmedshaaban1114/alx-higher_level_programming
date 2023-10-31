#!/usr/bin/python3
"""Module for add_integer"""

def add_integer(a, b=98):
    """Adds two integer

    Args:
    a: The first integer
    b: The seconed integer, defult = 98

    Raise:
    TypeError: if a, b are not int, float.

    Returns:
    the sum of two integer.
    """
    if type(a) not in (float, int):
        raise TypeError('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
