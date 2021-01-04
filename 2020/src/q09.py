with open("2020/res/in09.txt") as file:
    numbers = file.read().split("\n")


def find_sum(inArray, val):
    for i in range(0, len(inArray) - 1):
        for j in range(i + 1, len(inArray)):
            if (inArray[i] + inArray[j]) == val:
                return True
    return False


ints = [int(x) for x in numbers]
search = ints[:25]
index = 25
while find_sum(search, ints[index]):
    search.pop(0)
    search.append(ints[index])
    index += 1

value = ints[index]
print("Part 1: ", value)

lIdx = 0
rIdx = 1
runningSum = ints[0]

while runningSum != value:
    if runningSum < value:
        runningSum += ints[rIdx]
        rIdx += 1
    else:  # runningSum > value
        runningSum -= ints[lIdx]
        lIdx += 1

span = ints[lIdx:rIdx]
print("Part 2: ", min(span) + max(span))
