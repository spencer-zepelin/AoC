with open("2020/res/in12.txt") as file:
    commands = file.read().split("\n")


def newCoord(drct, inc, row, col):
    for _ in range(inc):
        if drct == "L":
            row, col = ((col * -1), row)
        elif drct == "R":
            row, col = (col, (row * -1))
    return (row, col)


drctArray = [(0, 1), (1, 0), (0, -1), (-1, 0)]

row = 0
col = 0
drct = 0

wRow = -1
wCol = 10
row2 = 0
col2 = 0
drct2 = 0

for command in commands:
    ltr = command[0]
    val = int(command[1:])
    if ltr == "E":
        col += val
        wCol += val
    elif ltr == "W":
        col -= val
        wCol -= val
    elif ltr == "S":
        row += val
        wRow += val
    elif ltr == "N":
        row -= val
        wRow -= val
    elif ltr == "L":
        inc = int(val / 90)
        drct = (drct - inc) % 4
        wRow, wCol = newCoord("L", inc, wRow, wCol)
    elif ltr == "R":
        inc = int(val / 90)
        drct = (drct + inc) % 4
        wRow, wCol = newCoord("R", inc, wRow, wCol)
    elif ltr == "F":
        # Part 1 Forward
        rDelt, cDelt = drctArray[drct]
        row += rDelt * val
        col += cDelt * val
        # Part 2 Forward
        rDelt, cDelt = (wRow, wCol)
        row2 += rDelt * val
        col2 += cDelt * val

print("Part 1: ", abs(row) + abs(col))
print("Part 2: ", abs(row2) + abs(col2))
