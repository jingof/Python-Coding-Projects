"""
    Author: Francis
    Date: 01/16/2022
"""


"""
Given an array of socks with different socks colors
can you get the number of same color pairs that can
be formed with the socks.
Parameters:
            n: is the number of socks
            ar: is the list of socks 
"""

def sockMerchant(n,ar):
    colors = list(set(ar))
    pairs = 0
    for color in colors:
        socks = ar.count(color)
        colorPair = socks/2
        pairs += int(colorPair) 
    return pairs


num = 9
array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(f"Number of same color pairs = {sockMerchant(num,array)}.")