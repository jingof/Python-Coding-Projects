"""
    Author: Francis
    Date: 01/16/2022
"""

"""
Given an n by m matrix with each index having an alhpabetical character.
Also given a word, find how many occurances of the word exist in the matrix
either by row combinations, column combinations or diagonal combinations.

Parameters:
            board: matrix with the characters
            word: the word being searched for

Example:
    Given a matrix m =[['g', 'o','o'],['g', 'g','g'],['o', 'g','g'],['o', 'o','g']]
    and a word 'go', the program should return 3 occurances of the word.
    There is 1 occurance in the first row, 1 in the first column and 1 in the second column.

    Given a matrix m= [['a','a'],['a','a']], and a word='aa', your code should return 5 occurances
    ie all rows and all columns and the diagonal.

NOTE: There can be more than 1 occurance of the word in the formed string.

TEST: board = [['s', 'o', 's', 'o'], ['s', 'o', 'o', 's'], ['s', 's', 's', 's']]    word = "sos"
      board2 = [['a','a'],['a','a']]    word = "aa"
      board3 = [['z','z','z'],['z','z','z'],['z','z','z']]  word = "zz"

"""

def solution(board,word):
    rows = len(board)
    cols =  len(board[0])
    occurance = 0
    wordLen = len(word)
    
    #traverse rows
    for i in range(rows):
        row = board[i]
        phrase = ""
        for letter in row:
            phrase +=letter
            if word in phrase:                          # takes care of the multiple occurances in the columns strings
                occurance+=1
    
    # traverse columns
    for j in  range(cols):
        phrase = ""
        for i in range(rows):
            phrase += board[i][j]
            if word in phrase:                          # takes care of the multiple occurances in the columns strings
                occurance+=1
    
    #traverse diagonals
    words = ["" for i in range(rows+cols-1)]
    # gets the words formed in the diagonals
    for r in range(rows):
        for c in range(cols):
            i = c-r+rows-1
            words[i] = words[i]+board[r][c]
            
    for phrase in words:
        if len(phrase) > len(word):                     # takes care of the multiple occurances in the diagonal strings
            for i in range(len(phrase)):
                phrase2 = phrase[i:i+len(word)]
                if word in phrase2:
                    occurance+=1

        elif word in phrase:
            occurance+=1          
    return occurance

board = [['s', 'o', 's', 'o'],
         ['s', 'o', 'o', 's'],
         ['s', 's', 's', 's']]

word = "sos"
print(solution(board,word))

board2 = [['a','a'],['a','a']]
word2 = 'aa'
print(solution(board2,word2))

board3 = [['z','z','z'],['z','z','z'],['z','z','z']]
word3 = 'zz'
print(solution(board3,word3))

