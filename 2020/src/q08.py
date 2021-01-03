with open("2020/res/in08.txt") as file:
    instructions = file.read().split("\n")

acc = 0
index = 0
run = set()
while index not in run:
    run.add(index)
    rule, val = instructions[index].split(" ")
    if rule == "acc":
        acc += int(val)
        index += 1
    elif rule == "nop":
        index += 1
    else:  # rule == "jmp"
        index += int(val)

print("Part 1: ", acc)

numInstructions = len(instructions)

for i in range(numInstructions):
    rule2, val2 = instructions[i].split(" ")
    if rule2 == "nop":
        instructions[i] = "jmp " + val2
    elif rule2 == "jmp":
        instructions[i] = "nop " + val2
    else:
        continue

    acc = 0
    index = 0
    run = set()
    while index not in run and index < numInstructions and index >= 0:
        run.add(index)
        rule, val = instructions[index].split(" ")
        if rule == "acc":
            acc += int(val)
            index += 1
        elif rule == "nop":
            index += 1
        else:
            index += int(val)

    if index >= numInstructions:
        break

    if rule2 == "nop":
        instructions[i] = "nop " + val2
    elif rule2 == "jmp":
        instructions[i] = "jmp " + val2

print("Part 2: ", acc)
