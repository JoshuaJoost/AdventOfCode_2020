from functools import reduce

fileInput = []

with open("AdventOfCode_2020\\03_input") as f:
    fileInput = list(map(str, f.readlines()))

startingPosition = [0,0]
#[[index: 0 = movementRight, 1 = movementDown]]
movement = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree = '#'
treesEncountered = [0 for i in movement]

i = 0
for elem in fileInput:
    # trim \n
    fileInput[i] = elem.replace("\n","")
    i += 1

    # count trees encounter
    j = 0
    for move in movement:
        pos = i * move[0] % len(fileInput[i-1])

        if i - 1 + move[1] <= len(fileInput) - 1:
            if fileInput[i - 1 + move[1]][pos] == tree:
                treesEncountered[j] += 1
        
        j += 1

print(treesEncountered)
print(reduce(lambda x,y: x*y, treesEncountered, 1))

    
    


