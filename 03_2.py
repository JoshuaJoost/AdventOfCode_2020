from functools import reduce

fileInput = []

with open("AdventOfCode_2020\\03_input") as f:
    fileInput = list(map(str, f.readlines()))

#[[index: 0 = movementRight, 1 = movementDown]]
movement = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree = '#'
treesEncountered = [0 for i in movement]

i = -1 # 0
for elem in fileInput:
    i += 1
    
    # trim \n
    fileInput[i] = elem.replace("\n","")

    j = -1 #0
    for move in movement:
        j += 1
        pos = move[0] * i % len(fileInput[i])

        if i % move[1] == 0:
            if i + move[1] <= len(fileInput):
                if fileInput[i][pos] == tree:
                    treesEncountered[j] += 1

print(treesEncountered)
print(reduce(lambda x,y: x*y, treesEncountered, 1))

    
    


