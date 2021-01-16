with open("2020/11/in.txt") as file:
    rows = file.read().split("\n")

numC = len(rows[0])
numR = len(rows)


def seat(rows, part=1):
    out = ["" for x in rows]
    occupancy = 0
    stateChanged = False
    for rowIdx in range(numR):
        for colIdx in range(numC):
            curr = rows[rowIdx][colIdx]
            occ = (
                getOccupied(rows, rowIdx, colIdx)
                if part == 1
                else getVisible(rows, rowIdx, colIdx)
            )
            limit = 4 if part == 1 else 5
            if curr == "L" and occ == 0:
                occupancy += 1
                out[rowIdx] = out[rowIdx] + "#"
                stateChanged = True
            elif curr == "#" and occ >= limit:
                occupancy -= 1
                out[rowIdx] = out[rowIdx] + "L"
                stateChanged = True
            else:
                if curr == "#":
                    occupancy += 1
                out[rowIdx] = out[rowIdx] + curr
    return (stateChanged, occupancy, out)


def getOccupied(rows, row, col):
    occupied = 0
    up = True if row > 0 else False
    down = True if row < (numR - 1) else False
    left = True if col > 0 else False
    right = True if col < (numC - 1) else False
    if up and left and rows[row - 1][col - 1] == "#":
        occupied += 1
    if up and rows[row - 1][col] == "#":
        occupied += 1
    if up and right and rows[row - 1][col + 1] == "#":
        occupied += 1
    if left and rows[row][col - 1] == "#":
        occupied += 1
    if right and rows[row][col + 1] == "#":
        occupied += 1
    if down and left and rows[row + 1][col - 1] == "#":
        occupied += 1
    if down and rows[row + 1][col] == "#":
        occupied += 1
    if down and right and rows[row + 1][col + 1] == "#":
        occupied += 1
    return occupied


def getVisible(rows, row, col):
    occupied = 0
    delts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for delt in delts:
        rDelt, cDelt = delt
        r = row + rDelt
        c = col + cDelt
        found = False
        while valid(r, c) and not found:
            curr = rows[r][c]
            if curr == "L":
                found = True
            elif curr == "#":
                found = True
                occupied += 1
            else:
                r += rDelt
                c += cDelt
    return occupied


def valid(r, c):
    return True if r >= 0 and r < numR and c >= 0 and c < numC else False


occupancy = 0
stateChanged = True
p1rows = rows  # Necessary so we don't pollute input for pt 2
while stateChanged:
    stateChanged, occupancy, p1rows = seat(p1rows, part=1)

print("Part 1: ", occupancy)

occupancy = 0
stateChanged = True
while stateChanged:
    stateChanged, occupancy, rows = seat(rows, part=2)

print("Part 2: ", occupancy)
