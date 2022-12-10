with open("2022/res/in10.txt") as file:
    ops = file.read().split("\n")


def score_cycle(cycle, x):
    return cycle * x if cycle in [20, 60, 100, 140, 180, 220] else 0


x = 1
cycle = 0
pt1 = 0
for op in ops:
    cycle += 1
    pt1 += score_cycle(cycle, x)
    if op != "noop":
        cycle += 1
        pt1 += score_cycle(cycle, x)
        _, delt = op.split()
        x += int(delt)

x = 1
cycle = 0
screen = ["."] * 240
for op in ops:
    if cycle % 40 in [x - 1, x, x + 1]:
        screen[cycle] = "#"
    cycle += 1
    if op != "noop":
        if cycle % 40 in [x - 1, x, x + 1]:
            screen[cycle] = "#"
        cycle += 1
        _, delt = op.split()
        x += int(delt)

print("Part 1: ", pt1)
print("\nPart 2:\n---")
idx = 0
while idx < 240:
    print("".join(screen[idx : idx + 40]))
    idx += 40
