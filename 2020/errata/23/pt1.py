start = list("137826495")
val = "1"
numVals = len(start)


def turn(inArray, val):
    idx = inArray.index(val)
    newArray = inArray[idx:] + inArray[:idx]
    pickUp = [newArray.pop(1), newArray.pop(1), newArray.pop(1)]
    dest = int(val) - 1
    while str(dest) not in newArray:
        if dest == 0:
            dest = 9
        else:
            dest -= 1
    destIdx = newArray.index(str(dest))
    finalArray = newArray[: destIdx + 1] + pickUp + newArray[destIdx + 1 :]
    return finalArray, finalArray[1]


for i in range(100):
    start, val = turn(start, val)

print(start, val)
