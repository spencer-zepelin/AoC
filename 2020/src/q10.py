with open("2020/res/in10.txt") as file:
    jolts = file.read().split("\n")

jolts = sorted([int(x) for x in jolts])

curr = 0
ones = 0
threes = 1  # diff for device itself
for jolt in jolts:
    diff = jolt - curr
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
    curr = jolt
print("Part 1: ", ones * threes)

memo = {}
memo[0] = 1
for jolt in jolts:
    memo[jolt] = memo.get(jolt - 1, 0) + memo.get(jolt - 2, 0) + memo.get(jolt - 3, 0)
print("Part 2: ", memo[jolts[-1]])
