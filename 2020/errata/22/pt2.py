with open("2020/22/in.txt") as file:
    p1, p2 = file.read().split("\n\n")

p1 = [int(x) for x in p1.split("\n")[1:]]
p2 = [int(x) for x in p2.split("\n")[1:]]
print(len(p1), len(p2))


def confId(p1, p2):
    return (*p1, "|", *p2)


def newCombat(p1, p2):
    decksSeen = set()
    winnerFound = False
    while len(p1) > 0 and len(p2) > 0 and not winnerFound:
        if confId(p1, p2) in decksSeen:
            winnerFound = True
            return (1, p1, p2)
        decksSeen.add(confId(p1, p2))
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            newP1 = [*(p1[:c1])]
            newP2 = [*(p2[:c2])]
            winner, _, _ = newCombat(newP1, newP2)
            if winner == 1:
                p1.append(c1)
                p1.append(c2)
            elif winner == 2:
                p2.append(c2)
                p2.append(c1)
            else:
                print("******GRAVE ERROR******")
        elif c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if winnerFound or len(p1) > 0:
        return (1, p1, p2)
    else:
        return (2, p1, p2)


winner, p1, p2 = newCombat(p1, p2)

print(winner, p1, p2)

final = p1 if winner == 1 else p2

score = 0
curr = 1
while len(final) > 0:
    score += final.pop() * curr
    curr += 1

print(score)
