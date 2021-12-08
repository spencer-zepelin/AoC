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
    # print(key, message)
    options = message.split(" | ")
    # print(options)
    valid = [x.split(" ") for x in options]
    # print(valid)
    ruleDict[key] = valid

# print(ruleDict)

memo = {}


def evaluate(ruleKey, ruleDict):
    global memo
    if ruleKey in memo:
        return memo[ruleKey]
    currentRule = ruleDict[ruleKey]
    stringArray = []
    for oneSide in currentRule:
        # if len(oneSide) > 2:
        #     print("AHHHHHHHHHHHHHHHH", ruleKey)
        stringHalves = []
        for value in oneSide:
            if value in ["a", "b"]:
                # DO SOMETHING
                stringHalves.append([value])
            else:
                stringHalves.append(evaluate(value, ruleDict))

        if len(stringHalves) > 1:
            for half in stringHalves[0]:
                for otherHalf in stringHalves[1]:
                    stringArray.append(half + otherHalf)
        else:
            stringArray = stringHalves[0]
    memo[ruleKey] = stringArray
    return stringArray


validStrings = set(evaluate("0", ruleDict))

# print(validStrings)
# print(validStrings)

print(sum([1 if message in validStrings else 0 for message in messages]))

# ruleDict = {}
# for rule in rules:
#     key, message = rule.split(": ")
#     print(key, message)
#     # options = message.split(" | ")
#     # print(options)
#     valid = message.split(" ") if message not in ["a", "b"] else message
#     # print(valid)
#     ruleDict[key] = valid

# print(ruleDict)

# final = "".join(ruleDict["0"])
# print(final)

# curr = [ruleDict["0"]]


# def evaluate(curr, ruleDict):
#     stringArray = []
#     if "|" in curr:
#         stringArray = evaluate(curr[:2], ruleDict) + evaluate(curr[-2:], ruleDict)
#     for val in curr:
#         if val not in ["a", "b"]:
#             stringArray += evaluate(ruleDict[val], ruleDict)
#     return stringArray


# while any([hasNumbers("".join(x)) for x in curr]):
#     news = []
#     for array in curr:
#         if hasNumbers(array):

#             for val in curr:
#                 if val not in ["a", "b"]:
#                     lookup = ruleDict[val]
#                     if "|" in lookup:
#                         frontHalf = [x + lookup[:2] for x in news]
#                         backHalf = [x + lookup[-2:] for x in news]
#                         news = frontHalf + backHalf
#                     else:
#                         news = [x + lookup for x in news]
#                 else:
#                     news = [x.append(val) for x in news]

#     curr = new

# print(curr)

#### stringier method
# for rule in rules:
#     key, message = rule.split(": ")
#     # print(key, message)
#     options = message.replace(" | ", "|").replace(" ", "-").split("|")
#     # print(options)
#     ruleDict[key] = options

# print(ruleDict)


# # print(ruleDict)

# validStrings = set()

# curr = ruleDict["0"]


# for expression in ruleDict["0"][0]


# def evaluate(curr, ruleDict):
#     out = []
#     for option in curr:  # either side of the OR
#         vals = []
#         for value in option:
#             if value in ["a", "b"]:
#                 vals.append(value)
#             else:
#                 vals.append

#         out.append(vals)


# initial = ruleDict["0"][0]
# new = [ruleDict[x] for x in initial]
# print(initial)
# print(new)
