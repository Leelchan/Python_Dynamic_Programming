'''
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.
'''

def perfectSumProblem(l, s, path):
    if len(l) == 0 and s != 0: return
    if s == 0: 
        print (path)
        return
    path.append(l[-1])
    return (perfectSumProblem(l[0:-1], s, path[0:-1]) or perfectSumProblem(l[0:-1], s - l[-1], path))



arr = [2, 3, 5, 6, 8, 10]
arr2 = [1, 2, 3, 4, 5]

s = 10

perfectSumProblem(arr2, s, [])