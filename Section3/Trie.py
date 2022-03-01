"""
Trie data structure 
"""
import os

class Node:
    """
    Representation of a trie node
    Keeps a character, 26 children and 
    the boolean which tracks 
    if its end of a word.
    """
    def __init__(self, c): 
        """
        Initialises the node and sets the character
        initialises the children to None
        Initialises end of word to false
        """
        self.c = c  
        self.children = [None] * 26
        self.isWord = False
#############################################################################
################## ******** END OF CLASS ******** ###########################
#############################################################################
      
class Trie:
    """
    Representation of a trie structure
    Has a root from which all words are built
    The root keeps a null character and 26 Node 
    children representing 26 alphabet Letters

    It also keeps a scores List that stores scores 
    for the various alphabets
    """
    def __init__(self):
        """
        initialises the root the scores array

        """
        self.root = Node('\0')
        self.scores = [0] * 26
        self.maxWord = ""
        self.maxScore = 0

    def getRoot(self):
        """
        return the root
        """
        return self.root

    def addScore(self, c, score):
        """
        adds a letter's score to the scores list
        """
        c = c.lower()
        ind = ord(c) - ord('a')
        self.scores[ind] = int(score)

    def insertWord(self,word):
        """
        Adds a word to the trie structure

        """
        i=0
        currNode = self.root
        while i < len(word):
            c = word[i].lower()
            ind = ord(c) - ord('a')
            if not currNode.children[ind]:
                currNode.children[ind] = Node(c)
            currNode = currNode.children[ind]
            i+=1
        currNode.isWord = True
    
    def getScore(self, word):
        """
        gets the score of a word
        """
        i = 0
        score = 0
        while i < len(word):
            c = word[i]
            ind = ord(c) - ord('a')
            score += self.scores[ind]
            i+=1 
        return score

    def printWords(self, currNode ,word):
        """
        prints all words in the trie
        """
        if currNode.isWord:
            score = self.getScore(word)
            print(word,", ", score)
        for i in range(26):
            if not currNode.children[i]:
                continue
            c = currNode.children[i].c
            self.printWords(currNode.children[i],word+c)
    
    def getMaxWord1(self,randomString):
        """
        
        """
        self.maxScore = 0
        self.maxWord = ""
        self.getMaxWord(self.root,"",randomString)
        return self.maxScore, self.maxWord

 
    def getMaxWord(self, currNode, word, randomString):
        if currNode.isWord:
            score = self.getScore(word)
            if score > self.maxScore:
                
                self.maxScore = score
                self.maxWord = word
    
        for i in range(26):
            if not currNode.children[i]:
                continue
            c = currNode.children[i].c
            if c not in randomString:
                continue
            self.getMaxWord(currNode.children[i],word+c, randomString.replace(c,"",1))

#############################################################################
################## ******** END OF CLASS ******** ###########################
#############################################################################

path = os.path.dirname(os.path.abspath(__file__))
trie = Trie()

scoreFile = open(f"{path}/score.txt")
scoreFile.readline()
while True:
    line = scoreFile.readline()
    if not line:
        break
    c = line[0].lower()
    s = line[3:].replace("\n", "")  
    if c.isalpha():
        trie.addScore(c,s)


dictionaryFile = open(f"{path}/dictionary.txt")
while True:
    line = dictionaryFile.readline()
    if not line:
        break
    if line.strip() != "":
        trie.insertWord(line.strip())  

randomStringFile = open(f"{path}/test_random_string_500.txt")
outputFile = open(f"{path}/output.txt",'w')

while True:
    line = randomStringFile.readline()
    if not line:
        break
    line = line.strip()
    if line != "":
        maxS, maxW = trie.getMaxWord1(line) 
        if maxS == 0:
            maxW = line
        outputFile.write(f"{line}, {maxW}, {maxS}\n")

        