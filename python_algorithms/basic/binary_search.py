#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binary_search(array, key):
    """ Serach location of key in sorted array.

    The method searches the location of the key in the array using binary searching algorithm.
    If it does not find the key, it return -1.

    Args:
        array: A sorted array where to search the key.
        key: A key to search for.

    Returns:
        The location of the key in the array if found.
        Otherwise returns -1.
    """

    lo, hi = 0, len(array)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if key < array[mid]:
            hi = mid - 1
        elif key > array[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    import sys
    import random

    print("Binary search")
    print("Generating a list with random numbers (1-100)")
    n = int(raw_input("How many numbers to genereate: "))
    array = sorted(list(set([random.randint(1, 100) for i in range(n)])))

    x = int(raw_input("Enter a number to search: "))
    p = binary_search(array, x)

    if p == -1:
        print(str(x) + " is not in the list")
    else:
        print("Found at position " + str(p))