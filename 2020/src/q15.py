startingNums = [8, 11, 0, 19, 1, 2]

turn = 1
lastSeen = {}
for num in startingNums:
    lastSeen[num] = turn
    turn += 1

nextVal = 0
while turn < 30000000:
    if nextVal not in lastSeen:
        lastSeen[nextVal] = turn
        nextVal = 0
    else:
        temp = turn - lastSeen[nextVal]
        lastSeen[nextVal] = turn
        nextVal = temp
    turn += 1
    if turn == 2020:
        print("Part 1: ", nextVal)
print("Part 2: ", nextVal)
