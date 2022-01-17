"""
This is based on a tic-tac-toe game also known as the XO game played on a board
Given an n by n matrix, with 3 a possibility of any of the 3 values ['X','O', '.']
    "X": Represents the moves made by player X
    "O": Represents the moves made by player O
    ".": Represents possibilities of spaces where moves are yet to be made

A solution should be implemented to predict the current state of the game
There are 4 possibilities ["X WIN","O WIN", "TIE","ONGOING"]
    "X WIN"   : When player X has won the game.
    "O WIN"   : When player O has won the game.
    "TIE"     : When both players can not win but the game is fully played.
    "ONGOING" : When neither player has won but theres still places to play.

A game is won on the following conditions:
    When a row or column has either only 'X' or either only 'O'
    When the two corner to corner diagonals have either only 'X' or either only 'O'
    These diagonals for an n by n matrix have a length of n each.

A game is ongoing if there is still '.' in the board and no one has won, otherwise 
the game is still  ongoing.

Example:
        Consider board with matrix [['X','O'],['O','.']], here the player O has won the game
        because one diagonal has "OO".

    . 
"""
def Solution(board):
    cols = len(board)
    rows = len(board)
    lista2 = []
    for i in range(cols):
        lista2.append(list(board[i]))
    
    for i in range(rows):
        row = lista2[i]
        phrase = ""
        for letter in row:
            phrase +=letter
        
        if "X"*rows in phrase:
            return "X WIN"
        if "O"*rows in phrase:
            return "O WIN"

    # traverse columns
    for j in  range(cols):
        phrase = ""
        for i in range(rows):
            phrase += lista2[i][j]
        if "X"*rows in phrase:
            return "X WIN"
        if "O"*rows in phrase:
            return "O WIN"

    #traverse diagonals
    diag = [board[i][i] for i in range(len(board))]
    lista = []
    
    lista.append("".join(diag))
    diag2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    lista.append("".join(diag2))
  
    for phrase in lista:
        if "X"*rows in phrase:
            return "X WIN"
        if "O"*rows in phrase:
            return "O WIN"
    
    for b in board:
        if '.' in b:
            return "ONGOING"
    return "TIE"
    

board = [['X', '.', '.', 'O'], ['.', 'X', 'O', '.'], ['.', 'O', 'X', '.'], ['O', 'X', 'X', 'O']]
print(Solution(board))

board = [['O','X'], ['X','.']]
print(Solution(board))

board = [['X','O','X'], ['O','X','O'],['O','X','O']]
print(Solution(board))

board = [['X','.','X'], ['O','X','O'],['O','X','O']]
print(Solution(board))