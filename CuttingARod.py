'''
Given a rod of length n inches and an array of prices that contains 
prices of all pieces of size smaller than n. Determine the maximum 
value obtainable by cutting up the rod and selling the pieces.
'''

def maxObtainableValue(price, n):
    dp = [0 for i in range (n)] #max value when the len = x

    max = dp[0]
    for i in range (n):
        pass

    return 0
    



price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print (maxObtainableValue(price, n))
