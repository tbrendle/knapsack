Small lib used to solve Knapsack problems
=========================================

Numpy is required 
KS with 10000 items and a capacity of 1000000 takes ~10s to compute on MacBook Air 2011.

How to use ? 
============ 

def knapsack(value, size, capacity):
"""
    Compute the optimum knapsack given values, sizes and capacity

    :param value: Array of values
    :param size: Array of sizes 
    :param capacity: Capacity of the knapsack
    :type value: list
    :type size: list
    :type capacity: float
    :return: a tuple (max value, repartition of items)
    :rtype: (float, list)

    :Example:
    >>> from knapsack import knapsack
    >>> knapsack([12, 10, 7], [10, 7, 6], 12.5)
    (12.0, array([1, 0, 0]))
    >>> knapsack([12, 10, 7], [10, 7, 6], 14)
    (17.0, array([0, 1, 1]))
"""

Run examples :
==============
>>> python example.py tests/test1.txt
 

Enjoy :) 