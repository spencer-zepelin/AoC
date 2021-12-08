from collections import deque

with open("2020/22/in2.txt") as file:
    p1, p2 = file.read().split("\n\n")


p1 = deque([int(x) for x in p1.split("\n")[1:]])
p2 = deque([int(x) for x in p2.split("\n")[1:]])
print(len(p1), len(p2))


memo = set()


def rCombat(p1, p2):
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
        return (1, p1, p2)
    else:
        p2.append(c2)
        p2.append(c1)
        return (2, p1, p2)


while len(p1) > 0 and len(p2) > 0:
    w, p1, p2 = rCombat(p1, p2)

print("p1: ", p1)
print("p2: ", p2)

winner = p1 if len(p2) == 0 else p2

score = 0
curr = 1
while len(winner) > 0:
    score += winner.pop() * curr
    curr += 1

print(score)
