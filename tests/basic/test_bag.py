#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bag
----------------------------------

Tests for `python_algorithms.bag` module.
"""

import unittest

from python_algorithms.basic.bag import Bag


class TestBag(unittest.TestCase):

    def setUp(self):
        self.empty_bag = Bag()
        self.bag = Bag()
        self.seq = [1, 2, 2, 3, 3, 3]
        for x in self.seq:
            self.bag.add(x)

    def test_add_to_empty_bag(self):
        self.empty_bag.add(0)
        seq_iter = [x for x in self.empty_bag]
        self.assertEqual(len(seq_iter), 1)
        self.assertEqual(seq_iter[0], 0)

    def test_add_to_bag(self):
        self.bag.add(0)
        seq_iter = [x for x in self.bag]
        self.assertEqual(len(seq_iter), len(self.seq) + 1)
        self.assertEqual(sorted(seq_iter), [0] + self.seq)

    def test_size_of_empty_bag(self):
        self.assertEqual(self.empty_bag.size, 0)

    def test_size_of_bag(self):
        self.assertEqual(self.bag.size, len(self.seq))

    def test_iterate_empty_bag(self):
        for curr in self.empty_bag:
            self.assertEqual(False, True)

    def test_iterate_bag(self):
        iter_seq = []
        for curr in self.bag:
            iter_seq.append(curr)
        iter_seq.sort()
        self.assertEqual(iter_seq, self.seq)

    def test_str_empty_bag(self):
        self.assertEqual(str(self.empty_bag), "")

    def test_str_bag(self):
        bag_str = str(self.bag)
        bag_seq = sorted([int(x) for x in bag_str.split()])
        self.assertEqual(bag_seq, self.seq)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
