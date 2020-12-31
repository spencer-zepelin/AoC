with open("2020/res/in06.txt") as file:
    groups = file.read().split("\n\n")

result1 = 0
result2 = 0
for group in groups:
    peeps = group.split("\n")
    group = group.replace("\n", "")
    result1 += len(set(group))
    answers = set(peeps[0])
    if len(peeps) > 1:
        for p in peeps[1:]:
            answers.intersection_update(set(p))
    result2 += len(answers)

print("Part 1: ", result1)
print("Part 2: ", result2)
