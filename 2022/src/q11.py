from copy import deepcopy

with open("2022/res/in11.txt") as file:
    raw_monkeys = file.read().split("\n\n")


def monkey_around(monks, rounds, worry_func):
    monkeys = deepcopy(monks)
    for _ in range(rounds):
        for monk_key in range(len(monkeys)):
            m = monkeys[monk_key]
            while len(m["items"]) > 0:
                old = m["items"].pop(0)
                m["count"] += 1
                new = worry_func(eval(m["op"]))
                throw_to = m["pass"] if new % m["div_test"] == 0 else m["fail"]
                monkeys[throw_to]["items"].append(new)

    counts = sorted([monkey["count"] for monkey in monkeys.values()], reverse=True)
    return counts[0] * counts[1]


universal = 1
monkeys = {}
for raw in raw_monkeys:
    monkey = {}
    lines = raw.split("\n")
    key = int(lines[0][-2])
    monkey["items"] = list(map(int, lines[1].split(": ").pop().split(", ")))
    monkey["op"] = lines[2].split(" = ").pop()
    mod = int(lines[3].split().pop())
    universal *= mod
    monkey["div_test"] = mod
    monkey["pass"] = int(lines[4].split().pop())
    monkey["fail"] = int(lines[5].split().pop())
    monkey["count"] = 0
    monkeys[key] = monkey

pt1 = monkey_around(monkeys, 20, lambda x: x // 3)
pt2 = monkey_around(monkeys, 10_000, lambda x: x % universal)
print("Part 1: ", pt1)
print("Part 2: ", pt2)
