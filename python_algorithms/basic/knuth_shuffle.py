#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a shuffle method using Knuth's algorithm."""


import random


def shuffle(seq):
    """Shuffle a list randomly using Knuth's algorithm.

    The method randomly shuffles a list by iterating over each position and
    exchanging the element with another random element.
    The original list is not maintained and will change.

    Args:
        seq: A list to shuffle.

    Returns:
        The original list with all elements shuffled.
    """

    N = len(seq)
    for i in range(N - 1):
        j = random.randint(i+1, N-1)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

if __name__ == "__main__":
    print("Knuth shuffle.")
    print("Generating a list with numbers (1-100)")
    seq = list(range(1, 101))

    print("The list after shuffling: ")
    shuffle(seq)
    print(seq)
