#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if  a_dictionary is None:
        return
    for k in sorted(a_dictionary.keys()):
        print("{} : {}".format(k, a_dictionary.get(k)))

def update_dictionary(a_dictionary, key, value):
    n_dic = {key: value}
    a_dictionary.update(n_dic)
    return a_dictionary
