#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a binary search method."""


def search(seq, val):
    """Search location of key in a sorted list.

    The method searches the location of a value in a list using
    binary searching algorithm. If it does not find the value, it return -1.

    Args:
        seq: A sorted list where to search the value.
        val: A value to search for.

    Returns:
        The location of the value in the sorted list if found.
        Otherwise returns -1.
    """

    lo, hi = 0, len(seq)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if val < seq[mid]:
            hi = mid - 1
        elif val > seq[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    import random

    print("Binary search.")
    print("Generating a list with random numbers (1-100)")
    n = int(raw_input("How many numbers to generate: "))
    seq = sorted(list(set([random.randint(1, 100) for i in range(n)])))

    x = int(raw_input("Enter a number to search: "))
    p = search(seq, x)

    if p == -1:
        print(str(x) + " is not in the list")
    else:
        print("Found at position " + str(p))
