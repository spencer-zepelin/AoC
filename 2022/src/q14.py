from copy import deepcopy

with open("2022/res/in14.txt") as file:
    paths = file.read().split("\n")

y_max = 0
topo = set()
for path in paths:
    points = [tuple(map(int, point.split(","))) for point in path.split(" -> ")]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                topo.add((x, y))
                if y > y_max:
                    y_max = y
topo2 = deepcopy(topo)


def tumble(topo, x, y):
    sx = x
    sy = y + 1
    if (sx, sy) not in topo:
        return (sx, sy)
    elif (sx - 1, sy) not in topo:
        return (sx - 1, sy)
    elif (sx + 1, sy) not in topo:
        return (sx + 1, sy)


def pour_sand(topo, max_y):
    sx = 500
    sy = 0
    while (
        (sx, sy + 1) not in topo
        or (sx - 1, sy + 1) not in topo
        or (sx + 1, sy + 1) not in topo
    ):
        sx, sy = tumble(topo, sx, sy)
        if sy == max_y:
            return False
    topo.add((sx, sy))
    return True


def pour_sand_floor(topo, max_y):
    sx = 500
    sy = 0
    if (sx, sy) in topo:
        return False
    while (
        (sx, sy + 1) not in topo
        or (sx - 1, sy + 1) not in topo
        or (sx + 1, sy + 1) not in topo
    ) and sy + 1 < max_y + 2:
        sx, sy = tumble(topo, sx, sy)
    topo.add((sx, sy))
    return True


pt1 = 0
while pour_sand(topo, y_max):
    pt1 += 1
pt2 = 0
while pour_sand_floor(topo2, y_max):
    pt2 += 1
print("Part 1: ", pt1)
print("Part 2: ", pt2)
