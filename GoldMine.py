'''
Given a gold mine of n*m dimensions. Each field in this mine 
contains a positive integer which is the amount of gold in tons. 
Initially the miner is at first column but can be at any row. 
He can move only (right-> ,right up /, right down\) that is from 
a given cell, the miner can move to the cell diagonally up 
towards the right or right or diagonally down towards the 
right. Find out maximum amount of gold he can collect.
'''

def move(mine, c, r):
    gold = 0
    if r < 0 or r >= len(mine[0]) or  c < 0 or c >= len(mine): return 0
    
    gold = mine[c][r] + max(move(mine, c - 1, r + 1), move(mine, c, r + 1), move(mine, c + 1, r + 1))
    return gold

def GoldMine(mine):
    result = 0
    for i in range (len(mine[0])):
        temp = move(mine, i, 0)
        if (temp > result):
            result = temp
    return result


mine = [[1, 3, 3],
        [2, 1, 4],
        [0, 6, 4]]

mine2 = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

mine3 = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

print (GoldMine(mine3))


