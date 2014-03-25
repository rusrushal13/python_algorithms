===============================
Python Algorithms
===============================

.. image:: https://badge.fury.io/py/python_algorithms.png
    :target: http://badge.fury.io/py/python_algorithms
    
.. image:: https://travis-ci.org/mihassan/python_algorithms.png?branch=master
        :target: https://travis-ci.org/mihassan/python_algorithms

.. image:: https://pypip.in/d/python_algorithms/badge.png
        :target: https://crate.io/packages/python_algorithms?version=latest


Python Algorithms contains a collection of useful algorithms written in python. The algorithms include (but not limited to) topics such as searching, sorting, graph, and string theory.

This project is inspired from the textbook Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne and associated booksite http://algs4.cs.princeton.edu/home/. The goal of this book is summarized in the following excerpt from the booksite:

    Our original goal for this book was to cover the 50 algorithms that every programmer should know. We use the word programmer to refer to anyone engaged in trying to accomplish something with the help of a computer, including scientists, engineers, and applications developers, not to mention college students in science, engineering, and computer science.

However, the algorithms for this project are not simply a ported version of the algorithms found in the book. Rather they are implemented from the scratch following Pythonic coding style. Most of the algorithms are well known and can be found in many books and sites.

Features
--------

* Mainly for educational purpose, but can be useful in certain situations.
* Consequently, built-in algorithms are not used, rather fully implemented from the scratch.
* Preference towards pythonic code rather than OOP.
* Free software: BSD license
* Documentation: http://python_algorithms.rtfd.org.

Algorithms
----------

Here is a list of algorithms divided into packages. 
Note that, all of the algorithms have not yet been implemented.

Basic
=====

A collection of few basic algorithms that do not fit in other packages. 
Trivial algorithms and data structures that are built into python are skipped.

* Binary search
* Knuth shuffle
* Stack
* Queue
* Bag
* Union find

Searching
=========

Specialized searching algorithms and/or corresponding data structures are included in this package.
Although some of the following data structures, such as Hash, are implemented in python, they have been implemented for demonstration purpose.
Unless, specific needs arise, the built-in data structures should be preferred in production code.

* BST
* Red black BST
* Hash

Sorting
=======

* Insertion
* Selection
* Merge
* Quick
* Quick 3 way
* Shell
* Heap

Graph
=====

* Graph
* Directed graph
* BFS
* BFS paths
* DFS
* DFS paths
* Topological

String
======

* LSD
* MSD
* Quick 3 string
* TST
* KMP
* Rabin karp
