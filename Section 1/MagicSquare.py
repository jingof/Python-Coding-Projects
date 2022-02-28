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
def magicSquare1(s):
    magic_squares = [[8,1,6,3,5,7,4,9,2],
                     [8,3,4,1,5,9,6,7,2],
                     [4,9,2,3,5,7,8,1,6],
                     [4,3,8,9,5,1,2,7,6],
                     [6,7,2,1,5,9,8,3,4],
                     [6,1,8,7,5,3,2,9,4],
                     [2,9,4,7,5,3,6,1,8],
                     [2,7,6,9,5,1,4,3,8]]
    cost = 0
    s2 = []
    for i in s:
        for j in i:
            s2.append(j)
    min_score = 100000
    for s3 in magic_squares:
        cost = 0
        for i in range(len(s2)):
            cost += abs(s2[i] - s3[i])
        if min_score > cost:

            min_score = cost
  
    return min_score
    
s2 = [[7, 5, 5], [7, 4, 1], [1, 9, 3]]
print(magicSquare1(s2))
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]] 
print(magicSquare1(s))

s3 =[[4, 9, 2], [3, 5, 7], [8, 1, 5]]
print(magicSquare1(s3))

s4 =[[4, 8, 2], [4, 5, 7], [6, 1, 6]]
print(magicSquare1(s4))

s5 = [[2, 9, 8], [4, 2, 7], [5, 6, 7]]     
print(magicSquare1(s5))

