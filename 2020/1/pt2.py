def arb_sum(sum, index, array):
    kv = {}
    length = len(array)
    for i in range(index, length):
        val = array[i]
        if val in kv:
            return (val, kv[val])
        kv[sum - val] = val
    return False


if __name__ == "__main__":
    file = open("in.txt")
    vals = list(map(int, file.read().splitlines()[:-1]))
    for i, v in enumerate(vals):
        result = arb_sum(2020 - v, i, vals)
        if result:
            print(
                [
                    v,
                    result[0],
                    result[1],
                    v + result[0] + result[1],
                    v * result[0] * result[1],
                ]
            )
            break
    file.close()
