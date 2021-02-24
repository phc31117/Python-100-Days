Statement
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, find the maximal element and print its row number and column number. If there are many maximal elements in different rows, report the one with smaller row number. If there are many maximal elements in the same row, report the one with smaller column number. 

Example input
3 4
0 3 2 4
2 3 5 5
5 1 2 3
(maximal element is highlighted)

# 2 2
# -1000000003 -1000000002
# -1000000002 -1000000001




Example output
1 2

# 1 1


Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/two_dimensional_lists_arrays/

You may also try step-by-step theory chunks:
https://snakify.org/lessons/two_dimensional_lists_arrays/steps/1/



import numpy as np

a, b = map(int, input().split())
x = [[int(i) for i in input().split()] for j in range(a)]





# a, b = map(int, input().split())
# m = [[int(j) for j in input().split()] for i in range(a)]

# list = m.flatten()
# ma = max(list)

# print(m.index(ma))
