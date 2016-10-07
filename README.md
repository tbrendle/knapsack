Small lib used to solve Knapsack problems
=========================================

Numpy is required 
KS with 10000 items and a capacity of 1000000 takes ~10s to compute on MacBook Air 2011.

How to use ? 
============ 

> from knapsack import knapsack

> values = [12, 10, 7]

> sizes = [10, 7, 6]

> capacity = 12.5

> knapsack(values, sizes, capacity)

(12.0, array([1, 0, 0]))

> knapsack([12, 10, 7], [10, 7, 6], 14)

(17.0, array([0, 1, 1]))


Run examples :
==============
> python example.py tests/test1.txt
 

Enjoy :) 