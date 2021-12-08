# curr incorrect on test

start = list("137826495")  # actual
# start = list("389125467") #test
start = list(map(int, start))
val = "1"
numVals = 1000000
numMoves = 10000000
# numVals = 20
# numMoves = 1

for i in range(10, numVals + 1):
    start.append(i)

queue = {}
for i in range(numVals):
    nextIdx = (i + 1) % numVals
    priorIdx = i - 1
    if priorIdx == -1:
        priorIdx = numVals - 1
    queue[start[i]] = {
        "value": start[i],
        "next": start[nextIdx],
        "prior": start[priorIdx],
    }


def turn(queue, val):
    curr = queue[val]
    p1 = queue[curr["next"]]
    p2 = queue[p1["next"]]
    p3 = queue[p2["next"]]
    currNextKey = p3["next"]
    # print(currNextKey)
    queue[val]["next"] = currNextKey
    queue[currNextKey]["prior"] = val

    dest = val - 1
    while (
        dest
        in [
            p1["value"],
            p2["value"],
            p3["value"],
        ]
        or dest == 0
    ):
        if dest == 0:
            dest = numVals
        else:
            dest -= 1

    destNode = queue[dest]
    destTail = queue[destNode["next"]]
    p3["next"] = destTail["value"]
    destTail["prior"] = p3["value"]
    destNode["next"] = p1["value"]
    p1["prior"] = destNode["value"]

    return queue, currNextKey


# for k, v in queue.items():
#     print(k, "---", v)

val = 1
for i in range(numMoves):
    if i % 100000 == 0:
        print(i)
    queue, val = turn(queue, val)

# for k, v in queue.items():
#     print(k, "---", v)

k1 = queue[1]["next"]
k2 = queue[k1]["next"]
print(k1)
print(k2)
print(k1 * k2)


# # def turn(inArray, val):
# #     idx = inArray.index(val)
# #     pickUp = [inArray.pop(idx + 1), inArray.pop(idx + 1), inArray.pop(idx + 1)]
# #     dest = int(val) - 1
# #     while str(dest) in pickUp or dest == 0:
# #         if dest == 0:
# #             dest = numVals
# #         else:
# #             dest -= 1
# #     destIdx = inArray.index(str(dest))
# #     inArray.insert(destIdx + 1, pickUp[0])
# #     inArray.insert(destIdx + 2, pickUp[1])
# #     inArray.insert(destIdx + 3, pickUp[2])
# #     return inArray, inArray[idx + 1]


# # for i in range(numMoves):
# #     if i % 100 == 0:
# #         print(i)
# #     start, val = turn(start, val)

# # onedex = start.index("1")
# # print(
# #     start[onedex + 1],
# #     start[onedex + 2],
# #     start[onedex + 1] * start[onedex + 2],
# # )


# # def turn(inArray, val):
# #     idx = inArray.index(val)
# #     newArray = inArray[idx:] + inArray[:idx]
# #     pickUp = [newArray.pop(1), newArray.pop(1), newArray.pop(1)]
# #     dest = int(val) - 1
# #     while str(dest) in pickUp or dest == 0:
# #         if dest == 0:
# #             dest = numVals
# #         else:
# #             dest -= 1
# #     destIdx = newArray.index(str(dest))
# #     finalArray = newArray[: destIdx + 1] + pickUp + newArray[destIdx + 1 :]
# #     return finalArray, finalArray[1]


# # for i in range(numMoves):
# #     if i % 100 == 0:
# #         print(i)
# #     start, val = turn(start, val)

# # onedex = start.index("1")
# # print(
# #     start[int(onedex) + 1],
# #     start[int(onedex) + 2],
# #     start[int(onedex) + 1] * start[int(onedex) + 2],
# # )
