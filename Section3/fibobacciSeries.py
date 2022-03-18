"""
Fibonacci Series
F(0) = 1
F(1) = 1
F(n) = F(n-1)+F(n-2)
"""

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(i, ", ", fibonacci(i))

i = 12
print(i, ", ", fibonacci(i))

