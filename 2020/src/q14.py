with open("2020/res/in14.txt") as file:
    lines = file.read().split("\n")


def toBstring(base10str):
    return bin(int(base10str))[2:].zfill(mLen)


def maskVal(mask, val):
    out = ""
    for i in range(mLen):
        if mask[i] in "01":
            out += mask[i]
        else:
            out += val[i]
    return out


def maskValFloating(mask, val):
    outArray = [""]
    for i in range(mLen):
        if mask[i] == "X":
            new = []
            for j in range(len(outArray)):
                new.append(outArray[j] + "1")
                outArray[j] = outArray[j] + "0"
            outArray = outArray + new
        elif mask[i] == "1":
            for j in range(len(outArray)):
                outArray[j] = outArray[j] + "1"
        else:
            for j in range(len(outArray)):
                outArray[j] = outArray[j] + val[i]
    return [int(x, 2) for x in outArray]


mLen = 36
mask = ""
mem = {}
mem2 = {}
for line in lines:
    cmd, val = line.split(" = ")
    if cmd == "mask":
        mask = val
    else:
        # Pt 1
        cmd = cmd[4:-1]
        mem[cmd] = int(maskVal(mask, toBstring(val)), 2)
        # Pt 2
        addresses = maskValFloating(mask, toBstring(cmd))
        for address in addresses:
            mem2[address] = int(val)

print("Part 1: ", sum(mem.values()))
print("Part 2: ", sum(mem2.values()))
