"""
Given a 1-index array of zeros with size n, and a list of operations, for each operation add a value
to each array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array. 

Example:
n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]  # operations are in format [a,b,k]

    Create an 1-indexed array filled with zeroes with size 10.
    For operation [1,5,3], add 3 to all indices between 1 and 5 inclusive.
    Do this for all operations, return the max value in the array
"""

from collections import Counter

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def Solution(n, queries):
    # Write your code here
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum
    

n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]
print(Solution(n,queries))
print('here')

filereader = open("manipulationInput.txt")
lines = filereader.readlines()
lines = [line.strip('\n') for line in lines]
lines = [line.split(" ") for line in lines]
lines = [ list(map(int,line)) for line in lines]
n = lines[0][0]
print(n)
del(lines[0])
print(len(lines))
print(lines[0:3])
print(Solution(n,lines))

