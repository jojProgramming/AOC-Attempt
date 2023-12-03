
numbers = ['0','1','2','3','4','5','6','7','8','9']
total = 0

puzzleInput = (open("values.txt").read().split("\n"))
puzzleInput.append("...")

def getSum(current): # GET THE SUM OF THE CHARS.
    running = 0
    a = 0
    while a < len(current):
        if current[a] not in numbers and a == 0:
            current = current[a:]
        elif current[a] not in numbers and a == len(current):
            current = current[:a]
        elif current[a] not in numbers:
            tempList = current.split(current[a])
            
            return getSum(tempList[0])+getSum(tempList[1])
        a += 1
    length = len(current)
    for a in range(length):
        if current[a] in numbers:
            running += int(current[a]) * (10**(length-int(a)-1))
    return running


def isApproved(working, indexLower = 0, indexHigher = -1): # CHECK IF IT SHOULD BE APPROVED
    if indexHigher == -1:
        indexHigher = len(working)
    working = working[indexLower :indexHigher + 1]
    for x in range(len(working)):
            currentChar = working[x]
            if currentChar not in numbers and currentChar != '.':
                return True
    return False

for i in range(len(puzzleInput)-1): # Read in each string
    if i != 0:
        aboveInput = puzzleInput[i - 1]
    else:
        aboveInput = "......................................................................................................................................................................"
        
    currentInput = puzzleInput[i]
    belowInput = puzzleInput[i + 1]
    
    currentSet = currentInput.split('.')
    for j in range(len(currentSet)):
        appendage = str()
        currentApproved = False
        currentPart = currentSet[j]

        currentApproved = isApproved(currentPart)
        #for x in range(len(currentPart)):
         #   currentChar = currentPart[x]
          #  if currentChar not in numbers and currentChar != '.':
           #     currentApproved = True

        if currentApproved == False:
            #print(currentPart)
            #if currentPart == "":
             #   print("NODATA")
            lowerI = currentInput.find("."+currentPart+".")
            if lowerI == -1:
                lowerI = currentInput.find("."+currentPart)
                if lowerI == -1:
                    lowerI = currentInput.find(currentPart+".")
            
            #print(lowerI)
            higherI = lowerI + len(currentPart) + 2
            if lowerI != -1:
                currentApproved = isApproved(aboveInput,lowerI,higherI -1)
                if currentApproved == False:
                    #print(currentPart, "LOWER CHECKIN")
                    currentApproved = isApproved(belowInput,lowerI,higherI -1)
        if currentApproved == True:
            #print("The following value is marked as true: ", currentPart)
            total += getSum(currentPart)
        for y in range(len(currentPart)):
                appendage = appendage + "0"
                #print(appendage)
        alpha = currentInput.find("."+currentPart+".")
        currentInput = currentInput[:alpha] + appendage + currentInput[(alpha+len(currentPart)):]

input(total)
    #print(currentSet)
