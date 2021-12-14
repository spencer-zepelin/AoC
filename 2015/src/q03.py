with open("2015/res/in03.txt") as file:
    directions = file.read()

diffs = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, 1),
    'v': (0, -1)
}

x = 0
y = 0
sx = 0
sy = 0
rx = 0
ry = 0
visited = set([(x, y)])
visited2 = set([(sx, sy)])
for i, dir in enumerate(directions):
    x_delt, y_delt = diffs[dir]
    x += x_delt
    y += y_delt
    visited.add((x, y))
    if i % 2 == 0:
        sx += x_delt
        sy += y_delt
        visited2.add((sx, sy))
    else:
        rx += x_delt
        ry += y_delt
        visited2.add((rx, ry))

pt1 = len(visited)
pt2 = len(visited2)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
