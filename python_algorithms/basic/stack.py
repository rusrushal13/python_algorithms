#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a linked list based stack data structure."""

class _Node(object):
    """ An internal class that represents a node with a single item 
    and links to other nodes.
    """
    
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack(object):
    """An implementation of a simple stack with linked list."""

    def __init__(self):
        """Initializes an empty stack."""
        self._head = None
        self._size = 0

    @property
    def size(self): 
        """The number of items in the stack."""    
        return self._size

    def isEmpty(self):
        """Check if the stack is empty.

        Returns:
            True if the stack is empty.
            False otherwise.
        """
        return self._size == 0

    def push(self, item):
        """Inserts an item to the stack."""
        n = _Node(item)
        n.next = self._head
        self._head = n
        self._size += 1

    def pop(self):
        """Remove and return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        n = self._head
        self._head = self._head.next
        self._size -= 1
        return n.item

    def peek(self):
        """Return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self._head.item

if __name__ == "__main__":
    import sys

    print("Stack using linked list")
    s = Stack()
    while True:
        n = int(raw_input("Enter a number to enter or 0 to pop a number (exit when stack empty): "))
        if n:
            s.push(n)
            print("Pushed: " + str(s.peek()))
        else:
            if s.isEmpty():
                print("Stack is empty.")
                break
            print("Popped: " + str(s.pop()))