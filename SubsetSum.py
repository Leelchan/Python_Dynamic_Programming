'''
Given a set of non-negative integers, and a value sum, 
determine if there is a subset of the given set with sum equal to given sum.

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || 
                           isSubsetSum(set, n-1, sum-set[n-1])
'''

def SubsetSum(l, s):
    if len(l) == 0 and s != 0: return False
    if s == 0: return True
    
    return (SubsetSum(l[0:-1], s) or SubsetSum(l[0:-1], s - l[-1]))

def SubsetSumDivisibleBym(l, m, sum):
    if len(l) == 0 and s != 0: return False
    if sum % m == 0 and sum != 0: return True

    return SubsetSumDivisibleBym(l[0:-1], m, sum + l[-1]) or SubsetSumDivisibleBym(l[0:-1], m, sum)


l = [3, 34, 4, 12, 5, 2]
s = 9
m = 35

print (SubsetSum(l, s))

print (SubsetSumDivisibleBym(l, m, 0))