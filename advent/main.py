fileObject = open("input.txt")
fileString = fileObject.read()
instructionList = fileString.splitlines()
registerX = 1
cycleCount = 0
ansList = []

def checkCycle():
    if (cycleCount-20)%40==0:
        ansList.append(registerX*cycleCount)

for item in instructionList:
    cycleCount += 1
    checkCycle()
    if item=="noop":
        continue
    else:
        val = item[5:]
        cycleCount += 1
        checkCycle()
        registerX += int(val)
print(ansList)