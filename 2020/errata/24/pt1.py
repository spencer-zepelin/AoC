with open("2020/24/in.txt") as file:
    rawDirs = file.read().split("\n")


def parseDir(rawDir):
    length = len(rawDir)
    ctr = 0
    out = []
    curr = ""
    while ctr < length:
        if rawDir[ctr] in ["e", "w"]:
            curr += rawDir[ctr]
            out.append(curr)
            curr = ""
        else:
            curr += rawDir[ctr]
        ctr += 1
    return out


dirs = [parseDir(d) for d in rawDirs]

bTiles = set()
for d in dirs:
    row = col = 0
    for step in d:
        if step == "w":
            col -= 2
        elif step == "e":
            col += 2
        elif step == "nw":
            row += 1
            col -= 1
        elif step == "ne":
            row += 1
            col += 1
        elif step == "sw":
            row -= 1
            col -= 1
        elif step == "se":
            row -= 1
            col += 1
    if (row, col) in bTiles:
        bTiles.remove((row, col))
    else:
        bTiles.add((row, col))

print(len(bTiles))


def day(bSet):
    outSet = set()
    whiteMemo = {}
    for tile in bSet:
        row, col = tile
        total = 0
        neighbors = [
            (row, col - 2),
            (row, col + 2),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
        ]
        for n in neighbors:
            if n in bSet:
                total += 1
            else:
                whiteMemo[n] = whiteMemo.get(n, 0) + 1
        if total in [1, 2]:
            outSet.add(tile)
    for tile, bCount in whiteMemo.items():
        if bCount == 2:
            outSet.add(tile)
    return outSet


for i in range(100):
    if i % 10 == 0:
        print(i)
    bTiles = day(bTiles)

print(len(bTiles))
