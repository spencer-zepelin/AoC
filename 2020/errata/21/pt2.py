with open("2020/21/in.txt") as file:
    foods = file.read().split("\n")


def process(food):
    ings, algs = food.split(" (contains ")
    algs = algs.replace(")", "").split(", ")
    ings = ings.split(" ")
    return (algs, ings)


foods = [process(food) for food in foods]

algDict = {}
algSet = set()
for food in foods:
    algs, ings = food
    ingSet = set(ings)
    for alg in algs:
        algSet.add(alg)
        if alg in algDict:
            algDict[alg] = algDict[alg].intersection(ingSet)
        else:
            algDict[alg] = ingSet

print(algDict)

badIngs = set()

for _, v in algDict.items():
    badIngs = badIngs.union(v)

numAlgs = len(badIngs)


found = {}
while len(found) < numAlgs:
    for k, v in algDict.items():
        if len(v) == 1:
            found[list(v)[0]] = k
        else:
            remaining = set()
            for ing in v:
                if ing not in found:
                    remaining.add(ing)
            algDict[k] = remaining
print(found)

sortedAllergens = ",".join(
    [x[0] for x in sorted(found.items(), key=lambda item: item[1])]
)
print(sortedAllergens)
