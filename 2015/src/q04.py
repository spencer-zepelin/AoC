import hashlib


def mine(key, match):
    val = 1
    while True:
        string = f"{key}{val}"
        hash = hashlib.md5(string.encode())
        match_len = len(match)
        init = str(hash.hexdigest())[:match_len]
        if init == match:
            return val
        else:
            val += 1


KEY = "ckczppom"

pt1 = mine(KEY, "00000")
print("Part 1: ", pt1)

pt2 = mine(KEY, "000000")
print("Part 2: ", pt2)
