#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_union_find
----------------------------------

Tests for `python_algorithms.union_find` module.
"""

import unittest

from python_algorithms.basic.union_find import UF


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.N = 10
        self.uf = UF(self.N)
        self.pairs = ((0, 1), (1, 2), (4, 5), (7, 8), (8, 9))

    def test_count(self):
        self.assertEqual(self.uf.count(), self.N)
        self.assertEqual(self.count_sets(), self.N)

        for x, y in self.pairs:
            self.uf.union(x, y)
        n = self.N - len(self.pairs)
        self.assertEqual(self.uf.count(), n)
        self.assertEqual(self.count_sets(), n)

    def test_str_empty_uf(self):
        self.assertEqual(str(UF(0)), "")

    def test_str_uf(self):
        self.assertEqual(str(self.uf), " ".join([str(x) for x in range(self.N)]))

    def count_sets(self):
        return len(set([self.uf.find(x) for x in range(self.N)]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
