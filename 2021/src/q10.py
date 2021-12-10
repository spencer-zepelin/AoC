with open("2021/res/in10.txt") as file:
    lines = file.read().split("\n")

openers = '{[<('
pairs = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')'
}
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
points2 = {
    '{': 3,
    '[': 2,
    '<': 4,
    '(': 1
}

invalids = []
incomplete_scores = []
for line in lines:
    stack = []
    corrupt = False
    for char in line:
        if char in openers:
            stack.append(char)
        else:
            left = stack.pop()
            if pairs[left] != char:
                invalids.append(char)
                corrupt = True
                break
    if not corrupt:
        score = 0
        stack.reverse()
        for char in stack:
            score = (score * 5) + points2[char]
        incomplete_scores.append(score)

pt1 = 0
for invalid in invalids:
    pt1 += points[invalid]

idx = len(incomplete_scores) // 2
pt2 = sorted(incomplete_scores)[idx]

print("Part 1: ", pt1)
print("Part 2: ", pt2)
