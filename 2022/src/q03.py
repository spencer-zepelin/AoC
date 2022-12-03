with open("2022/res/in03.txt") as file:
    sacks = file.read().split("\n")


def get_val(item):
    asc_val = ord(item)
    uppers_correct = asc_val - 38
    if uppers_correct <= 52:
        return uppers_correct
    return uppers_correct - 58


pt1 = 0
for sack in sacks:
    half_items = len(sack) // 2
    first_half = set(sack[:half_items])
    second_half = set(sack[half_items:])
    in_both = list(first_half.intersection(second_half))[0]
    pt1 += get_val(in_both)

i = 0
pt2 = 0
while i < len(sacks):
    g1 = set(sacks[i])
    g2 = set(sacks[i + 1])
    g3 = set(sacks[i + 2])
    badge = list(g1.intersection(g2).intersection(g3))[0]
    pt2 += get_val(badge)
    i += 3

print("Part 1: ", pt1)
print("Part 2: ", pt2)
