"""
    Author: Francis
    Date: 01/06/2022
"""

filereader = open("listsInput.txt")
lines = filereader.readlines()
lines = [line.strip('\n') for line in lines]
lista = []
for i in range(1, len(lines)):
    line = lines[i]
    line = line.split(' ')
    if(line[0] == 'insert'):
        lista.insert(int(line[1]), int(line[2]))
    elif(line[0] == 'print'):
        print(lista)
    elif(line[0] == 'remove'):
        lista.remove(int(line[1]))
    elif(line[0] == 'append'):
        lista.append(int(line[1]))
    elif(line[0] == 'sort'):
        lista.sort()
    elif(line[0] == 'pop'):
        del(lista[len(lista)-1])
    elif(line[0] == 'reverse'):
            lista.reverse()
