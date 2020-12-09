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

inputItemCount = int(input("Insert number of combinations to combine here: "))
for i in range(inputItemCount):
        print("\n Input variables for", i+1, "here:")
        inputn = int(input("Insert n variable here: "))
        inputr = int(input("Insert r variable here: "))
        globals()[i] = findCombination(inputn, inputr)

for p in range(inputItemCount - 1):
    print("\n Relation between no. of combinations", p+1, "and", p+2)
    globals()[str(p)+"inputRelation"] = input("Insert relation between the two combinations (and / or): ")


# The following code works as long as long as addition is priotized as long as it precedes multiplication

# total = globals()[0]

# for q in range(inputItemCount - 1):
#     if globals()[str(q)+"inputRelation"] == "and":
#         total = total * globals()[q+1]
#     elif globals()[str(q)+"inputRelation"] == "or":
#         total = total + globals()[q+1]


# The following code respects the order of operation

total = globals()[0]

for q in range(inputItemCount - 1):
    if globals()[str(q)+"inputRelation"] == "and":
        total = total * globals()[q+1]

for q in range(inputItemCount - 1):
    if globals()[str(q)+"inputRelation"] == "or":
        total = total + globals()[q+1]

print("\n Your total is: ", total)


# Backup of old code

# if inputRelation == "and":
#     for i in range(2):
#         inputn = int(input("Insert n variable here: "))
#         inputr = int(input("Insert r variable here: "))
#         globals()[i] = findCombination(inputn, inputr)
#     print(int(globals()[0] * globals()[1]))
# elif inputRelation == "or":
#     for i in range(2):
#         print("Insert variables for",i+1,"here:")
#         inputn = int(input("Insert n variable here: "))
#         inputr = int(input("Insert r variable here: "))
#         globals()[i] = findCombination(inputn, inputr)
#     print(int(globals()[0] + globals()[1]))
# else:
#     print("Error: Incorrect input")