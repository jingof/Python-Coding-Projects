from collections import Counter
def Solution(files,numCores, limit):
    c = Counter(files)
    print()
    keys = list(c.keys())
    values = list(c.values())
    print(keys)
    
    value = [int((keys[i]/numCores)) if keys[i]%numCores == 0 else keys[i] for i in range(len(keys))]
    value = [value[i] * values[i]  for i in range(len(keys))]
    
    return sum(value)
    print(value)
   

    
    print(c)



files = [5, 3, 1] 
numCores = 5
limit = 5
Solution(files, numCores, limit)