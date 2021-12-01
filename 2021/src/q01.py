with open("2021/res/in01.txt") as file:
    str_vals = file.read().split("\n")

vals = [int(val) for val in str_vals]

curr = vals[0]
ctr = 0
for val in vals:
    if val > curr:
        ctr += 1
    curr = val

curr_sum = sum(vals[0:3])
ctr2 = 0
for i in range(len(vals[:-2])):
    val_sum = sum(vals[i:(i+3)])
    if val_sum > curr_sum:
        ctr2 += 1
    curr_sum = val_sum

print("Part 1: ", ctr)
print("Part 2: ", ctr2)
