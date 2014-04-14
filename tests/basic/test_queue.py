#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_queue
----------------------------------

Tests for `python_algorithms.queue` module.
"""

import unittest

from python_algorithms.basic.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.empty_queue = Queue()
        self.queue = Queue()
        self.seq = [0, 2, 4, 6, 8]
        for x in self.seq:
            self.queue.enqueue(x)

    def test_enqueue_to_empty_queue(self):
        self.empty_queue.enqueue(0)
        self.assertEqual(self.empty_queue.peek(), 0)

    def test_enqueue_to_queue(self):
        self.queue.enqueue(10)
        for i in range(len(self.seq)):
            self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue_from_empty_queue(self):
        self.assertRaises(IndexError, self.empty_queue.dequeue)

    def test_dequeue_from_queue(self):
        self.assertEqual(self.queue.dequeue(), self.seq[0])

    def test_size_of_empty_queue(self):
        self.assertEqual(self.empty_queue.size, 0)

    def test_size_of_queue(self):
        self.assertEqual(self.queue.size, len(self.seq))

    def test_peek_at_empty_queue(self):
        self.assertRaises(IndexError, self.empty_queue.peek)

    def test_peek_at_queue(self):
        self.assertEqual(self.queue.peek(), self.seq[0])

    def test_iterate_empty_queue(self):
        for curr in self.empty_queue:
            self.assertEqual(False, True)

    def test_iterate_queue(self):
        iter_seq = []
        for curr in self.queue:
            iter_seq.append(curr)
        self.assertEqual(iter_seq, self.seq)

    def test_str_empty_queue(self):
        self.assertEqual(str(self.empty_queue), "")

    def test_str_queue(self):
        self.assertEqual(str(self.queue), " ".join([str(x) for x in self.seq]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
