'''
Given a set of n elements, find number of ways of partitioning it.

Solution: use Bell triangle
The Bell triangle may be constructed by placing the number 1 in its 
first position. After that placement, the leftmost value in each row 
of the triangle is filled by copying the rightmost value in the previous row. 
The remaining positions in each row are filled by a rule very similar to that 
for Pascal's triangle: they are the sum of the two values to the left and upper 
left of the position.
'''
def bellNumber(n): 
  
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
  
        # Explicitly fill for j = 0 
        bell[i][0] = bell[i-1][i-1] 
  
        # Fill for remaining values of j 
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1] 
  
    return bell[n][0] 
  
# Driver program 
for n in range(6): 
    print('Bell Number', n, 'is', bellNumber(n)) 