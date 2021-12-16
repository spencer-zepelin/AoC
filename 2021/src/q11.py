with open("2021/res/in11.txt") as file:
    lines = file.read().split("\n")

DIM = 10
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


class octo:
    def __init__(self, val):
        self.energy = val
        self.flashed = False


def valid_pos(row, col):
    return row >= 0 and row < DIM and col >= 0 and col < DIM


def flash(grid, row, col):
    new_flash = False
    for delta in deltas:
        adj_row = row + delta[0]
        adj_col = col + delta[1]
        if (
            valid_pos(adj_row, adj_col)
            and not grid[adj_row][adj_col].flashed
            and grid[adj_row][adj_col].energy < 10
        ):
            grid[adj_row][adj_col].energy += 1
            if grid[adj_row][adj_col].energy == 10:
                new_flash = True
    return new_flash


def all_flashed(grid):
    all_flashed = True
    for row in grid:
        for o in row:
            if not o.flashed:
                all_flashed = False
    return all_flashed


grid = []
for row in range(DIM):
    temp = []
    for col in range(DIM):
        temp.append(octo(int(lines[row][col])))
    grid.append(temp)

pt1 = 0
pt2 = 0
step = 0
pt2_found = False
while not pt2_found or step < 100:
    new_flashes = False
    # Increment all
    for row in range(DIM):
        for col in range(DIM):
            o = grid[row][col]
            o.energy += 1
            if o.energy == 10:
                new_flashes = True
    # Flash chain
    while new_flashes:
        new_flashes = False
        for row in range(DIM):
            for col in range(DIM):
                o = grid[row][col]
                if o.energy >= 10:
                    new_flash = flash(grid, row, col)
                    if step < 100:
                        pt1 += 1
                    o.energy = 0
                    o.flashed = True
                    if new_flash:
                        new_flashes = True
    # Check for condition 2
    if not pt2_found and all_flashed(grid):
        pt2 = step + 1
        pt2_found = True
    # Create grid for next step
    new_grid = []
    for row in range(DIM):
        temp = []
        for col in range(DIM):
            temp.append(octo(int(grid[row][col].energy)))
        new_grid.append(temp)
    grid = new_grid
    step += 1

print("Part 1: ", pt1)
print("Part 2: ", pt2)
