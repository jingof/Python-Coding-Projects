
def Solution(N, M):
    if N <= M:
        lista = list(range(N,M+1))
    else:
        lista = list(range(M,N+1))
    sequence = ['FizzBuzz' if x%15 == 0 else x for x in lista]
    sequence = ['Fizz' if isinstance(x,int) and x%3 == 0  else x for x in sequence]
    sequence = ['Buzz' if isinstance(x,int) and x%5 == 0 else x for x in sequence]
    
    
    print("".join([]))


Solution(1,5)

