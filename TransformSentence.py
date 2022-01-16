"""
    Author: Francis
    Date: 01/05/2022
"""


"""
We shall use the ASCII code hierachy of letters.

Given a sentence perform the following actions on each word;
1. Leave the first letter of each word as is.
2. For the other letters;
    a. If a letter is the same as the letter before it irrespective of the case, do nothing.
    b. If a letter is less than the letter before it, change it to lower case.
    c. If a letter is greater than the letter before it, change it to upper case.

NOTE: Tthe case only applies to point 2 a.
"""

def transformSentence(sentence):
    words = sentence.split(" ")
    newSent = ""
    for word in words:
        newWord = ""
        for i in range(len(word)):
            char = word[i]
            if i == 0:
                newWord = newWord+char    
                continue

            if char.lower() == word[i-1].lower():
                newWord = newWord + char

            elif char > word[i-1]:
                char = char.upper()
                newWord = newWord + char

            elif char < word[i-1]:
                char = char.lower()
                newWord = newWord + char
        newSent = newSent + newWord + " "


    return newSent.strip()

sentence = "coOL dog"
print(sentence)
newSentence = transformSentence(sentence)
print(newSentence)