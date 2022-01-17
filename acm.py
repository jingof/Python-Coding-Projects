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