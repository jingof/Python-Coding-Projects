"""
A team has players where every player has a rating.
A coach wants to pair players whose rating
diffee by no less than a given minimum. What is the 
maximum number of pairs that can be formed.

Example:
    n = 6
    ratings = [1,2,3,4,5,6]
    diff = 4

Only two pairs have a difference of 4 or more 
(1,5), (2,6)
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    # Write your code here
    print(minDiff)
    print(skillLevel)
    skillLevel.sort()
    lenn = len(skillLevel)
    if skillLevel[lenn-1] - skillLevel[0] < minDiff:
        return 0
    foundIndices = []
    pairs = []
    for i in range(lenn-1):
        if i in foundIndices:
            continue
        #3,11,12,13,14
        for j in range(i+1, lenn):
            if skillLevel[j] - skillLevel[i] < minDiff:
                continue
            if j in foundIndices:
                continue
            
            pairs.append([skillLevel[i], skillLevel[j]])
            foundIndices.append(i)
            foundIndices.append(j)
            break
    return len(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)

    fptr.write(str(result) + '\n')

    fptr.close()
