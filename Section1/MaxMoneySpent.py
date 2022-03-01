"""
A person wants to determine the most expensive computer keyboard and USB drive that 
can be purchased with a given budget. Given price lists for keyboards and USB drives and a budget, 
find the cost to buy them. If it is not possible to buy both items, return -1.

Example
b = 60 
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a 40 keyboard + 12 drive =  52, or a 40 keyboard + 8 drive =  58.
Choose the latter as the more expensive option and return 58.

Function Description

Complete the getMoneySpent function in the editor below.

Parameter(s):
        int keyboards[n]: the keyboard prices
        int drives[m]: the drive prices
        int b: the budget

Returns
    int: the maximum that can be spent, or -1 if it is not possible to buy both items
"""

budget1 = 10
keyboards1 = [3,1]
drives1 = [5,2,8]

budget2 = 5
keyboards2 = [4]
drives2 = [5]

budget3 = 60 
keyboards3 = [40,50,60]
drives3 = [5,8,12]


def Solution(b,k,d):
    if min(k)+min(d) > b:
        return -1
    maxx = 0
    for i in k:
        for j in d:
            if i+j > maxx and i+j <= b:
                maxx = i+j
    return maxx
    
val = Solution(budget1, keyboards1, drives1)
print(val)

val = Solution(budget2, keyboards2, drives2)
print(val)

val = Solution(budget3, keyboards3, drives3)
print(val)