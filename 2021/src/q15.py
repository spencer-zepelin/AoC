def next_node(visited, scannable, curr_vals):
    smallest = None
    coords = None
    for row, col in scannable:
        val = curr_vals[row][col]
        if (row, col) not in visited and (not smallest or val < smallest):
            smallest = val
            coords = (row, col)
    return coords


def valid_coord(row, col, w, h):
    return row >= 0 and col >= 0 and row < h and col < w


def risk_level(val_grid):
    diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    w = len(val_grid[0])
    h = len(val_grid)
    dist_grid = [[-1 for col in range(w)] for row in range(h)]

    dist_grid[0][0] = 0
    visited = set()
    scannable = set([(0, 0)])
    print_chunk = w * h // 100
    while (h - 1, w - 1) not in visited:
        if len(visited) % print_chunk == 0:
            print(f"{len(visited) // print_chunk}% complete")
        row, col = next_node(visited, scannable, dist_grid)
        visited.add((row, col))
        scannable.discard((row, col))

        val = dist_grid[row][col]
        for diff in diffs:
            n_col = col + diff[1]
            n_row = row + diff[0]
            if valid_coord(n_row, n_col, w, h) and (
                dist_grid[n_row][n_col] == -1
                or val + val_grid[n_row][n_col] < dist_grid[n_row][n_col]
            ):
                dist_grid[n_row][n_col] = val + val_grid[n_row][n_col]
                scannable.add((n_row, n_col))

    return dist_grid[h - 1][w - 1]


with open("2021/res/in15.txt") as file:
    lines = file.read().split("\n")

val_grid1 = [list(map(int, line)) for line in lines]

# Stretch width 5x
long_lines = [5 * line for line in lines]
# Stretch height 5x
all_lines = []
for mult in range(5):
    all_lines += long_lines.copy()
val_grid2 = [list(map(int, line)) for line in all_lines]
# Increment according to rules
w = len(all_lines[0])
h = len(all_lines)
for row in range(h):
    for col in range(w):
        added = col // (w // 5) + row // (h // 5)
        new_val = val_grid2[row][col] + added
        while new_val > 9:
            new_val -= 9
        val_grid2[row][col] = new_val

pt1 = risk_level(val_grid1)
pt2 = risk_level(val_grid2)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
