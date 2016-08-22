#!/usr/bin/env python
# -*- coding: utf -8 -*-

from linked_list import LinkedList


class Stack(object):
    def __init__(self, param=None):
        """Create an instance of Stack.
        This is a composition with linked list."""
        self._parent = LinkedList(param)

    def __len__(self):
        """Return the length of the linked list for the built-in len."""
        return self._parent.__len__()

    def pop(self):
        """Remove a node from the head, return removed node."""
        return self._parent.pop()

    def push(self, val):
        """Insert a new node to the head of a stack."""
        return self._parent.push(val)
