from math import prod

with open("2020/20/in.txt") as file:
    tiles = file.read().split("\n\n")


def getEdges(tile):
    left = "".join([x[0] for x in tile])
    right = "".join([x[-1] for x in tile])
    return (tile[0], tile[-1], left, right)


def reverseString(inString):
    return "".join(list(reversed(inString)))


print(len(tiles), "tiles")

edgeDict = {}
tileArray = []
cornerArray = []
for tile in tiles:
    num, *rows = tile.split("\n")  ## All tiles have four digit ids
    tNum = num[5:9]
    # print(tNum)
    matchCount = 0
    for edge in getEdges(rows):
        matchFound = False
        rEdge = reverseString(edge)
        if edge in edgeDict:
            edgeDict[edge] += 1
            if edgeDict[edge] > 2:
                print("WARNING!!!")
            matchFound = True
        else:
            edgeDict[edge] = 1
        if rEdge in edgeDict:
            edgeDict[rEdge] += 1
            matchFound = True
            if edgeDict[rEdge] > 2:
                print("WARNING!!!")
        else:
            edgeDict[rEdge] = 1
        if matchFound:
            matchCount += 1

corners = []
for tile in tiles:
    num, *rows = tile.split("\n")  ## All tiles have four digit ids
    tNum = num[5:9]
    # print(tNum)
    forwardEdges = getEdges(rows)
    backwardEdges = [reverseString(x) for x in forwardEdges]
    fCount = bCount = 4
    for edge in forwardEdges:
        if edgeDict[edge] == 1:
            fCount -= 1
    for edge in backwardEdges:
        if edgeDict[edge] == 1:
            bCount -= 1
    if bCount <= 2 or fCount <= 2:
        corners.append(int(tNum))
        print(tNum, bCount, fCount)
print(prod(corners))
