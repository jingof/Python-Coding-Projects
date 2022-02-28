"""
Bowling Game Rules
The game consists of 10 frames. In each frame the player has two rolls to knock down 10 pins. 
The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.
A spare is when the player knocks down all 10 pins in two rolls. The bonus for that 
frame is the number of pins knocked down by the next roll.
A strike is when the player knocks down all 10 pins on his first roll. 
The frame is then completed with a single roll. The bonus for that frame is the value of the next two rolls.
In the tenth frame a player who rolls a spare or strike is allowed 
to roll the extra balls to complete the frame. However no more than three balls can be rolled in tenth frame.

Requirements
Write a class Game that has two methods
    # 1. roll(int) is called each time the player rolls a ball. The argument is the number of pins knocked down.
    # 2. score() returns the total score for that game.

10 frames
each frame - 2 rolls
each roll - chance to knoeck down 10 pins
score is computed at frame level
score is total number of pins knockedDown
"""

def score(rollsList):
    i = 0
    totalScore = 0
    bonus = 0
  
    while i < len(rollsList):
        if rollsList[i] == 10:
            bonus = sum(rollsList[i+1:i+3]) 
            totalScore+=10
            totalScore+=bonus
            i+=1
            continue
    
        frame = rollsList[i:i+2]
        totalScore += sum(frame)
        if sum(frame) == 10:
            bonus = rollsList[i+2]
            totalScore += bonus
        i+=2
    return totalScore
      

  

 


def roll(pinsKnockedDown):
  if pinsKnockedDown == 10:
    # this is a spike
  
    pass

  pass

score([5,3,2,5,2,5,7,3,10,0,5,8,1,9,1,10,2,4])

