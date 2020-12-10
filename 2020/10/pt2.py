with open("2020/10/in.txt") as file:
    jolts = file.read().split("\n")

jolts = [int(x) for x in jolts]
jolts = sorted(jolts)

large = jolts[-1]

memo = {}
memo[0] = 1
for jolt in jolts:
    memo[jolt] = memo.get(jolt-1, 0) + memo.get(jolt-2, 0) + memo.get(jolt-3, 0)

print(memo[large])
