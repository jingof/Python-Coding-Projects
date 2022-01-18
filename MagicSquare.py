"""
We define a magic square to be an n*n matrix of distinct positive integers from 1 to n-squared 
where the sum of any row, column, or diagonal of length n is always equal to the same number: 
the magic constant.

You will be given a 3*3 matrix s of integers in the inclusive range [1,9]. We can convert any a
digit to any other digit b in the range [1,9] at cost of [a-b]. Given s, convert it into a 
magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].
Example
$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]  can be converted to [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
at a cost of |5-8|+|8-9|+|4-7| = 7
"""

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]] 
s2 = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]

 
def magicSquare(m):
    
    cost = 0
    if m[1][1] != 5:
        cost += abs(m[1][1] - 5)
        m[1][1] = 5

    #mid Row correction
    midRow = m[1]
    both  = 0

    if midRow[0] in [1,9] and midRow[2] in [3,7]:
        both = 2
    elif midRow[2] in [1,9] and midRow[0] in [3,7]:
        both = 2
    elif midRow[2] in [1,9] or midRow[0] in [1,9]:
        both = 1
    elif  midRow[0] in [3,7] or midRow[2] in [3,7]:
        both = 0
    else:
        both = 3
    
    if both == 1:
        #print('1 , 9')
        val = [x for x in [1,5,9] if x not in midRow]
        if len(val) > 0:
            val = val[0]
            wrongVal = [x for x in midRow if x not in [1,5,9]][0]
            wrongInd = midRow.index(wrongVal)
            midRow[wrongInd] = val
            cost += (wrongVal-val)
    elif both == 0:
        #print('1 , 9')
        val = [x for x in [3,5,7] if x not in midRow]
        if len(val) > 0:
            val = val[0]
            wrongVal = [x for x in midRow if x not in [3,5,7]][0]
            wrongInd = midRow.index(wrongVal)
            midRow[wrongInd] = val
            cost += abs(wrongVal-val)
    print(midRow)
        
        


    

print(magicSquare(s2))