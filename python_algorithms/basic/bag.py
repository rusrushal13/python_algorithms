#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a bag or multiset data structure.

A bag or multiset is a generalization of the set data structure which allows
repeated or duplicate items to be stored. Items can only be added to the bag
and may not be removed. When the items in the bag are iterated there is not
restriction  on the ordering of the items.

In this module, the implementation of bag is similar to a linked list based
stack implementation. In the linked list based implementation, the bag object
need to keep track of only the head node. Each node contains an item and a link
to the next node.

..  note:: Python' has a built-in class `collections.Counter
    <https://docs.python.org/2/library/collections.html#collections.Counter>`_
    which is similar to a bag or multiset. instead of adding an item, 1 need to
    be added with the counter associated with that item and elements return all
    items (including duplicates) in the bag.

Complexity:
    * add -- O(1)
"""


class _Node(object):
    """ An internal class that represents a node with a single item
    and links to other nodes.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class Bag(object):
    """An implementation of a bag or multiset with linked list."""

    def __init__(self):
        """Initializes an empty bag."""
        self._head = None
        self._size = 0

    @property
    def size(self):
        """The number of items in the bag."""
        return self._size

    def isEmpty(self):
        """Check if the bag is empty.

        Returns:
            True if the bag is empty.
            False otherwise.
        """
        return self._size == 0

    def add(self, item):
        """Inserts an item to the bag."""
        n = _Node(item)
        n.next = self._head
        self._head = n
        self._size += 1

    def __iter__(self):
        """Return iterator for the bag."""
        current = self._head
        while current:
            yield current.item
            current = current.next

    def __str__(self):
        """String representation of the bag."""
        return " ".join([str(item) for item in self])

    def __repr__(self):
        """Representation of the bag."""
        return "Bag(" + str(self) + ")"

if __name__ == "__main__":
    print("Bag using linked list")
    b = Bag()
    while True:
        n = int(raw_input("Enter a number to add to the bag"
                          "or enter 0 to exit:"))
        if n:
            b.add(n)
            print("Added: " + str(n))
            print("Current bag: " + str(b))
        else:
            break
