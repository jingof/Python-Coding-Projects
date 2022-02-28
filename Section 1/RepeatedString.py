"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's in the first n
letters of the infinite string.

Example
s= "abcac"
n = 10
The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are
4 occurrences of a in the substring.

Function Description
Complete the repeatedString function in the editor below.
repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

Returns

    int: the frequency of a in the substring

"""



from audioop import mul


def Solution(s,n):
    if s == "a":
        return n
    indA = []
    for i in range(len(s)):
        letter = s[i]
        if letter == 'a':
            indA.append(i)
    lenS = len(s)
    multiple = int(n/lenS)
    remainder = n%lenS
    occurances = multiple * len(indA)
    for ind in indA:
        if ind < remainder:
            occurances+=1
    return occurances



   
   


s = "a"
n = 10000000

s= "abcac"
n = 5
print(Solution(s,n))