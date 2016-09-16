#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
from collections import deque

class Graph(object):
    """Defining class Graph."""
    def __init__(self, iterable=None):
        """Initiate an instance of class Graph."""
        self._dict = {}
        try:
            for item in iterable:
                try:
                    self._dict.setdefault(item, [])
                except TypeError as e:
                    e.args = (
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)',
                        )
                    raise
        except TypeError:
            if iterable is not None:
                self._dict.setdefault(iterable, [])

    def add_node(self, n):
        """Add a node to graph."""
        try:
            self._dict.setdefault(n, [])
        except TypeError as e:
                    e.args = (
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)',
                        )
                    raise

    def add_edge(self, n1, n2, weight):
        """Add a edge from n1 to n2."""
        new_node = self._dict.setdefault(n1, [])
        self._dict.setdefault(n2, [])
        for tup in new_node:
            if n2 == tup[0]:
                raise ValueError('This edge already exists.')
        else:
            new_node.append((n2, weight))

    def nodes(self):
        """Show all nodes."""
        return self._dict.keys()

    def edges(self):
        """Show all edges."""
        list_key_value = self._dict.items()
        list_edges = []
        for pair in list_key_value:
            for tup in pair[1]:
                list_edges.append((pair[0], tup[0], tup[1]),)
        return list_edges

    def del_node(self, n):
        """Delete a node from graph."""
        if n in self._dict:
            del self._dict[n]
            for key in self._dict:
                for tup in self._dict[key]:
                    if n in tup:
                        self._dict[key].remove(tup)
        else:
            raise KeyError('No such node in the graph.')

    def del_edge(self, n1, n2):
        """Delete a edge from n1 to n2."""
        try:
            for tup in self._dict[n1]:
                if n2 in tup:
                    self._dict[n1].remove(tup)
        except KeyError as e:
            e.args = ('No such edge exists',)
            raise

    def has_node(self, n):
        """Check if n is a node of graph."""
        if n in self._dict.keys():
            return True
        else:
            return False

    def neighbors(self, n):
        """Return a list of nodes that have edge connect to n."""
        try:
            return [x[0] for x in self._dict[n]]
        except KeyError as e:
            e.agrs = ('Node not in the graph',)
            raise

    def adjacent(self, n1, n2):
        """Check if 2 nodes has connection."""
        try:
            n1_neighbors = [x[0] for x in self._dict[n1]]
            n2_neighbors = [x[0] for x in self._dict[n2]]
            return n2 in n1_neighbors or n1 in n2_neighbors
        except KeyError as e:
            e.agrs = ('Node not in the graph',)
            raise

    def depth_first_traversal(self, start):
        """
        Perform a full depth-traversal of the graph beggining at start.
        Return full visited path when traversal is complete.
        Raise a ValueError, if the graph is empty.
        """
        if self._dict == {}:
            raise ValueError("Can't traverse an empty graph.")
        path_list = [start]
        visited_list = [start]
        current_node = start
        while current_node:
            for n in self.neighbors(current_node):
                if n not in path_list:
                    path_list.append(n)
                    visited_list.append(n)
                    current_node = n
                    break
            else:
                try:
                    visited_list.pop()
                    current_node = visited_list[-1]
                except IndexError:
                    break
        return path_list

    def breadth_first_traversal(self, start):
        """
        Perform a full breadth-traversal of the graph beggining at start.
        Return full visited path when traversal is complete.
        Raise a ValueError, if the graph is empty.
        """
        if self._dict == {}:
            raise ValueError("Can't traverse an empty graph.")
        path_list = [start]
        pending_list = []
        current_node = start
        while current_node:
            for n in self.neighbors(current_node):
                if n not in path_list:
                    path_list.append(n)
                    pending_list.append(n)
            try:
                current_node = pending_list.pop(0)
            except IndexError:
                break
        return path_list

    def neighbors_weight(self, n):
        """
        Return a list of neighbors of the node n and their weights
        as a tuple (node, weight)."""
        try:
            return self._dict[n]
        except KeyError as e:
            e.agrs = ('Node not in the graph',)
            raise

    def shortest_path_dijkstras(self, start, end):
        """
        Find the shortest path between two nodes in the graph
        with weighted edges,
        """
        if not self.has_node(start) and not self.has_node(end):
            raise ValueError('Node(s) is not in the graph')
        tentative_cost = {
            x: {'cost': float('inf'), 'path': None} for x in self._dict.keys()
        }
        tentative_cost[start]['cost'] = 0
        current_node = start
        pending_list = deque()
        pending_list.append(start)
        visited_list = []
        while len(pending_list) > 0 and end not in visited_list:
            for n in sorted(
                    self.neighbors_weight(current_node),
                    key=lambda x: x[1]
            ):
                if n[0] not in visited_list: pending_list.append(n[0])
                if tentative_cost[n[0]]['cost'] >\
                        tentative_cost[current_node]['cost'] + n[1]:
                    tentative_cost[n[0]]['cost'] =\
                            tentative_cost[current_node]['cost'] + n[1]
                    tentative_cost[n[0]]['path'] = current_node
            visited_list.append(current_node)
            try:
                current_node = pending_list.popleft()
            except IndexError:
                break
        if tentative_cost[end]['cost'] == float('inf'):
            raise ValueError(
                    'No path start from {} and end at {}'.format(start, end)
                )
        path = []
        next_node_to_insert = end
        while next_node_to_insert is not None:
            path.insert(0, next_node_to_insert)
            next_node_to_insert = tentative_cost[next_node_to_insert]['path']
        return path, tentative_cost[end]['cost']


if __name__ == '__main__':
    iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    gr = Graph(iterable)
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
        (8, 9), (9, 10), (1, 3), (1, 4), (1, 5), (1, 7), (1, 8), (2, 5),
        (2, 6), (2, 7), (2, 8), (2, 9), (3, 5), (3, 7), (3, 8), (3, 9)
    ]
    for edge in edges:
        gr.add_edge(edge[0], edge[1], 10)
    breadth = gr.breadth_first_traversal(1)
    depth = gr.depth_first_traversal(1)
    print(
        "For a graph with nodes {} \n and edges\n {}\n"
        "the results are:\n   depth traversal: {},\n   breadth traversal: {}."
        .format(iterable, edges, depth, breadth)
    )
