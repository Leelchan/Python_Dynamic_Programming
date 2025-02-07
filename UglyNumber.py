'''
Ugly numbers are numbers whose "only" prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
'''

def findNthUglyNum(n):

    # i2, i3, i5 will indicate indices for 2,3,5 respectively 
    i2 = 0
    i3 = 0
    i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    ugly = [0 for i in range(n)]
    ugly[0] = 1
    
    for i in range(1, n): 
        # choose the min value of all available multiples 
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 
  
        # increment the value of index accordingly
        # i2/3/5 will get increment if they have the same value
        if ugly[i] == next_multiple_of_2: 
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        
        if ugly[i] == next_multiple_of_3: 
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        
        if ugly[i] == next_multiple_of_5:  
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return (ugly[-1])



n = input()

print (findNthUglyNum(int(n)))

