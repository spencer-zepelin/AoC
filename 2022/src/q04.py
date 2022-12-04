with open("2022/res/in04.txt") as file:
    pairs = file.read().split("\n")

pt1 = 0
pt2 = 0
for pair in pairs:
    one, two = pair.split(",")
    one_low, one_high = map(int, one.split("-"))
    two_low, two_high = map(int, two.split("-"))
    if (one_low <= two_low and one_high >= two_high) or (
        two_low <= one_low and two_high >= one_high
    ):
        pt1 += 1

    one_set = set(range(one_low, one_high + 1))
    two_set = set(range(two_low, two_high + 1))
    if len(one_set.intersection(two_set)) > 0:
        pt2 += 1


print("Part 1: ", pt1)
print("Part 2: ", pt2)
