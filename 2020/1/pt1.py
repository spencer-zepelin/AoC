if __name__ == "__main__":
    file = open("in.txt")
    vals = file.read().splitlines()[:-1]
    kv = {}
    for v in vals:
        val = int(v)
        if val in kv:
            print([val, kv[val], val * kv[val]])
            break
        kv[2020 - val] = val
    file.close()
