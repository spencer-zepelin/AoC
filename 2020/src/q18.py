with open("2020/res/in18.txt") as file:
    problems = file.read().split("\n")

problems = (x.replace(" ", "") for x in problems)


def evaluate(expression, totalChars):
    curr = -1
    charsRead = 0
    nextOp = None
    while charsRead < totalChars:
        char = expression[charsRead]
        if char == "(":
            value, advance = evaluate(expression[charsRead + 1 :], totalChars)
            if curr == -1:
                curr = value
            elif nextOp == "*":
                curr *= value
            elif nextOp == "+":
                curr += value
            charsRead += advance
        elif char == ")":
            charsRead += 2
            return (curr, charsRead)
        elif char == "*":
            nextOp = "*"
            charsRead += 1
        elif char == "+":
            nextOp = "+"
            charsRead += 1
        elif curr == -1:
            curr = int(char)
            charsRead += 1
        else:
            if nextOp == "*":
                curr *= int(char)
            elif nextOp == "+":
                curr += int(char)
                # should reset nextOp, but assume valid input
            charsRead += 1
    return (curr, charsRead)


def parse(inString):
    expression = inString
    while "(" in expression:
        foundFirst = False
        remaining = 0
        start = end = None
        for i, char in enumerate(expression):
            if char == "(":
                if not foundFirst:
                    foundFirst = True
                    start = i
                remaining += 1
            elif char == ")":
                if remaining == 1:
                    end = i
                    break
                remaining -= 1
        first = expression[:start]
        middle = expression[start + 1 : end]
        last = expression[end + 1 :]
        expression = first + str(parse(middle)) + last
    sumChains = expression.split("*")
    sums = [sum(map(int, x.split("+"))) for x in sumChains]
    product = 1
    for oneSum in sums:
        product *= oneSum
    return product


total1 = 0
total2 = 0
for problem in problems:
    val1, _ = evaluate(problem, len(problem))
    total1 += val1
    total2 += parse(problem)

print("Part 1: ", total1)
print("Part 2: ", total2)
