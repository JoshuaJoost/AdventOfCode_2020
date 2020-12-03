fileInput = []

with open("02_input") as f:
    fileInput = list(map(str, f.readlines()))

def split(word):
    return [char for char in word]

validPasswords = 0
for input in fileInput:
    rule, password = input.split(":",1)
    numberOccurenciesRange, key = rule.split(" ",1)
    numberMinOccurencies, numberMaxOccurencies = list(map(int, numberOccurenciesRange.split("-",1)))
    
    passwordList = split(password.replace(" ","").replace("\n",""))

    # solution puzzle 1
    # keyOccurencies = 0
    # for char in passwordList:
    #     if char == key:
    #         keyOccurencies = keyOccurencies + 1
    
    # if keyOccurencies >= numberMinOccurencies and keyOccurencies <= numberMaxOccurencies:
    #     validPasswords = validPasswords + 1

    #solution puzzle 2
    releventKeyPosition1, releventKeyPosition2 = passwordList[numberMinOccurencies -1], passwordList[numberMaxOccurencies -1]
    
    if releventKeyPosition1 == key or releventKeyPosition2 == key:
        if releventKeyPosition1 != releventKeyPosition2:
            validPasswords = validPasswords + 1

print(validPasswords)
    
    

