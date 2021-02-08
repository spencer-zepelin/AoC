from math import prod

with open("2020/res/in16.txt") as file:
    valid, mine, nearbys = file.read().split("\n\n")

# Process Rules
ranges = []
ruleNames = []
rules = valid.split("\n")
numRules = len(rules)
for line in rules:
    name, specs = line.split(": ")
    ruleNames.append(name)
    r1, r2 = specs.split(" or ")
    r1l, r1r = r1.split("-")
    r2l, r2r = r2.split("-")
    ranges = ranges + [((int(r1l), int(r1r)), (int(r2l), int(r2r)))]

# Process My Ticket
START_VAL = "departure"
myTicket = [int(val) for val in mine.split("\n")[1].split(",")]

# Count and Filter Invalid Tickets
errorSum = 0
validTickets = []
tickets = nearbys.split("\n")[1:]
for ticket in tickets:
    validTicket = True
    for value in ticket.split(","):
        valid = False
        num = int(value)
        for span1, span2 in ranges:
            if (num >= span1[0] and num <= span1[1]) or (
                num >= span2[0] and num <= span2[1]
            ):
                valid = True
                break
        if not valid:
            errorSum += num
            validTicket = False
    if validTicket:
        validTickets.append(ticket)

print("Part 1: ", errorSum)

# Determine Possible Positions by Rule
candidates = {}
for name, ruleRange in zip(ruleNames, ranges):
    low, high = ruleRange
    llow, rlow = low
    lhigh, rhigh = high
    remaining = set(range(numRules))
    for ticket in validTickets:
        for i, val in enumerate(ticket.split(",")):
            num = int(val)
            inLow = num >= llow and num <= rlow
            inHigh = num >= lhigh and num <= rhigh
            if not (inLow or inHigh):
                remaining.discard(i)
    candidates[name] = remaining

# Determine Rule Position by Elimination
ruleMap = {}
while len(ruleMap) < numRules:
    for name, vals in candidates.items():
        found = vals.difference(set(ruleMap.values()))
        if len(found) == 1:
            ruleMap[name] = found.pop()

# Calculate Part Two Solution
pt2 = prod([myTicket[idx] for key, idx in ruleMap.items() if key.startswith(START_VAL)])

print("Part 2: ", pt2)