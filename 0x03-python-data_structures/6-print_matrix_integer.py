#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for x in matrix:
        if len(x) == 0:
            print()
        for a in range(len(x)):
            print("{:d}".format(x[a]), end="\n" if a is len(x) - 1 else" ")
