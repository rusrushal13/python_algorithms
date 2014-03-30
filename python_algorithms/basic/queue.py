#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a linked list based queue data structure."""


class _Node(object):
    """An internal class that represents a node with a single value
    and links to other nodes.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue(object):
    """An implementation of a simple queue with linked list."""

    def __init__(self):
        """Initialize an empty queue."""
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
        """Insert an item to the queue."""
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

    def __iter__(self):
        """Return iterator for the queue."""
        current = self._first
        while current:
            yield current.item
            current = current.next

    def __str__(self):
        """String representation of the queue."""

        return " ".join([str(item) for item in self])

    def __repr__(self):
        """Representation of the queue."""

        return "Queue(" + str(self) + ")"

if __name__ == "__main__":
    print("Queue using linked list.")
    q = Queue()
    while True:
        n = int(raw_input("Enter a number to enter or 0 to pop a number"
                          " (exit when queue empty): "))
        if n:
            q.enqueue(n)
            print("Queued: " + str(n))
            print("Current queue: " + str(q))
        else:
            if q.isEmpty():
                print("Queue is empty.")
                break
            print("Dequeued: " + str(q.dequeue()))
            print("Current queue: " + str(q))
