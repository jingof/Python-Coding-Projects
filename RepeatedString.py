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



def Solution(s,n):
    if s == "a":
        return n
    
    indA = []
    for letter in s:
        if letter == 'a':
            indA = 
    lenS = len(s)
    newS = s
    ind = 0
    while len(newS) < n:
        newS+=s[ind]
        ind +=1
        if ind == len(s):
            ind = 0
    #print(newS, s, n)
    print(len(newS))
    #print(s,n)


s = "a"
n = 10000000
print(Solution(s,n))