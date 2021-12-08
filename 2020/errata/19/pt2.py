with open("2020/19/in.txt") as file:
    ruleBlock, messageBlock = file.read().split("\n\n")


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


rules = ruleBlock.replace('"', "").split("\n")
messages = messageBlock.split("\n")
print(len(messages))

ruleDict = {}
for rule in rules:
    key, message = rule.split(": ")
    ruleDict[key] = message

expression1 = ruleDict["8"]
while hasNumbers(expression1):
    array = expression1.split(" ")
    outArray = []
    for key in array:
        if key.isdigit():
            newVal = ruleDict[key]
            if "|" in newVal:
                newVal = "( " + newVal + " )"
            outArray.append(newVal)
        else:
            outArray.append(key)
    expression1 = " ".join(outArray)

# print(ruleDict)
eightString = expression1.replace(" ", "")

expression2 = ruleDict["11"]
while hasNumbers(expression2):
    array = expression2.split(" ")
    outArray = []
    for key in array:
        if key.isdigit():
            newVal = ruleDict[key]
            if "|" in newVal:
                newVal = "( " + newVal + " )"
            outArray.append(newVal)
        else:
            outArray.append(key)
    expression2 = " ".join(outArray)
elevenString = expression2.replace(" ", "")

# a(a|b)


def evaluate(expression, totalChars):
    charsRead = 0
    validStrings = []
    onLeft = True
    leftHalf = [""]
    rightHalf = [""]
    while charsRead < totalChars:  # this doesn't work on recursive calls
        char = expression[charsRead]
        if char == "(":
            stringArray, advanced = evaluate(expression[charsRead + 1 :], totalChars)
            newValid = []
            if onLeft:
                for valid in leftHalf:
                    for newString in stringArray:
                        newValid.append(valid + newString)
                leftHalf = newValid
            else:
                for valid in rightHalf:
                    for newString in stringArray:
                        newValid.append(valid + newString)
                rightHalf = newValid
            charsRead += advanced
        elif char == ")":
            charsRead += 2
            return (leftHalf + rightHalf, charsRead)
        elif char in ["a", "b"]:
            if onLeft:
                leftHalf = [x + char for x in leftHalf]
            else:
                rightHalf = [x + char for x in rightHalf]
            charsRead += 1
        elif char == "|":
            onLeft = False
            charsRead += 1
    return (leftHalf + rightHalf, charsRead)


validEights, _ = evaluate(eightString, len(eightString))
validElevens, _ = evaluate(elevenString, len(elevenString))
validElevens = [x[8:] for x in validElevens]
validEights = set(validEights)
validElevens = set(validElevens)
print(validEights)
print(validElevens)
print("here")
validEightArray = set(map(len, validEights))
validElevenArray = set(map(len, validElevens))
print("here2")
messageLenArray = set(map(len, messages))
print("here3")
print(sorted(validEightArray), sorted(validElevenArray))
print(sorted(messageLenArray))
# print(min(validLenArray), max(validLenArray))
# print(min(messageLenArray), max(messageLenArray))


def valid(message, valid8, valid11):
    length = len(message)
    start = message[:8]
    start2 = message[8:16]
    end = message[-8:]
    remaining = message[16:-8]
    # eightCount = 0
    # elevenCount = 0
    numRemaining = len(remaining)
    if length == 24 and start in valid8 and start2 in valid8 and end in valid11:
        return True
    elif start in valid8 and start2 in valid8 and end in valid11:
        while numRemaining >= 8 and remaining[:8] in valid8:
            # eightCount += 1
            remaining = remaining[8:]
            numRemaining = len(remaining)
            if numRemaining >= 8 and remaining[-8:] in valid11:
                remaining = remaining[:-8]
                numRemaining = len(remaining)
        # while (
        #     numRemaining >= 8 and remaining[-8:] in valid11 and eightCount > elevenCount
        # ):
        #     elevenCount += 1
        #     remaining = remaining[:-8]
        #     numRemaining = len(remaining)
        if numRemaining == 0:
            return True
    return False


count = 0
for message in messages:
    if valid(message, validEights, validElevens):
        count += 1
print(count)

# 408 is too high
# total messages is 476

# print(validStrings)
# print(sum([1 if message in validStrings else 0 for message in messages]))


# def evaluate(expression, totalChars):
#     curr = -1
#     charsRead = 0
#     nextOp = None
#     while charsRead < totalChars:
#         char = expression[charsRead]
#         if char == "(":
#             value, advance = evaluate(expression[charsRead + 1 :], totalChars)
#             if curr == -1:
#                 curr = value
#             elif nextOp == "*":
#                 curr *= value
#             elif nextOp == "+":
#                 curr += value
#             charsRead += advance
#         elif char == ")":
#             charsRead += 2
#             return (curr, charsRead)
#         elif char == "*":
#             nextOp = "*"
#             charsRead += 1
#         elif char == "+":
#             nextOp = "+"
#             charsRead += 1
#         elif curr == -1:
#             curr = int(char)
#             charsRead += 1
#         else:
#             if nextOp == "*":
#                 curr *= int(char)
#             elif nextOp == "+":
#                 curr += int(char)
#                 # should reset nextOp, but assume valid input
#             charsRead += 1
#     return (curr, charsRead)
