with open("2021/res/in03.txt") as file:
    rows = file.read().split("\n")

sums = [0] * len(rows[0])

for row in rows:
    for i, char in enumerate(row):
        if char == "1":
            sums[i] += 1
        else:
            sums[i] -= 1

g = ""
e = ""
for val in sums:
    if val > 0:
        g += "1"
        e += "0"
    else:
        g += "0"
        e += "1"

gamma = int(g, 2)
epsilon = int(e, 2)
print("Part 1: ", gamma * epsilon)

g_cand = [list(x) for x in rows]
g_temp = []
curr = 0
while len(g_cand) > 1:
    common = 0
    for cand in g_cand:
        if cand[curr] == "1":
            common += 1
        else:
            common -= 1
    winner = "1" if common >= 0 else "0"
    for cand in g_cand:
        if cand[curr] == winner:
            g_temp.append(cand)
    g_cand = g_temp
    g_temp = []
    curr += 1

oxygen = int("".join(g_cand[0]), 2)

e_cand = [list(x) for x in rows]
e_temp = []
curr = 0
while len(e_cand) > 1:
    common = 0
    for cand in e_cand:
        if cand[curr] == "1":
            common += 1
        else:
            common -= 1
    winner = "0" if common >= 0 else "1"
    for cand in e_cand:
        if cand[curr] == winner:
            e_temp.append(cand)
    e_cand = e_temp
    e_temp = []
    curr += 1

co2 = int("".join(e_cand[0]), 2)

print("Part 2: ", oxygen * co2)
