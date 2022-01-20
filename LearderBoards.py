"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, 
and the next player(s) receive the immediately following ranking number.

Example:
    ranked = [100,90,90,80]
    player = [70,80,105]

    The ranked players will have ranks 1, 2, 2, and 3, respectively. 
    If the other player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st. 
    Return [4,3,1].

Parameters:
        int ranked[n]: the leaderboard scores
        int player[m]: the player's scores

[4, 3, 3, 1]
[6, 4, 2, 1]
[6, 5, 4, 2, 1]
"""
def findClosestPos(ranked, i):
    lenn = len(ranked)
    if lenn == 1:
        return ranked[0]
    midPos = int(lenn/2)
    if i == ranked[midPos]:
        return ranked[midPos]
    elif i > ranked[midPos]:
        return findClosestPos(ranked[:midPos], i)
    elif i < ranked[midPos]:
        return findClosestPos(ranked[midPos:], i)


def Solution(ranked, player):
    ranked = list(set(ranked)) 
    ranked.sort()
    ranked.reverse()
    otherRanks = []
    lenn = len(ranked)

    for i in player:
        if i in ranked:
            otherRanks.append(ranked.index(i)+1)
        elif  i > ranked[0]:
            otherRanks.append(1)
        elif i < ranked[lenn-1]:
            
            otherRanks.append(lenn+1)
        else:
            value = findClosestPos(ranked, i)
            if i < value:
                poss = ranked.index(value)+1
            else:
                poss = ranked.index(value)
            otherRanks.append(poss+1)
    
    return otherRanks
    




r1 = [100,90,90,80]
p1 = [70,80,85,105]
print(Solution(r1, p1))

r2 = [100,100,50,40,40,20,10]
p2 = [5,25,50,120]
print(Solution(r2, p2))

r2 = [100,90,90,80,75,60]
p2 = [50,65,77,90,102]
print(Solution(r2, p2))


