
def Solution(p):
    words = p.split()
    vowels = 0
    consonants = 0
    hyphen = "-".join(words)
    addingV = ""
    reversing = ""
    reversedWords = []
    for word in words:    
        for l in word:
            if l.lower() in ['a','e','i','o','u']:
                addingV += "pv" + l
                vowels += 1
            else:
                consonants += 1
                addingV +=  l
            if l == l.lower():
                reversing =   reversing + l.upper()
            else:
                reversing =  reversing + l.lower() 
        addingV += " "
        reversedWords.append(reversing)
        reversing = ""
   
    reversedWords.reverse()
    reversedWords = " ".join(reversedWords)
    
    finalString = str(vowels)+ " " + str(consonants) + "::" + reversedWords + "::" + hyphen+ "::" + addingV
    print(finalString)
   
    
    
    
    










p = "ThIs is p"
Solution(p)


