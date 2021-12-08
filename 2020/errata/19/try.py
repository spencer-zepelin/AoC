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

expression = ruleDict["0"]
while hasNumbers(expression):
    array = expression.split(" ")
    outArray = []
    for key in array:
        if key.isdigit():
            newVal = ruleDict[key]
            if "|" in newVal:
                newVal = "( " + newVal + " )"
            outArray.append(newVal)
        else:
            outArray.append(key)
    expression = " ".join(outArray)

# print(ruleDict)
inString = expression.replace(" ", "")


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


# validStrings = set(evaluate("0", ruleDict))
# print(validStrings)
print(type(inString))
validStrings, _ = evaluate(inString, len(inString))
validStrings = set(validStrings)
print(validStrings)
print(sum([1 if message in validStrings else 0 for message in messages]))


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
