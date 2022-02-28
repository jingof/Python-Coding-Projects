"""
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

Parameters:
            c: array with clouds numbering
Example
c = [0,1,0,0,0,1,0]
Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. 
They could follow these two paths: 0->2->3->4->6 or 0->2->4->6. The first path takes 4 jumps while the second takes 3. Return 3.
"""

def cloudsJump(c):
    indexWithJumps = []
    for i in range(len(c)):
        if i == 0 and c[i] == 0:
            indexWithJumps.append(i)
            continue
        if c[i] == 1:
            continue
        if i == len(c)-1 and c[i] == 0:
            indexWithJumps.append(i)
            break
        indBefore = i-1
        indAfter = i+1
        if c[indBefore]  != c[indAfter]:
            indexWithJumps.append(i)

        elif i not in indexWithJumps and indBefore not in indexWithJumps:
            indexWithJumps.append(i)

    return len(indexWithJumps)-1
    


cs= [[0,1,0,0,0,1,0], [0,0,1,0,0,1,0], [0,0,1,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,0,1,0]]

for c in cs:
    print(c, cloudsJump(c))

c = [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0]

print(c, cloudsJump(c))