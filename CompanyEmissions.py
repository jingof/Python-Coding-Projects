"""
    Author: Francis
    Date: 01/02/2022
"""

"""
A company has stations that release given emissions.
The company plans to install filters to reduce the missions.
Given that each filter reduces the emission by half, what is 
the least number of filters need to installed to reduce 
the total company emissions by atleast half.

Parameters:
            A: is the company emissions array with emissions pers station
"""

def solution(A):
    B = A.copy()
    half = sum(A)/2.0
    filters = 0
    while(True):
        indMax = B.index(max(B))
        B[indMax] = B[indMax]/2.0
        sumB = sum(B)
        filters += 1
        if sumB <= half:
            break
    return filters

print(f"Least filters needed = {solution([5,19,8,1])}.")
