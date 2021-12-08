from math import prod
import pprint

pp = pprint.PrettyPrinter(depth=6)
with open("2020/20/in.txt") as file:
    tiles = file.read().split("\n\n")


def reverseString(inString):
    return "".join(list(reversed(inString)))


def getEdges(tile):
    top = tile[0]
    right = "".join([x[-1] for x in tile])
    bottom = tile[-1]
    left = "".join([x[0] for x in tile])
    return (top, right, bottom, left)


def getEdgesHflip(tile):
    top = reverseString(tile[0])
    right = "".join([x[0] for x in tile])
    bottom = reverseString(tile[-1])
    left = "".join([x[-1] for x in tile])
    return (top, right, bottom, left)


def findMonsters(puzzle):
    count = 0
    for r in range(len(puzzle) - 2):
        for c in range(len(puzzle[0]) - 19):
            if (
                puzzle[r][c + 18] == "#"
                and puzzle[r + 1][c] == "#"
                and puzzle[r + 1][c + 5] == "#"
                and puzzle[r + 1][c + 6] == "#"
                and puzzle[r + 1][c + 11] == "#"
                and puzzle[r + 1][c + 12] == "#"
                and puzzle[r + 1][c + 17] == "#"
                and puzzle[r + 1][c + 18] == "#"
                and puzzle[r + 1][c + 19] == "#"
                and puzzle[r + 2][c + 1] == "#"
                and puzzle[r + 2][c + 4] == "#"
                and puzzle[r + 2][c + 7] == "#"
                and puzzle[r + 2][c + 10] == "#"
                and puzzle[r + 2][c + 13] == "#"
                and puzzle[r + 2][c + 16] == "#"
            ):
                count += 1
    return count


def rotate(edges, shift):
    top, right, bottom, left = edges
    for i in range(shift):
        nt = reverseString(left)
        nr = top
        nb = reverseString(right)
        nl = bottom
        top, right, bottom, left = nt, nr, nb, nl
    return (top, right, bottom, left)


def stripTile(tile):
    rows = tile[1:-1]
    return [x[1:-1] for x in rows]


def flipTile(tile):
    return [reverseString(row) for row in tile]


def rotateTile(tile, turns):
    curr = tile
    for _ in range(turns):
        out = []
        dim = len(tile)
        for col in range(dim):
            out.append(reverseString("".join([curr[row][col] for row in range(dim)])))
        curr = out
    return curr


def processTile(tile, conf, turns):
    out = stripTile(tile)
    if conf == "hFlip":
        out = flipTile(out)
    return rotateTile(out, turns)


# def getEdgesVflip(tile):
#     top = tile[-1]
#     right = reverseString("".join([x[-1] for x in tile]))
#     bottom = tile[0]
#     left = reverseString("".join([x[0] for x in tile]))
#     return (top, right, bottom, left)


def buildTileObject(rows):
    tile = {}
    tile["base"] = getEdges(rows)
    tile["hFlip"] = getEdgesHflip(rows)
    # tile["vFlip"] = getEdgesVflip(rows)
    tile["rows"] = rows
    return tile


numTiles = len(tiles)
dim = 12
flips = ["base", "hFlip"]
cornerIds = ["1609", "2621", "1123", "3253"]  # currently hardcoded from pt 1

edgeDict = {}
tileDict = {}
for tile in tiles:
    num, *rows = tile.split("\n")  ## All tiles have four digit ids
    tNum = num[5:9]
    tileDict[tNum] = buildTileObject(rows)
    for edge in getEdges(rows):
        rEdge = reverseString(edge)
        if edge in edgeDict:
            edgeDict[edge].append(tNum)
            if len(edgeDict[edge]) > 2:
                print("warning!!!")
        else:
            edgeDict[edge] = [tNum]
        if rEdge in edgeDict:
            edgeDict[rEdge].append(tNum)
            if len(edgeDict[rEdge]) > 2:
                print("warning!!!")
        else:
            edgeDict[rEdge] = [tNum]

# print(tileDict)

ordering = [[] for x in range(dim)]

print(ordering)

puzzle = {}
row = col = 0
currId = cornerIds[0]
currTile = tileDict[currId]
# while row < dim:
for conformation in flips:
    cEdges = currTile[conformation]
    for i in range(4):
        etop, eright, ebottom, eleft = rotate(cEdges, i)
        if (
            len(edgeDict[eright]) == 2
            and len(edgeDict[ebottom]) == 2
            and len(edgeDict[eleft]) == 1
            and len(edgeDict[etop]) == 1
        ):
            top = right = bottom = left = "border"
            for tileId in edgeDict[eright]:
                if tileId != currId:
                    right = tileId
            if col < 11:
                for tileId in edgeDict[ebottom]:
                    if tileId != currId:
                        bottom = tileId
            puzzle[(row, col)] = {
                "id": currId,
                "topId": top,
                "rightId": right,
                "bottomId": bottom,
                "leftId": left,
                "conf": conformation,
                "r": i,
                "top": etop,
                "right": eright,
                "bottom": ebottom,
                "left": eleft,
            }
        # print(cornerIds[0], conformation, i)
        # print(edgeDict[edge], edgeDict[cEdges[bIdx]])
        ## DOUBLE BREAK
