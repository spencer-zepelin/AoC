with open("2021/res/in08.txt") as file:
    rows = file.read().split("\n")

in_vals = [row.split(" | ")[0].split(" ") for row in rows]
out_vals = [row.split(" | ")[1].split(" ") for row in rows]

# Part 1
pt1 = 0
for row in out_vals:
    for val in row:
        if len(val) in [2, 3, 4, 7]:
            pt1 += 1
print("Part 1: ", pt1)

# Part 2
pt2 = 0
for i in range(len(in_vals)):
    all_vals = [''.join(sorted(val)) for val in in_vals[i] + out_vals[i]]
    string_key = {}
    num_key = {}
    known_letter = {}
    for val in all_vals:
        if len(val) == 2:
            string_key[val] = 1
            num_key[1] = val
        elif len(val) == 3:
            string_key[val] = 7
            num_key[7] = val
        elif len(val) == 4:
            string_key[val] = 4
            num_key[4] = val
        elif len(val) == 7:
            string_key[val] = 8
            num_key[8] = val
    # Find A
    for char in num_key[7]:
        if char not in num_key[1]:
            known_letter['a'] = char
            break
    # Find 6 and C
    for val in all_vals:
        if len(val) == 6 and (num_key[1][1] not in val or num_key[1][0] not in val):
            num_key[6] = val
            string_key[val] = 6
            c = num_key[1][0] if num_key[1][0] not in val else num_key[1][1]
            known_letter['c'] = c
    # Find F
    known_letter['f'] = num_key[1][0] if num_key[1][0] != known_letter['c'] else num_key[1][1]
    # Find 3 and D
    for val in all_vals:
        if len(val) == 5 and known_letter['a'] in val and known_letter['c'] in val and known_letter['f'] in val:
            string_key[val] = 3
            num_key[3] = val
            for char in val:
                if char in num_key[4] and char not in num_key[1]:
                    known_letter['d'] = char
                    break
            break
    # Find 2
    for val in all_vals:
        if len(val) == 5 and known_letter['f'] not in val:
            string_key[val] = 2
            num_key[2] = val
            break
    # Find 5
    for val in all_vals:
        if len(val) == 5 and known_letter['c'] not in val:
            string_key[val] = 5
            num_key[5] = val
            break
    # Find 9
    for val in all_vals:
        if len(val) == 6 and known_letter['d'] in val and known_letter['c'] in val:
            string_key[val] = 9
            num_key[9] = val
            break
    # Find 0
    for val in all_vals:
        if val not in string_key:
            for j in range(10):
                if j not in num_key:
                    string_key[val] = j
                    num_key[j] = val

    # Decode
    time = ''
    for val in all_vals[-4:]:
        time += str(string_key[val])
    pt2 += int(time)

print("Part 2: ", pt2)

# In 7 (3len) but not 1 (2len) == a xx
# in 1 (2len) either c or f
# in 4 (4len) but not 1, either b or d
# in len5 with both c and f is 3
# 8 - 6 missing one of c or f yields c
# c yields f
# len 5 which has all of a, c, f overlaps d with len 4
# c,f,d yields b
# on len 5 all have g, one has e
