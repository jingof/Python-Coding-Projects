"""
1496 = 21
6941
6+(2*9)+4+(2*1) = 6+18+4+2 = 6+1+8+4+2 = 21
"""

def getChecksum(n):
    n = list(str(n))
    n.reverse()
 
    i = 0
    totalSummation = 0
    while i < len(n):
        section = n[i:i+2]
        summation = int(section[0])
        if len(section) == 2:
            second = str(int(section[1])*2)
            summation += int(second[0])
            if len(second) == 2:
                summation += int(second[1])
            
        totalSummation += summation
        i+=2
    return totalSummation
n = 1946
print(getChecksum(6789))
#print(len(1946))