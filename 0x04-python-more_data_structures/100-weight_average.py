#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    w = 0
    we = 0
    for t in my_list:
        w += t[1]
        we += t[0] * t[1]
    return we / w
