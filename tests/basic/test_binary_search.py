#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_binary_search
----------------------------------

Tests for `python_algorithms.binary_search` module.
"""

import random
import unittest

from python_algorithms.basic import binary_search as bs


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.size = 100
        self.seq = list(range(self.size))

    def test_random_location(self):
        n = random.randrange(0, self.size)
        k = bs.search(self.seq, n)
        self.assertEqual(n, k)

    def test_first_location(self):
        n = 0
        k = bs.search(self.seq, n)
        self.assertEqual(n, k)

    def test_last_location(self):
        n = self.size - 1
        k = bs.search(self.seq, n)
        self.assertEqual(n, k)

    def test_absence(self):
        n = 100
        k = bs.search(self.seq, n)
        self.assertEqual(k, -1)

    def test_empty(self):
        k = bs.search([], 0)
        self.assertEqual(k, -1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
