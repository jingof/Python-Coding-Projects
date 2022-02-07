"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, 
but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""

def Solution(q):
    newArray = list(range(1,len(q)+1))
    totalBribes = 0
    j = 0
    changed = True  
    while changed == True:     
        changed = False
        if j >= len(q):
            break
        num1 = q[j]
        
        if num1 > newArray[j] and num1 != newArray[j]:
            print(num1)
            print(newArray)    
            removed = newArray.copy()
            orig = newArray.copy()
            removed.remove(num1)
            newArray = newArray[:j] + [num1] + removed[j:]
            print(newArray)
            print(q)      
            totalBribes+= abs(num1 - j-1)
            if num1-j-1 > 2:
                print("Too Chaotic")
                return "Too Chaotic"
            print(num1-j-1,totalBribes)
            diff = [orig[i] for i in range(len(orig)) if orig[i] != newArray[i]]
            if len(diff) != 0:
                changed = True
                print(diff)
                j = 0
            else:
                j+=1        
        else:
            j+=1
            changed = True
            print("Here False")
        
        print()
    print(totalBribes)

q = [5, 1, 2, 3, 7, 8, 6, 4]
Solution(q)
print()
print()

print("Second")
q2 = [1, 2, 5, 3, 7, 8, 6, 4]
Solution(q2)

print()
print("Third")
q3 = [2, 1, 5, 3, 4]
Solution(q3)

print()
print("Fourth")
q4 = [1, 2, 5, 3, 4, 7, 8, 6]
Solution(q4)