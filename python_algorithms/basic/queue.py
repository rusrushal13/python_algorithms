#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a linked list based queue data structure.

A queue is a data structure to hold a collection of items in order ad which
supports operations such as the addition of an item (*enqueue*) and removal of
an item (*dequeue*) can be performed. The items are always enqueued at the rear
end of the queue and dequeued from the front end of the queue. As such, the
queue can be also viewed as a First-In-First-Out(*FIFO*) data structure. In a
FIFO data structure, the first item added to the structure is the first one to
be removed. Apart from those two operations, *peek*  operation can also be
implemented, returning the value at the front end without removing it.

The particular implementation of queue in this module is based on linked list,
as array based queue implementation is already supported in python's list. In
the linked list based implementation, the queue object need to keep track of
the front and the rear nodes where each node contains an item and a link to the
next node.

..  note:: For most practical purposes, the python's implementation as dequeue
    suffices as a queue object. Use append method instead of enqueue and
    popleft method instead of dequeue for queue operations in a list.

Complexity:
    * push -- O(1)
    * pop  -- O(1)
    * peek -- O(1)
"""


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
