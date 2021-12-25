def step(grid):
    movement = False
    h = len(grid)
    w = len(grid[0])

    # right moves
    middle = []
    for row in range(h):
        new_row = ""
        for col in range(w):
            curr = grid[row][col]
            left_col = (col - 1) % w
            right_col = (col + 1) % w
            left = grid[row][left_col]
            right = grid[row][right_col]
            if curr == "." and left == ">":
                new_row += ">"
                movement = True
            elif curr == ">" and right == ".":
                new_row += "."
                movement = True
            else:
                new_row += curr
        middle.append(new_row)

    # down moves
    out = []
    for row in range(h):
        new_row = ""
        for col in range(w):
            curr = middle[row][col]
            above_row = (row - 1) % h
            below_row = (row + 1) % h
            above = middle[above_row][col]
            below = middle[below_row][col]
            if curr == "." and above == "v":
                new_row += "v"
                movement = True
            elif curr == "v" and below == ".":
                new_row += "."
                movement = True
            else:
                new_row += curr
        out.append(new_row)

    return out, movement


with open("2021/res/in25.txt") as file:
    grid = file.read().split("\n")

pt1 = 0
movement = True
while movement:
    grid, movement = step(grid)
    pt1 += 1

print("Part 1: ", pt1)
print("Part 2:  N/A")
