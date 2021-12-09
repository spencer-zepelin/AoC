from collections import deque
from math import prod

with open("2021/res/in09.txt") as file:
    rows = file.read().split("\n")

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def is_valid(col_max, row_max, col, row):
    return col >= 0 and col < col_max and row >= 0 and row < row_max


def find_basin(topo, row, col):
    size = 0
    w = len(topo[1])
    h = len(topo)
    seen = set()
    q = deque([(row, col)])
    seen.add(f'{row}-{col}')
    while len(q) != 0:
        r, c = q.popleft()
        size += 1
        val = topo[r][c]
        for diff in [LEFT, RIGHT, UP, DOWN]:
            test_row = r + diff[0]
            test_col = c + diff[1]
            test_key = f'{test_row}-{test_col}'
            if is_valid(w, h, test_col, test_row) and topo[test_row][test_col] != 9 and val < topo[test_row][test_col] and test_key not in seen:
                seen.add(test_key)
                q.append((test_row, test_col))
    return size


w = len(rows[1])
h = len(rows)

topo = []
for row in rows:
    topo.append([int(val) for val in list(row)])

pt1 = 0
basins = []
for row in range(h):
    for col in range(w):
        val = topo[row][col]
        above = True if row == 0 else val < topo[row - 1][col]
        left = True if col == 0 else val < topo[row][col - 1]
        below = True if row == (h - 1) else val < topo[row + 1][col]
        right = True if col == (w - 1) else val < topo[row][col + 1]

        if above and left and below and right:
            pt1 += (val + 1)
            basin_size = find_basin(topo, row, col)
            basins.append(basin_size)

pt2 = prod(sorted(basins)[-3:])

print("Part 1: ", pt1)
print("Part 2: ", pt2)
