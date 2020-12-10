with open("2020/10/in.txt") as file:
    jolts = file.read().split("\n")

print(jolts)

jolts = [int(x) for x in jolts]
jolts = sorted(jolts)

curr = 0
ones = 0
threes = 0
for jolt in jolts:
    diff = jolt - curr
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
    curr = jolt

print(ones, threes, ones * threes)