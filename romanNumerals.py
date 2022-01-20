def Solution(n):
    string = ""
    while (n >= 1000):
        n = n - 1000
        string += "M"
    
    while (n >= 900):
        n = n - 900
        string += "CM"
    while (n >= 500):
        n = n - 500
        string += "D"
    while (n >= 100):
        n = n - 100
        string += "C"
    while (n >= 90):
        n = n - 90
        string += "XC"
    while (n >= 50):
        n = n - 50
        string += "L"
    while (n >= 10):
        n = n - 10
        string += "X"
    if n >= 9:
        n = n - 9
        string += "IX"
    if n >= 8:
        n = n - 8
        string += "VIII"
    if n >= 7:
        n = n - 7
        string += "VII"
    if n >= 6:
        n = n - 6
        string += "VI"
    if n >= 5:
        n = n - 5
        string += "V"
    if n >= 4:
        n = n - 4
        string += "IV"
    while n >= 1:
        n = n - 1
        string += "I"
    
    print(string)
    return string

Solution(1958)
Solution(1990)
Solution(1994)