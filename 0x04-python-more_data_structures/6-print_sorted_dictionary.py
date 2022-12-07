#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dic_array = (sorted(a_dictionary.keys()))

    for key in sorted_dic_array:
        print("{:s}: {}".format(key, a_dictionary[key]))
