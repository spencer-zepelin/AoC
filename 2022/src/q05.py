from copy import deepcopy
from math import ceil

with open("2022/res/in05.txt") as file:
    rows, ops = file.read().split("\n\n")

rows = rows.split("\n")
ops = ops.split("\n")

num_stacks = ceil(len("".join(rows[0])) / 4)
stacks = [[] for _ in range(num_stacks)]
for row in rows[:-1]:
    for i in range(num_stacks):
        idx = (i * 4) + 1
        val = row[idx]
        if val != " ":
            stacks[i].append(val)

for stack in stacks:
    stack.reverse()
stacks2 = deepcopy(stacks)

for op in ops:
    rest, to = op.split(" to ")
    to = int(to) - 1
    rest, fro = rest.split(" from ")
    fro = int(fro) - 1
    _, cubes = rest.split(" ")
    cubes = int(cubes)

    pt2_temp = []
    for i in range(cubes):
        cube = stacks[fro].pop()
        stacks[to].append(cube)

        pt2_temp += stacks2[fro].pop()

    pt2_temp.reverse()
    stacks2[to].extend(pt2_temp)


pt1 = "".join([stack[-1] for stack in stacks])
pt2 = "".join([stack[-1] for stack in stacks2])

print("Part 1: ", pt1)
print("Part 2: ", pt2)
