"""
Soldiers really like sleeping and resting. n soldiers settle in k barracks following this set of rules:

    - soldiers come one at a time from 1 to n;
    - each soldier chooses the most empty barrack available. If he can choose from more than one equally 
    empty barracks, he chooses one of them randomly;

Your job is to find how many possible ways the soldiers can settle in barracks for a given pair (n, k). 
Two ways are considered distinct if at least one of the barracks has different soldiers. 
"""

def Solution(n,k):
    barracks = [0]*k
    options = 1
    i = 0
    while i < n:
        minn = min(barracks)
        counter = barracks.count(minn)    
        options *= counter   
        minInd = barracks.index(minn)  
        barracks[minInd] +=1
        i+=1      
    return options


n = 5
k = 2
Solution(n,k)
