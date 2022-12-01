with open("2022/res/in01.txt") as file:
    elves = file.read().split("\n\n")

most, second, third, *rest = sorted(
    [sum([int(item) for item in elf.split("\n")]) for elf in elves], reverse=True
)

print("Part 1: ", most)
print("Part 2: ", most + second + third)
