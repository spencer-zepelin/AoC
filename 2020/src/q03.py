with open("2020/res/in03.txt") as file:
    rows = file.read().split("\n")

numRows, numCols = len(rows), len(rows[0])


def countTrees(rows, numRows, numCols, rdelt, cdelt):
    row, col = rdelt, cdelt
    trees = 0
    while row < numRows:
        if rows[row][col] == "#":
            trees += 1
        row += rdelt
        col = (col + cdelt) % numCols
    return trees


print("Part 1: ", countTrees(rows, numRows, numCols, 1, 3))

slopeArray = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
product = 1
for slope in slopeArray:
    product *= countTrees(rows, numRows, numCols, slope[0], slope[1])
print("Part 2: ", product)