if col < 11:
    currId = puzzle[(row, col)]["rightId"]
    currTile = tileDict[currId]
    col += 1
else:
    col = 0
    row += 1
    if row < 12:
        currId = puzzle[(row - 1, col)]["bottomId"]
        currTile = tileDict[currId]


pp.pprint(puzzle)


while row < dim:
    # print(row, col)
    # print(currId)
    # # print(currTile)
    leftEdge = topEdge = None
    if row != 0:
        topEdge = puzzle[(row - 1, col)]["bottom"]
    if col != 0:
        leftEdge = puzzle[(row, col - 1)]["right"]
    print(topEdge, leftEdge)
    for conformation in flips:
        cEdges = currTile[conformation]
        for i in range(4):
            etop, eright, ebottom, eleft = rotate(cEdges, i)
            if topEdge and etop != topEdge:
                print("shouldnt see this!")
                continue
            if leftEdge and eleft != leftEdge:
                print("no left match: ", conformation, i)
                continue
            if col < 11 and len(edgeDict[eright]) != 2:
                print(currId)
                print(currTile)
                print("no right match: ", conformation, i)
                continue
            if row < 11 and len(edgeDict[ebottom]) != 2:
                print("shouldn't see this222222!")
                continue
            top = right = bottom = left = "border"
            if topEdge:
                top = puzzle[(row - 1, col)]["id"]
            if leftEdge:
                left = puzzle[(row, col - 1)]["id"]
            for tileId in edgeDict[eright]:
                if tileId != currId:
                    right = tileId
            if col < 11:
                for tileId in edgeDict[ebottom]:
                    if tileId != currId:
                        bottom = tileId
            puzzle[(row, col)] = {
                "id": currId,
                "topId": top,
                "rightId": right,
                "bottomId": bottom,
                "leftId": left,
                "conf": conformation,
                "r": i,
                "top": etop,
                "right": eright,
                "bottom": ebottom,
                "left": eleft,
            }
            # found = True
            # print(cornerIds[0], conformation, i)
            # print(edgeDict[edge], edgeDict[cEdges[bIdx]])
            ## DOUBLE BREAK
    # print(puzzle)
    if col < 11:
        currId = puzzle[(row, col)]["rightId"]
        currTile = tileDict[currId]
        col += 1
    else:
        col = 0
        row += 1
        if row < 12:
            currId = puzzle[(row - 1, col)]["bottomId"]
            currTile = tileDict[currId]

# print(puzzle)
print(len(list(puzzle.keys())))
pp.pprint(puzzle[(0, 0)])
# for k, v in edgeDict.items():
#     if "3833" in v:
#         print(k, v)
# print(tileDict["3833"]["base"])
# print(tileDict["3709"]["base"])

# print(puzzle.keys())
# print(edgeDict)

# corners = []
# for tile in tiles:
#     num, *rows = tile.split("\n")  ## All tiles have four digit ids
#     tNum = num[5:9]
#     # print(tNum)
#     forwardEdges = getEdges(rows)
#     backwardEdges = [reverseString(x) for x in forwardEdges]
#     fCount = bCount = 4
#     for edge in forwardEdges:
#         if edgeDict[edge] == 1:
#             fCount -= 1
#     for edge in backwardEdges:
#         if edgeDict[edge] == 1:
#             bCount -= 1
#     if bCount <= 2 or fCount <= 2:
#         corners.append(int(tNum))
#         print(tNum, bCount, fCount)
# print(prod(corners))
tile = ["123", "456", "789"]
tile = flipTile(tile)
for i in range(4):
    print(f"------{i} rotation-----")
    for row in rotateTile(tile, i):
        print(row)

finalDim = 96
finalPuzzle = ["" for _ in range(finalDim)]

for row in range(dim):
    for col in range(dim):
        piece = puzzle[(row, col)]
        # print(piece)
        pId = piece["id"]
        conf = piece["conf"]
        r = piece["r"]
        # print(pId, conf, r)
        tile = tileDict[pId]["rows"]
        # print(tile)
        tile = processTile(tile, conf, r)
        for i, currRow in enumerate(tile):
            rowNum = (row * 8) + i
            finalPuzzle[rowNum] = finalPuzzle[rowNum] + currRow

if len(finalPuzzle) == 96:
    print("yaayyyyy!")

hashCount = 0
for row in finalPuzzle:
    for char in row:
        if char == "#":
            hashCount += 1

print(hashCount)

monsterCount = 0
for puzzle in [finalPuzzle, flipTile(finalPuzzle)]:
    for i in range(4):
        monsters = findMonsters(rotateTile(puzzle, i))
        if monsters > 0:
            monsterCount = monsters

print(hashCount - (monsterCount * 15))
