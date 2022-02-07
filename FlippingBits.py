"""
You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) 
and return the result as an unsigned integer. 
"""


def Solution(num):
    string = ""
    val = num
    while num > 2:
        mod = num%2
        num = int(num/2)
        string = str(mod) + string
        if num < 2:
            string = str(num) + string
            break 
    if num == 2:
        string = "10" + string  
    print(string)
    strLen = len(string)
    newString = [1 if x=='0' else 0 for x in string]

    newString = ([1] * (32-strLen)) + newString
    print(newString)
    value = [newString[i] * (2**(31-i)) for i in range(len(newString))]
    return sum(value)


print(Solution(9))
