Statement
Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Given a positive integer, determine if it's the nth Fibonacci number for some n. If it is, print such n, otherwise print -1.

Example input
8

Example output
6

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/while_loop/     

You may also try step-by-step theory chunks:
https://snakify.org/lessons/while_loop/steps/1/



n = int(input())

a = 1
b = 1
k = 2
c = a + b

list = [a, b, c]

while c < n:
  a, b = b, c
  c = a + b
  list += [c]

if n in list:
  print(list.index(n)+1)
else:
  print(-1)


Model Solution

prev, next = 1, 1
index = 2
possible_fib = int(input())
while possible_fib > next:
  prev, next = next, prev + next
  index += 1
if possible_fib == next:
  print(index)
else:
  print(-1)