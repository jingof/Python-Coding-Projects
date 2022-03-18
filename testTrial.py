from collections import Counter
#######################################################
#################### PROBLEM 1 ########################
#######################################################

def reduceString(myStr):
    c = Counter(myStr)
    res = ""
    for key in c.keys():
        if c.get(key)%2 == 1:
            res += key
    if res == "":
        return "Empty String"
    return res

def reduceString2(s):
    s = list(s)
    i = 0
    lenn = len(s)
    while True:
        if i >= lenn-1:
            break
        if s[i] == s[i+1]:
            del s[i+1]
            del s[i]
            lenn -= 2
            if i != 0:
                i -= 1
        else:    
            i+=1
    return s
        

lString = "baab"
#lString = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
#print(reduceString(lString))

#######################################################
#################### PROBLEM 2 ########################
#######################################################
def countWords(s):
    up = [i for i in s if i.isupper()]
    return len(up)+1
    
#countWords("saveChangesInTheEditor")

#######################################################
#################### PROBLEM 3 ########################
#######################################################
def strongifyPassword(pswd):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    chN = False
    chU = False
    chL = False
    chS = False 
    for c in pswd:
        if not chN and c in numbers:
            chN = True
        elif not chL and c in lower_case:
            chL = True
        elif not chU and c in upper_case:
            chU = True
        elif not chS and c in special_characters:
            chS = True
    lis = [chN,chS, chL, chU]
    ch = 0
    for l in lis:
        if l == False:
            ch+=1
    if len(pswd) > 5:
        print("67")
        return ch
    lenShort = 6 - len(pswd)
    if lenShort > ch:
        return lenShort
    else:
        return ch

#print(strongifyPassword("Ab1"))

#######################################################
#################### PROBLEM 4 ########################
#######################################################
def checkDuplication(s):
    dups = [s[i] for i in range(len(s)-1) if s[i] == s[i+1]]
    if len(dups) == 0:
        return False
    return True
def possiblePairs(lista):
    lista = list(set(lista))  
    lista = [i for i in lista if i.isalpha()] 
    lista = [[x,y] for x in lista for y in lista if x != y]
    res = []
    for val in lista:
        if [val[0],val[1]] not in res and [val[1],val[0]] not in res:
            res.append(val)
    return res
    
def getOtherPairs(pair, s):
    s = ''.join(list(set(s)))
    for p in pair:
        s = s.replace(p,'')     
    return s

def alternatinChars(s):
    pairs = possiblePairs(s)
    tracker = []
    for pair in pairs:
        otherChars = getOtherPairs(pair,s)   
        val = ''.join(list(s))
        for c in otherChars:
            val = val.replace(c,'')
        if not checkDuplication(val):
            tracker.append(val)
    if len(tracker) == 0:
        return 0
    lens = [len(i) for i in tracker]
    return max(lens)
    
#print(alternatinChars("asdcbsdcagfsdbgdfanfghbsfdab"))

#######################################################
#################### PROBLEM 5 ########################
#######################################################
def ceasorCipher(s,k):
    new = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                i = ord(i)+k
                while i > ord('z'):
                    i = ord('a') + i - ord('z') - 1  
                i = chr(i)
            else:
                i = ord(i)+k
                if i > ord('Z'):
                    i = ord('A') + i - ord('Z') - 1   
                i = chr(i)    
        new += i
    print(new)

    pass

s = "www.abc.xy"
print(s)
print(ceasorCipher(s, 87))

