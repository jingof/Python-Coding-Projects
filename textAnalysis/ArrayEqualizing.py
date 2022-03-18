
def compute(a):
    a.reverse()
    return sum([a[i]*(i+1) for i in range(len(a))])

def minOperations(a):
    a = sorted(a, reverse=True)
    res = 0
    for i in range(len(a)):
        res += compute(a[:i+1])
    return res
    


arr = [4,2,1,3]
print(minOperations(arr))