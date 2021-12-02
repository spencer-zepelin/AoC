with open("2021/res/in02.txt") as file:
    rows = file.read().split("\n")

vals = [row.split(' ') for row in rows]

h = 0
d = 0
for val in vals:
    instruction = val[0]
    num = int(val[1])
    if instruction == 'forward':
        h += num
    elif instruction == 'down':
        d += num
    elif instruction == 'up':
        d -= num

h2 = 0
d2 = 0
aim = 0
for val in vals:
    instruction = val[0]
    num = int(val[1])
    if instruction == 'forward':
        h2 += num
        d2 += (aim * num)
    elif instruction == 'down':
        aim += num
    elif instruction == 'up':
        aim -= num


print("Part 1: ", h * d)
print("Part 2: ", h2 * d2)