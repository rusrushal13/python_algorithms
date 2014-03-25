#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_binary_search
----------------------------------

Tests for `python_algorithms.binary_search` module.
"""

import random
import unittest

from python_algorithms.basic import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.size = 100
        self.seq = range(self.size)

    def test_location(self):
        n = random.randrange(0, self.size)
        k = binary_search.binary_search(self.seq, n)
        self.assertEqual(n, k)

    def test_absence(self):
        n = 100
        k = binary_search.binary_search(self.seq, n)
        self.assertEqual(k, -1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()