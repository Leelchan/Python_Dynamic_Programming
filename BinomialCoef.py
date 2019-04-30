'''
Write a function that takes two parameters n and k and returns the value of 
Binomial Coefficient C(n, k). 
'''

def mutiAllElementinList(l):
    result = 1
    for e in l:
        result *= e
    return result

def BinomialCoef(n, r):
    return int (mutiAllElementinList([i for i in range (1, n + 1)]) / (mutiAllElementinList([i for i in range (1, r + 1)]) * mutiAllElementinList([i for i in range (1, n - r + 1)])))

n, r = input().split(" ")
print (BinomialCoef(int(n), int(r)))