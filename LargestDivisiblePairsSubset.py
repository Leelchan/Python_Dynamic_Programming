'''
Given an array of n distinct elements, 
find length of the largest subset such that every pair 
in the subset is the larger element of the pair 
is divisible by smaller element.
'''

def largestDivPair(arr):
    arr.sort(reverse=True)
    n = len(arr)
    dp = [1 for i in range (n)]
    for i in range (n):
        for j in range (i + 1, n):
            if (arr[i] % arr[j] == 0):
                dp[i] += 1

    return max(dp)

arr = [10, 5, 3, 15, 20]
arr2 = [18, 1, 3, 6, 13, 17]
print (largestDivPair(arr2))

