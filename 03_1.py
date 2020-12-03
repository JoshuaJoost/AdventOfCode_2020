fileInput = []

with open("AdventOfCode_2020\\03_input") as f:
    fileInput = list(map(str, f.readlines()))

startingPosition = [0,0]
#index: 0 = movementRight, 1 = movementDown
movement = [3,1]
tree = '#'

treesEncountered = 0
i = 0
for elem in fileInput:
    # trim \n
    fileInput[i] = elem.replace("\n","")
    i += 1

    # count trees encounter
    pos = i * movement[0] % len(fileInput[i-1])

    if i - 1 + movement[1] <= len(fileInput) - 1:
        if fileInput[i - 1 + movement[1]][pos] == tree:
            treesEncountered += 1

print(treesEncountered)

    
    


