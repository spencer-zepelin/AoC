from collections import defaultdict

with open("2022/res/in15.txt") as file:
    rows = file.read().split("\n")

sensors = []
beacons = set()
for row in rows:
    s_string, b_string = row.split(": closest beacon is at x=")
    sx_string, sy_string = s_string.split(", y=")
    sy = int(sy_string)
    sx = int(sx_string.split("=")[1])
    bx_string, by_string = b_string.split(", y=")
    by = int(by_string)
    bx = int(bx_string)
    dist = abs(sy - by) + abs(sx - bx)
    sensors.append((sx, sy, dist))
    beacons.add((bx, by))


def count_covered_on_row(sensors, beacons, row):
    covered = set()
    for sx, sy, dist in sensors:
        y_dist = abs(sy - row)
        dist_delt = dist - y_dist
        if dist_delt >= 0:
            for i in range(0, dist_delt + 1):
                for loc in [(sx + i, row), (sx - i, row)]:
                    if loc not in beacons:
                        covered.add(loc)
    return len(covered)


def build_row_intervals(sensors, dim):
    memo = defaultdict(list)
    for sx, sy, dist in sensors:
        for x_delt in range(0, dist + 1):
            y_range = dist - x_delt
            low_y, high_y = sy - y_range, sy + y_range
            low_x, high_x = sx - x_delt, sx + x_delt

            valid_rows = filter(lambda y: 0 <= y <= dim, [low_y, high_y])
            valid_x_range = (
                0 <= low_x <= dim or 0 <= high_x <= dim or (low_x < 0 and high_x > dim)
            )

            if valid_x_range:
                if low_x < 0:
                    low_x = 0
                if high_x > dim:
                    high_x = dim
                for row in valid_rows:
                    memo[row].append([low_x, high_x])
    return memo


def find_frequency(interval_map, dim, x_multiple):
    for y in range(dim + 1):
        interval_map[y].sort(key=lambda x: x[0])
        row_intervals = interval_map[y]

        merged = []
        merged.append(row_intervals[0])
        for interval in row_intervals[1:]:
            curr_low, curr_high = merged[-1]
            int_low, int_high = interval

            # discrete values mean adjacent is continuous
            if curr_low <= int_low <= curr_high + 1:
                merged[-1][-1] = max(curr_high, int_high)
            else:
                return (merged[-1][-1] + 1) * x_multiple + y


ROW = 2_000_000
pt1 = count_covered_on_row(sensors, beacons, ROW)

DIM = 4_000_000
X_MULT = 4_000_000
intervals_by_row = build_row_intervals(sensors, DIM)
pt2 = find_frequency(intervals_by_row, DIM, X_MULT)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
