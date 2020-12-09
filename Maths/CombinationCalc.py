import math

def findCombination(n, r):
    newn = n
    newr = r
    result = 0
    for i in range(r - 1):
        newn = newn * (n - (i + 1))
    for i in range(r - 1):
        newr = newr * (r - (i + 1))
    result = newn / newr
    return result



inputn = int(input("Insert n variable here: "))
inputr = int(input("Insert r variable here: "))

print(int(findCombination(inputn, inputr)))
