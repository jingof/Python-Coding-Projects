"""
Given a 6*6 2D Array, arr:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
a b c
  d  
e f g

here are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. 
The array will always be  6*6.

Example

 arr =  -9 -9 -9  1 1 1 
         0 -9  0  4 3 2
        -9 -9 -9  1 2 3
         0  0  8  6 6 0
         0  0  0 -2 0 0
         0  0  1  2 4 0
The 16 hourglass sums are:
        -63, -34, -9, 12, 
        -10,   0, 28, 23, 
        -27, -11, -2, 10, 
          9,  17, 25, 18
The highest hourglass sum 28 is from the hourglass beginning at row 1, column 2:
0 4 3
  1
8 6 6

"""

arr =  [[-9,-9, -9, 1, 1, 1], 
        [0, -9,  0, 4, 3, 2],
        [-9,-9, -9, 1, 2, 3],
        [0,  0,  8, 6, 6, 0],
        [0,  0,  0,-2, 0, 0],
        [0,  0,  1, 2, 4, 0]]


def Solution(arr):
    row1 = 0
    row2 = 1
    row3 = 2
    col1 = 0
    col2 = 1
    col3 = 2
    
    val = 0
    totals = []
    while val < 16:
        val+=1
        a = arr[row1][col1]
        b = arr[row1][col2]
        c = arr[row1][col3]
        d = arr[row2][col2]
        e = arr[row3][col1]
        f = arr[row3][col2]
        g = arr[row3][col3]
        total = a+b+c+d+e+f+g
        totals.append(total)
        if col3 < 5:
            col1+=1
            col2+=1
            col3+=1
        elif col3 == 5:
            row1+=1
            row2+=1
            row3+=1
            col1=0
            col2=1
            col3=2
    
    return max(totals)
            
        
        

    print(a,b,c,d,e,f,g)
    print(totals)
    #print(glasses)

Solution(arr)


