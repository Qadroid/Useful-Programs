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

inputItemCount = int(input("Insert number of items here: "))

## Currently I am going to use a max of 2 till I figure out how to combine and/or

inputRelation = input("Insert relation between the two combinations (and / or): ")
if inputRelation == "and":
    for i in range(2):
        inputn = int(input("Insert n variable here: "))
        inputr = int(input("Insert r variable here: "))
        globals()[i] = findCombination(inputn, inputr)
    print(int(globals()[0] + globals()[1]))
elif inputRelation == "or":
    for i in range(2):
        print("Insert variables for",i+1,"here:")
        inputn = int(input("Insert n variable here: "))
        inputr = int(input("Insert r variable here: "))
        globals()[i] = findCombination(inputn, inputr)
    print(int(globals()[0] * globals()[1]))
else:
    print("Error: Incorrect input")