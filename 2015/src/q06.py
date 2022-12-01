with open("2015/res/in06.txt") as file:
    instructions = file.read().split("\n")


def parse_inst(instruction):
    begin, point2 = instruction.split(" through ")

    op_and_point1 = begin.split(" ")
    if op_and_point1[0] == "toggle":
        op = op_and_point1[0]
    else:
        op = op_and_point1[1]

    point1 = op_and_point1[-1]
    x1, y1 = list(map(int, point1.split(",")))
    x2, y2 = list(map(int, point2.split(",")))
    x_min = min([x1, x2])
    x_max = max([x1, x2]) + 1
    y_min = min([y1, y2])
    y_max = max([y1, y2]) + 1

    return op, x_min, x_max, y_min, y_max


def grid_sum(grid):
    total = 0
    for row in grid:
        total += sum(row)
    return total


grid = [[0 for col in range(1000)] for row in range(1000)]
grid2 = [[0 for col in range(1000)] for row in range(1000)]

for inst in instructions:
    op, x_min, x_max, y_min, y_max = parse_inst(inst)
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            if op == "on":
                grid[x][y] = 1
                grid2[x][y] += 1
            elif op == "off":
                grid[x][y] = 0
                new = grid2[x][y] - 1
                grid2[x][y] = new if new >= 0 else 0
            else:
                grid[x][y] = 0 if grid[x][y] == 1 else 1
                grid2[x][y] += 2

pt1 = grid_sum(grid)
pt2 = grid_sum(grid2)
print("Part 1: ", pt1)
print("Part 2: ", pt2)
