from math import floor, ceil


def magnitude(fish_num):
    l, r = fish_num
    left = l if type(l) == int else magnitude(l)
    right = r if type(r) == int else magnitude(r)
    return (3 * left) + (2 * right)


def find_explosion(fish_num, depth):
    l, r = fish_num
    l_int = type(l) == int
    r_int = type(r) == int
    if l_int and r_int and depth >= 4:
        return True, l, r
    if l_int and r_int and depth < 4:
        return False, 0, 0
    if not l_int:
        found, l_val, r_val = find_explosion(l, depth + 1)
        if found:
            return True, l_val, r_val
    if not r_int:
        found, l_val, r_val = find_explosion(r, depth + 1)
        if found:
            return True, l_val, r_val
    return False, 0, 0


def find_num(any_string):
    return any_string.replace(",", " ").replace("[", " ").replace("]", " ").split()


def find_index(fish_string, explode_string):
    for i in range(len(fish_string)):
        if fish_string[i:].startswith(explode_string):
            count = 0
            for char in fish_string[:i]:
                if char == "[":
                    count += 1
                if char == "]":
                    count -= 1
            if count >= 4:
                return i
    return -1


def explode(fish_num):
    exploded, l, r = find_explosion(fish_num, 0)
    if exploded:
        fish_string = str(fish_num)
        explode_string = f"[{l}, {r}]"
        idx = find_index(fish_string, explode_string)
        l_fish = fish_string[:idx]
        r_fish = fish_string[idx + len(explode_string) :]
        l_vals = find_num(l_fish)
        if len(l_vals) > 0:
            l_val = l_vals[-1]
            new_val = str(int(l_val) + l)
            l_fish = new_val.join(l_fish.rsplit(l_val, 1))
        r_vals = find_num(r_fish)
        if len(r_vals) > 0:
            r_val = r_vals[0]
            new_val = str(int(r_val) + r)
            r_fish = new_val.join(r_fish.split(r_val, 1))
        new_fish_num = eval("0".join([l_fish, r_fish]))
        return True, new_fish_num
    return False, fish_num


def find_split(fish_num, pos):
    curr_pos = pos
    l, r = fish_num
    if type(l) != int:
        found, found_pos, val = find_split(l, curr_pos + "0")
        if found:
            return True, found_pos, val
    if type(l) == int and l > 9:
        return True, curr_pos + "0", l
    if type(r) != int:
        found, found_pos, val = find_split(r, curr_pos + "1")
        if found:
            return True, found_pos, val
    if type(r) == int and r > 9:
        return True, curr_pos + "1", r
    return False, "", -1


def split(fish_num):
    found_split, found_pos, val = find_split(fish_num, "")
    if found_split:
        half = val / 2
        l = floor(half)
        r = ceil(half)
        new_num_string = f"[{l}, {r}]"
        return True, eval(str(fish_num).replace(str(val), new_num_string, 1))
    return False, fish_num


with open("2021/res/in18.txt") as file:
    lines = file.read().split("\n")

fish_nums = [eval(line) for line in lines]

current = fish_nums[0]
for fish_num in fish_nums[1:]:
    new_fish_num = [current, fish_num]
    action_happened = True
    while action_happened:
        did_explode, result = explode(new_fish_num)
        if did_explode:
            action_happened = True
            new_fish_num = result
            continue
        did_split, result = split(new_fish_num)
        if did_split:
            action_happened = True
            new_fish_num = result
            continue
        action_happened = False
    current = new_fish_num

pt1 = magnitude(current)

largest = 0
for i in range(len(fish_nums)):
    print(f"{i} of {len(fish_nums)}")
    for j in range(len(fish_nums)):
        if i == j:
            continue
        new_fish_num = [fish_nums[i], fish_nums[j]]
        action_happened = True
        while action_happened:
            did_explode, result = explode(new_fish_num)
            if did_explode:
                action_happened = True
                new_fish_num = result
                continue
            did_split, result = split(new_fish_num)
            if did_split:
                action_happened = True
                new_fish_num = result
                continue
            action_happened = False
        mag = magnitude(new_fish_num)
        if mag > largest:
            largest = mag

pt2 = largest

print("Part 1: ", pt1)
print("Part 2: ", pt2)
