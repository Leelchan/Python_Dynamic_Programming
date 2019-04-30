'''
The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...
C0 = 1
Cn+1 = sum from n to 0 Ci*Cn-i for n >= 0
'''

def findNthCatalanNum (n):
    if n == 0: return 0
    c = [0 for i in range(n)]
    c[0] = 1
    for i in range (1, n):
        for j in range (i):
            c[i] += c[j]*c[i - 1 - j]
    return c

'''
Cn = (1/(n + 1))(2n C n)
Binomial coefficient: nCk = n! / (k!(n - k)!)
''' 
def mutiAllElementinList(l):
    result = 1
    for e in l:
        result *= e
    return result

def BinomialCoef(n, r):
    return mutiAllElementinList([i for i in range (1, n + 1)]) / (mutiAllElementinList([i for i in range (1, r + 1)]) * mutiAllElementinList([i for i in range (1, n - r + 1)]))

def findNthCatalanNumUsingBinomialCoef (n): 
    c = [0 for i in range(n)]
    for i in range (n):
        c[i] = int ((1 / (i + 1))*BinomialCoef(2*i, i))
    return c

n = input()
print (findNthCatalanNum(int(n)))
print (findNthCatalanNumUsingBinomialCoef(int(n)))