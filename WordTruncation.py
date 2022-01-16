"""
    Author: Francis
    Date: 01/04/2022
"""


"""
Given a sentence 'message' and a length 'K'.
Trim the sentence to a 'phrase' to be of length less or equal to K
- The last word cannot be stripped, if it makes the phrase longer than K, 
    do not add the word.
- Spaces should be included when getting the length.
Parameters:
            message: sentence to be trimmed.
            K: The maximum length of the returned phrase

Example:
    Given a sentence "I like this dog", K=10
    the returned phrase should be "I like" 
    because "I like this" is longer than 10 
    and we can not strip "this"

"""
def Solution(message, K):
    words = message.split(" ")
    newWord = ""
    totalLen = 0
    for word in words:
        wLen = len(word)
        if totalLen+wLen <= K:
            totalLen = totalLen + 1 + wLen 
            newWord +=  word + " "
        else:
            break
    #print(newWord)
    return newWord.strip()

sentence = 'The quick brown fox jumps over the lazy dog'
k=28
phrase = Solution(sentence, k)
print(sentence)
print(k)
print(phrase)
print(len(phrase))
