with open("2022/res/in02.txt") as file:
    games = file.read().split("\n")

SCORE = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2,
    "C Z": 3 + 3,
}

SCORE2 = {
    "A X": 3,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

pt1 = 0
pt2 = 0
for game in games:
    pt1 += SCORE[game]
    pt2 += SCORE2[game]

print("Part 1: ", pt1)
print("Part 2: ", pt2)
