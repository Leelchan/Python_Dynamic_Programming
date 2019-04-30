'''
The Permutation Coefficient represented by P(n, k) 
is used to represent the number of ways to obtain 
an ordered subset having k elements from a set of n elements.
'''
def mutiAllElementinList(l):
    result = 1
    for e in l:
        result *= e
    return result

def PermutationCoef(n, k):
    return int (mutiAllElementinList([i for i in range (1, n + 1)]) / mutiAllElementinList([i for i in range (1, n - k + 1)]))

n, k = input().split(" ")
print (PermutationCoef(int(n), int(k)))