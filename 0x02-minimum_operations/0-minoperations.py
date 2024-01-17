#!/usr/bin/python3
"""0-minoperations.py"""


def minOperations(n):
    """minOperations"""
    if n == 1:
        return 0

    my_n = 2
    counter = 2
    base = 0
    while my_n != n:
        my_n += base
        counter += base
        while my_n < n:
            my_n *= 2
            counter += 2
        if my_n == n:
            return counter
        if base == n:
            return 0
        my_n = 2
        counter = 2
        base += 1
