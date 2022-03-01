def pickingNumbers(a):
    subArrayLen = 0
    a.sort()
    groups = []
    for i in range(len(a)-1):
        group = []
        group.append(a[i])
        for j in range(i+1,len(a)):
            if abs(a[i]- a[j]) <= 1:        
                group.append(a[j])
        if len(group) > 1:
            groups.append(group)
    for group in groups:
        if len(group) > subArrayLen:
            subArrayLen = len(group)
    return subArrayLen
            

a = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(a))

a2 = [1, 2, 2, 3, 1, 2]
print(pickingNumbers(a2))

