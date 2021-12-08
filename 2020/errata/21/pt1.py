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

badIngs = set()

for _, v in algDict.items():
    badIngs = badIngs.union(v)

print(badIngs, len(badIngs))

numGood = 0
numGood = sum(
    [sum([1 if ing not in badIngs else 0 for ing in food[1]]) for food in foods]
)
print(numGood)
