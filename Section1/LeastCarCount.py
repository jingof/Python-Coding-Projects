"""
    Author: Francis
    Date: 01/03/2022
"""

"""
People are going for a ceremony, they have a meet-up station where
they agree to take as few cars as possible. What is the least 
number of cars they can take?
Parameters:
            P: an array with number of people in each car
            S: an array with number of seats in each car
"""

def solution(P,S):
    people = 0
    totalPeople = sum(P)
    neededCars = 0

    while(True):     
        maxSeat = max(S)
        ind = S.index(maxSeat)
        people += maxSeat
        neededCars += 1
        if people >= totalPeople:
            break  
        if type(ind) == list:
            del(S[ind[0]])
        else:
            del(S[ind])
    return neededCars


P = [1,4,1]
S = [1,5,1]
print(f"Least cars needed = {solution(P,S)}.")