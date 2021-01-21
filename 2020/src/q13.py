with open("2020/res/in13.txt") as file:
    ts, bString = file.read().split("\n")

ts = int(ts)
buses = [int(x) for x in bString.split(",") if x != "x"]

minWait = max(buses) + 1
busNum = None
for bus in buses:
    if ts % bus != 0:
        nextTime = ((ts // bus) + 1) * bus
        wait = nextTime - ts
        if wait < minWait:
            busNum = bus
            minWait = wait
    else:
        print("0 wait")

print("Part 1: ", busNum * minWait)

numBuses = [(int(x), i) for i, x in enumerate(bString.split(",")) if x != "x"]


def compareTwo(base, step, bus2, bus2off):
    curr = base
    while (curr + bus2off) % bus2 != 0:
        curr += step
    newStep = step * bus2
    return (curr, newStep)


progress = numBuses[0][0]
step = numBuses[0][0]
for bus in numBuses[1:]:
    num, offset = bus
    progress, step = compareTwo(progress, step, num, offset)

print("Part 2: ", progress)
