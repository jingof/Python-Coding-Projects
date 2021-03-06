"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly n steps, 
for every step it was noted if it was an uphill, , or a downhill, step. 
Hikes always start and end at sea level, and each step up or down represents a
unit change in altitude. We define the following terms:
    - A mountain is a sequence of consecutive steps above sea level, 
        starting with a step up from sea level and ending with a step down to sea level.
    - A valley is a sequence of consecutive steps below sea level, 
        starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 
"""

def countingValleys(steps, path):
    heightAboveSeaLevel = 0
    valleys=0
    for step in path:
        if step == "D":
            if  heightAboveSeaLevel == 0:
                valleys+=1 
            heightAboveSeaLevel-=1

        elif step == "U":
            heightAboveSeaLevel+=1
        else:
            continue
    return valleys


paths = ["UDDDUDUU","UDDDUDUU", "DDUUDDUDUUUD"]
for path in paths:   
    V = countingValleys(8, path)
    print(f"Valleys traversed for route {path} are = {V}")
