'''
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} 
valued coins, how many ways can we make the change? 
The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, 
{2,3,5} and {5,5}. So the output should be 5.
'''

def CoinChange(S, m , n):
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return CoinChange( S, m - 1, n ) + CoinChange( S, m, n-S[m-1] ); 
    

n = 4
S = [1, 2, 3]

print (CoinChange(S, len(S), n))