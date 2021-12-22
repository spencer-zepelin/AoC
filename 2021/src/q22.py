from itertools import combinations


def get_cube_size(inst):
    _, x_min, x_max, y_min, y_max, z_min, z_max = inst
    return (1 + x_max - x_min) * (1 + y_max - y_min) * (1 + z_max - z_min)


def overcount(ignore_ranges):
    range_count = len(ignore_ranges)
    offset = 0
    if range_count <= 1:
        return 0
    for i in range(2, range_count + 1):
        range_combos = combinations(ignore_ranges, i)
        sign = 1 if i % 2 == 0 else -1
        for range_combo in range_combos:
            overlap = check_multiple_overlap(range_combo)
            if overlap:
                offset += sign * get_cube_size(overlap)
    return offset


def check_overlap(inst1, inst2):
    _, x_min1, x_max1, y_min1, y_max1, z_min1, z_max1 = inst1
    _, x_min2, x_max2, y_min2, y_max2, z_min2, z_max2 = inst2

    # No dimension can have its range smaller than the smallest
    # or larger than the largest of the other cuboid in that dimension
    if (
        (x_min2 < x_min1 and x_max2 < x_min1)
        or (x_min2 > x_max1 and x_max2 > x_max1)
        or (y_min2 < y_min1 and y_max2 < y_min1)
        or (y_min2 > y_max1 and y_max2 > y_max1)
        or (z_min2 < z_min1 and z_max2 < z_min1)
        or (z_min2 > z_max1 and z_max2 > z_max1)
    ):
        return None
    x_min = max(x_min1, x_min2)
    x_max = min(x_max1, x_max2)
    y_min = max(y_min1, y_min2)
    y_max = min(y_max1, y_max2)
    z_min = max(z_min1, z_min2)
    z_max = min(z_max1, z_max2)
    return (_, x_min, x_max, y_min, y_max, z_min, z_max)


def check_multiple_overlap(ranges):
    overlap = ranges[0]
    for new_range in ranges[1:]:
        overlap = check_overlap(overlap, new_range)
        if not overlap:
            return None
    return overlap


with open("2021/res/in22.txt") as file:
    lines = file.read().split("\n")

insts = []
for line in lines:
    x_inst, y_inst, z_inst = line.split(",")
    op = x_inst.split(" ")[0]
    x_min, x_max = list(map(lambda x: int(x) + 50, x_inst.split("=")[1].split("..")))
    y_min, y_max = list(map(lambda x: int(x) + 50, y_inst.split("=")[1].split("..")))
    z_min, z_max = list(map(lambda x: int(x) + 50, z_inst.split("=")[1].split("..")))
    insts.append((op, x_min, x_max, y_min, y_max, z_min, z_max))

dim = 101
cube = [[[0 for col in range(dim)] for row in range(dim)] for layer in range(dim)]

for inst in insts[:20]:
    op, x_min, x_max, y_min, y_max, z_min, z_max = inst
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                val = 1 if op == "on" else 0
                cube[x][y][z] = val

pt1 = 0
for layer in cube:
    for row in layer:
        for val in row:
            pt1 += val


reverse_inst = insts.copy()
reverse_inst.reverse()

# iterating in reverse
# we build a list of exclusion zones
# and count any position not in an exclusion zone
# if the operation is "on"
pt2 = 0
insts_seen = []
for i, inst in enumerate(reverse_inst):
    if i % 20 == 0:
        print(f"executing instruction {i} of {len(reverse_inst)}")
    op, x_min, x_max, y_min, y_max, z_min, z_max = inst
    size = get_cube_size(inst)
    if op == "on":
        ignore_ranges = []
        for seen in insts_seen:
            overlap = check_overlap(inst, seen)
            if overlap:
                ignore_ranges.append(overlap)
        for i_range in ignore_ranges:
            size -= get_cube_size(i_range)
        size += overcount(ignore_ranges)
        pt2 += size

    insts_seen.append(inst)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
