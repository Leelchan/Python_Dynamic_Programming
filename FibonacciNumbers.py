'''
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ......

Recurrence relation:
Fn = Fn-1 + Fn-2
F0 = 0 and F1 = 1.

Given a number n, print n-th Fibonacci Number.
'''

#O(n)
def findNthFibonacciNum(n):
    if n == 0: return 0
    if n == 1: return 1
    f = [0 for i in range(n)]
    f[0] = 0
    f[1] = 1

    for i in range (2, n):
        f[i] = f[i - 1] + f[i - 2]

    return f[n - 1]


while True:
    n = input()
    print (findNthFibonacciNum(int(n)))