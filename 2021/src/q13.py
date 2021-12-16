def y_fold(grid, fold_val):
    top = grid[:fold_val]
    bottom = grid[(fold_val + 1) :]

    for i, row in enumerate(bottom):
        for j, col in enumerate(row):
            top_row = -i - 1
            bottom_val = bottom[i][j]
            top_val = top[top_row][j]
            top[top_row][j] = top_val or bottom_val
    return top


def x_fold(grid, fold_val):
    left = []
    right = []
    for row in grid:
        left.append(row[:fold_val])
        right.append(row[(fold_val + 1) :])

    for i, row in enumerate(right):
        for j, col in enumerate(row):
            left_col = -j - 1
            right_val = right[i][j]
            left_val = left[i][left_col]
            left[i][left_col] = left_val or right_val
    return left


with open("2021/res/in13.txt") as file:
    coord_block, instruction_block = file.read().split("\n\n")

coords = [
    (int(str_coord.split(",")[1]), int(str_coord.split(",")[0]))
    for str_coord in coord_block.split("\n")
]

instructions = [
    (inst.split(" ")[-1].split("=")[0], int(inst.split(" ")[-1].split("=")[1]))
    for inst in instruction_block.split("\n")
]

width = max(col + 1 for _, col in coords)
height = max(row + 1 for row, _ in coords)

grid = [[0 for _col in range(width)] for _row in range(height)]

for row, col in coords:
    grid[row][col] = 1

pt1 = False
for fold_type, fold_val in instructions:
    if fold_type == "x":
        grid = x_fold(grid, fold_val)
    else:
        grid = y_fold(grid, fold_val)
    if not pt1:
        pt1 = sum(sum(row) for row in grid)

for row in grid:
    chars = ["#" if val else "." for val in row]
    print("".join(chars))

print("Part 1: ", pt1)
print("Part 2: BLKJRBAG")  # Answer hardcoded from visual examination
