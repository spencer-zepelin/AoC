with open("2020/res/in01.txt") as file:
    vals = [int(x) for x in file.read().split("\n")]

kv = {}
for val in vals:
    if val in kv:
        print("Part 1: ", [val, kv[val], val * kv[val]])
        break
    kv[2020 - val] = val


def arb_sum(sum, index, array):
    kv = {}
    length = len(array)
    for i in range(index, length):
        val = array[i]
        if val in kv:
            return (val, kv[val])
        kv[sum - val] = val
    return False


for i, v in enumerate(vals):
    result = arb_sum(2020 - v, i, vals)
    if result:
        print(
            "Part 2: ",
            [
                v,
                result[0],
                result[1],
                v + result[0] + result[1],
                v * result[0] * result[1],
            ],
        )
        break
