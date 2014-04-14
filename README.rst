===============================
Python Algorithms
===============================

.. image:: https://badge.fury.io/py/python_algorithms.png
    :target: http://badge.fury.io/py/python_algorithms
    
.. image:: https://travis-ci.org/mihassan/python_algorithms.png?branch=master
        :target: https://travis-ci.org/mihassan/python_algorithms

.. image:: https://coveralls.io/repos/mihassan/python_algorithms/badge.png?branch=master
        :target: https://coveralls.io/r/mihassan/python_algorithms?branch=master


Python Algorithms contains a collection of useful algorithms written in python.
The algorithms include (but not limited to) topics such as searching, sorting,
graph, and string theory.

This project is inspired from the textbook Algorithms, 4th Edition by Robert
Sedgewick and Kevin Wayne and associated book-site
http://algs4.cs.princeton.edu/home/. The goal of this book is summarized in the
following excerpt from the book-site:

    Our original goal for this book was to cover the 50 algorithms that every
    programmer should know. We use the word programmer to refer to anyone
    engaged in trying to accomplish something with the help of a computer,
    including scientists, engineers, and applications developers, not to mention
    college students in science, engineering, and computer science.

However, the algorithms for this project are not meant to be a ported version of
the algorithms found in the book. Efforts should be made to implement those
algorithms from the scratch following Pythonic coding style. Some of the
algorithms are well known and the reference for those algorithms should appear
in the documentation. While, some of the algorithms are very specific and
difficult implement in a different way while maintaining accuracy and
efficiency. Such algorithms appear in the scientific literatures and/or books
and those should be properly referenced as well.

Features
--------

* Mainly for educational purposes, but can be useful in certain practical scenarios as well.
* Consequently, built-in algorithms are avoided as much as possible and detailed
  implementation is done from the scratch.
* Preference is given towards a pythonic style rather than sticking to true OOP style.
* Free software: BSD license.
* Documentation: http://python_algorithms.rtfd.org.

Algorithms
----------

Here is a list of algorithms divided into packages. 

.. Note:: Not all of the algorithms have been fully implemented yet.

Basic
=====

A collection of few basic algorithms that do not fit in other packages. Trivial
algorithms and data structures that are built into python are skipped.

* Binary search
* Knuth shuffle
* Stack
* Queue
* Bag
* Union find

:Estimated Release: 0.2.0

Searching
=========

Specialized searching algorithms and/or corresponding data structures are included in this package.
Although some of the following data structures, such as Hash, are implemented in python, they have been implemented for demonstration purpose.
Unless, specific needs arise, the built-in data structures should be preferred in production code.

* BST
* Red black BST
* Hash

:Estimated Release: 0.3.0

Sorting
=======

* Insertion
* Selection
* Merge
* Quick
* Quick 3 way
* Shell
* Heap

:Estimated Release: 0.4.0

Graph
=====

* Graph
* Directed graph
* BFS
* BFS paths
* DFS
* DFS paths
* Topological

:Estimated Release: 0.5.0

String
======

* LSD
* MSD
* Quick 3 string
* TST
* KMP
* Rabin karp

:Estimated Release: 0.6.0

