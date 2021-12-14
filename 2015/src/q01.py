with open("2015/res/in01.txt") as file:
    input = file.read()

pt1 = 0
pt2 = False
for i, char in enumerate(input):
    pt1 += 1 if char == '(' else -1
    if not pt2 and pt1 < 0:
        pt2 = i + 1

print("Part 1: ", pt1)
print("Part 2: ", pt2)
