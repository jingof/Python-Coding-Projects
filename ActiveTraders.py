"""
An institutional broker wants to review their book of customers to see who is most active.
Given a list of trades by customer name, determine which customer accounts for atleast 5% of
the total number of trades. Order the list alphabetically ascending by name.

Example:
customers = ['Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 
            'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega',
             'Alpha', 'Omega', 'Alpha', 'Omega', 'Beta']

"""
from collections import Counter
import numpy as np
def Solution(customers): 
    lenn = len(customers)
    fivePercent = 0.05 * lenn
    print(fivePercent)
     
    uniqueSet = list(set(customers))
    uniqueLen = len(uniqueSet)
    uniqueness = [uniqueSet[i] for i in range(uniqueLen) if float(customers.count(uniqueSet[i])) >= fivePercent]
    uniqueness.sort()
    print(uniqueness)
    uniqueCount = [customers.count(i) for i in uniqueSet]
    percents = [float(i/lenn) for i in uniqueCount]
    morethan5percent = [uniqueSet[i] for i in range(len(uniqueCount)) if percents[i] >= 0.05]
    morethan5percent.sort()
    
    
    print("Set ",uniqueSet)
    print("count ",uniqueCount)
    print("percent",percents) 
    print("fiinal",morethan5percent)



customers = ['Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 
            'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega', 'Alpha', 'Omega',
             'Alpha', 'Omega', 'Alpha', 'Omega', 'Beta']
             
def Soln2(customers):
    fivePercent = 0.05 * len(customers)
    c = Counter(customers)
    lista = [key for key, val in c.items() if float(val) >= fivePercent]

   


    print(lista)
    print(c)
    #keys = c.keys()
    #values = c.values()
    #perc = c.
    #lenn = 
    #lenn
    #print(keys)
    #print(values)

customers2 = ['Alpha','Beta','Zeta','Beta','Zeta','Zeta','Epsilon',
            'Beta','Zeta','Beta','Zeta','Beta',
            'Delta','Zeta','Beta','Zeta','Beta','Zeta','Beta','Zeta','Beta']
Soln2(customers2)


