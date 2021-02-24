Statement
Given two lists of numbers, find all the numbers that occur in both the first and the second list. Print them in ascending order.

Example input
1 3 2
4 3 2

Example output
2 3

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/sets/


s1 = {int(i) for i in input().split()}
s2 = {int(j) for j in input().split()}
join = s1&s2
list = sorted(list(join))
print(list)


 Model Solution

 first = set([int(s) for s in input().split()])
second = set([int(s) for s in input().split()])
print(*sorted(first & second))