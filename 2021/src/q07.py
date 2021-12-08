with open("2021/res/in07.txt") as file:
    crabs = [int(crab) for crab in file.read().split(",")]

min_val = min(crabs)
max_val = max(crabs)

total1 = None
total2 = None
for i in range(min_val, max_val + 1):
    temp_total1 = 0
    temp_total2 = 0
    for crab in crabs:
        diff = abs(crab - i)
        temp_total1 += diff
        temp_total2 += int(diff * (diff + 1) / 2)
    if total1 is None or temp_total1 < total1:
        total1 = temp_total1
    if total2 is None or temp_total2 < total2:
        total2 = temp_total2

print("Part 1: ", total1)
print("Part 2: ", total2)
