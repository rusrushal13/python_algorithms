#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a linked list based queue data structure."""


class _Node(object):
    """ An internal class that represents a node with a single value
    and links to other nodes.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue(object):
    """An implementation of a simple queue with linked list."""

    def __init__(self):
        """Initializes an empty queue."""
        self._first = None
        self._last = None
        self._size = 0

    @property
    def size(self):
        """The number of items in the queue."""
        return self._size

    def isEmpty(self):
        """Check if the queue is empty.

        Returns:
            True if the queue is empty.
            False otherwise.
        """
        return self._size == 0

    def enqueue(self, item):
        """Inserts an item to the queue."""
        n = self._last
        self._last = _Node(item)
        if self.isEmpty():
            self._first = self._last
        else:
            n.next = self._last
        self._size += 1

    def dequeue(self):
        """Remove and return the first item from the queue.

        Returns:
            The first item from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        n = self._first
        self._first = self._first.next
        self._size -= 1
        return n.item

    def peek(self):
        """Return the first item from the queue.

        Returns:
            The first item from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("peek at empty queue")
        return self._first.item

if __name__ == "__main__":
    print("Queue using linked list")
    q = Queue()
    while True:
        n = int(raw_input("Enter a number to enter or 0 to pop a number"
                          " (exit when stack empty): "))
        if n:
            q.enqueue(n)
            print("Pushed: " + str(n))
        else:
            if q.isEmpty():
                print("Queue is empty.")
                break
            print("Dequeued: " + str(q.dequeue()))
