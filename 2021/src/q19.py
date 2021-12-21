from collections import deque


# Algorithm is sound but painfully slow
class Scanner:
    def __init__(self, scanner_id, beacon_list, fixed=False, pos=(0, 0, 0)):
        self.scanner_id = scanner_id
        self.beacon_list = beacon_list
        self.pos = pos
        self.fixed = fixed

    def __str__(self):
        return f"ID: {self.scanner_id}\nFixed: {self.fixed}\nPOS: {self.pos}"

    def rotate_scanner(self, facing, turns):
        new_beacon_list = []
        for beacon in self.beacon_list:
            new_beacon_list.append(rotate(beacon, facing, turns))
        return Scanner(self.scanner_id, new_beacon_list)


def rotate(initials, facing, turns):
    x, y, z = initials
    if facing == "x":
        x1, y1, z1 = x, y, z
    elif facing == "-x":
        x1, y1, z1 = -x, -y, z
    elif facing == "y":
        x1, y1, z1 = y, -x, z
    elif facing == "-y":
        x1, y1, z1 = -y, x, z
    elif facing == "z":
        x1, y1, z1 = z, y, -x
    elif facing == "-z":
        x1, y1, z1 = -z, y, x
    for _turn in range(turns):
        y1, z1 = -z1, y1
    return (x1, y1, z1)


def all_rotations(initials):
    x, y, z = initials
    every = []
    for facing in ["x", "-x", "y", "-y", "z", "-z"]:
        if facing == "x":
            x1, y1, z1 = x, y, z
        elif facing == "-x":
            x1, y1, z1 = -x, -y, z
        elif facing == "y":
            x1, y1, z1 = y, -x, z
        elif facing == "-y":
            x1, y1, z1 = -y, x, z
        elif facing == "z":
            x1, y1, z1 = z, y, -x
        elif facing == "-z":
            x1, y1, z1 = -z, y, x
        for _turn in range(4):
            y1, z1 = -z1, y1
            coords = (x1, y1, z1)
            every.append(coords)
            print(coords)
    return every


def match_scanners(fixed_scanner, unfixed_scanner):
    f1x, f1y, f1z = fixed_scanner.pos
    # all possible conformations for unfixed
    for facing in ["x", "-x", "y", "-y", "z", "-z"]:
        for turns in range(4):
            candidate = unfixed_scanner.rotate_scanner(facing, turns)
            for beacon1 in fixed_scanner.beacon_list:
                for beacon2 in candidate.beacon_list:
                    x_rel, y_rel, z_rel = (
                        beacon1[0] - f1x,
                        beacon1[1] - f1y,
                        beacon1[2] - f1z,
                    )
                    pos2 = (beacon2[0] - x_rel, beacon2[1] - y_rel, beacon2[2] - z_rel)
                    candidate.pos = pos2
                    if scanners_match(fixed_scanner, candidate):
                        candidate.fixed = True
                        return candidate
    return None


def scanners_match(scanner1, scanner2):
    s1x, s1y, s1z = scanner1.pos
    s2x, s2y, s2z = scanner2.pos
    match_count = 0
    for beacon1 in scanner1.beacon_list:
        for beacon2 in scanner2.beacon_list:
            x1, y1, z1 = beacon1[0] - s1x, beacon1[1] - s1y, beacon1[2] - s1z
            x2, y2, z2 = beacon2[0] - s2x, beacon2[1] - s2y, beacon2[2] - s2z
            if x1 == x2 and y1 == y2 and z1 == z2:
                match_count += 1
                break
    return match_count >= 12


def count_beacons(scanner_array):
    beacons = set()
    for scanner in scanner_array:
        sx, sy, sz = scanner.pos
        for beacon in scanner.beacon_list:
            bx, by, bz = beacon
            coords = (bx - sx, by - sy, bz - sz)
            beacons.add(coords)
    return len(beacons)


def manhattan_distance(scanner1, scanner2):
    s1x, s1y, s1z = scanner1.pos
    s2x, s2y, s2z = scanner2.pos
    return abs(s1x - s2x) + abs(s1y - s2y) + abs(s1z - s2z)


with open("2021/res/in19.txt") as file:
    str_scanners = file.read().split("\n\n")

num_scanners = len(str_scanners)

scanners = []
for i, scanner in enumerate(str_scanners):
    beacon_list = [
        tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]
    ]
    fixed = i == 0  # scanner 0 is fixed
    s = Scanner(i, beacon_list, fixed)
    scanners.append(s)

fixed_ids = set()
fixed_ids.add(0)
fixed_count = 1
fixed_scanners = [scanners[0]]
fixed_scanner_queue = deque([scanners[0]])
while fixed_count < num_scanners:
    fixed = fixed_scanner_queue.popleft()
    for i, scanner in enumerate(scanners):
        if scanner.scanner_id not in fixed_ids:
            match = match_scanners(fixed, scanner)
            if match:
                fixed_count += 1
                print(f"match found! found {fixed_count} of {num_scanners}")
                fixed_ids.add(match.scanner_id)
                fixed_scanner_queue.append(match)
                fixed_scanners.append(match)

pt1 = count_beacons(fixed_scanners)
pt2 = 0
for i in range(len(fixed_scanners) - 1):
    for j in range(1, len(fixed_scanners)):
        dist = manhattan_distance(fixed_scanners[i], fixed_scanners[j])
        if dist > pt2:
            pt2 = dist

print("Part 1: ", pt1)
print("Part 2: ", pt2)
