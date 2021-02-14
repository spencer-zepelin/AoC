with open("2020/res/in17.txt") as file:
    rows = file.read().split("\n")

cycles = 6
numPlanes = 1 + (cycles * 2)
numDims = numPlanes
numRowsStart = len(rows)
numColsStart = len(rows[0])
numRows = numRowsStart + (cycles * 2)
numCols = numColsStart + (cycles * 2)

rows = [("0" * 6) + x.replace("#", "1").replace(".", "0") + ("0" * 6) for x in rows]


def validPos3(curr, central):
    i, j, k = curr
    return not (
        curr == central
        or i < 0
        or i >= numPlanes
        or j < 0
        or j >= numRows
        or k < 0
        or k >= numCols
    )


def nextVal3(space, pos):
    p, r, c = pos
    char = space[p][r][c]
    neighborSum = 0
    for i in range(p - 1, p + 2):
        for j in range(r - 1, r + 2):
            for k in range(c - 1, c + 2):
                if validPos3((i, j, k), pos) and space[i][j][k] == "1":
                    neighborSum += 1
    if char == "1":
        return "1" if neighborSum in [2, 3] else "0"
    else:
        return "1" if neighborSum == 3 else "0"


def cycle3(space):
    newSpace = []
    for p in range(numPlanes):
        newSpace.append([])
        for r in range(numRows):
            thisRow = ""
            for c in range(numCols):
                thisRow += nextVal3(space, (p, r, c))
            newSpace[p].append(thisRow)
    return newSpace


space3 = []
for i in range(numPlanes):
    space3.append([])
    for j in range(numRows):
        if i == cycles and j >= 6 and j < 14:
            space3[i].append(rows[j - 6])
        else:
            space3[i].append("0" * numCols)

for i in range(cycles):
    space3 = cycle3(space3)

activeCount3 = 0
for p in space3:
    for r in p:
        for c in r:
            if c == "1":
                activeCount3 += 1

print("Part 1: ", activeCount3)


#### PART 2 ####
def validPos4(curr, central):
    h, i, j, k = curr
    return not (
        curr == central
        or h < 0
        or h >= numDims
        or i < 0
        or i >= numPlanes
        or j < 0
        or j >= numRows
        or k < 0
        or k >= numCols
    )


def nextVal4(space, pos):
    d, p, r, c = pos
    char = space[d][p][r][c]
    neighborSum = 0
    for h in range(d - 1, d + 2):
        for i in range(p - 1, p + 2):
            for j in range(r - 1, r + 2):
                for k in range(c - 1, c + 2):
                    if validPos4((h, i, j, k), pos) and space[h][i][j][k] == "1":
                        neighborSum += 1
    if char == "1":
        return "1" if neighborSum in [2, 3] else "0"
    else:
        return "1" if neighborSum == 3 else "0"


def cycle4(space):
    newSpace = []
    for d in range(numDims):
        newSpace.append([])
        for p in range(numPlanes):
            newSpace[d].append([])
            for r in range(numRows):
                thisRow = ""
                for c in range(numCols):
                    thisRow += nextVal4(space, (d, p, r, c))
                newSpace[d][p].append(thisRow)
    return newSpace


space4 = []
for d in range(numDims):
    space4.append([])
    for i in range(numPlanes):
        space4[d].append([])
        for j in range(numRows):
            if d == cycles and i == cycles and j >= 6 and j < 14:
                space4[d][i].append(rows[j - 6])
            else:
                space4[d][i].append("0" * numCols)

for i in range(cycles):
    print(f"Calculating cycle {i + 1} of {cycles}")
    space4 = cycle4(space4)

activeCount4 = 0
for d in space4:
    for p in d:
        for r in p:
            for c in r:
                if c == "1":
                    activeCount4 += 1

print("Part 2: ", activeCount4)