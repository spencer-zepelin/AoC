from copy import deepcopy
from functools import cmp_to_key
from math import prod


def test_pair(left_, right_):
    left = deepcopy(left_)
    right = deepcopy(right_)
    over = False
    while not over:
        if len(left) == 0 and len(right) == 0:
            return "NA"
        if len(left) == 0:
            return True
        if len(right) == 0:
            return False
        l, r = left.pop(0), right.pop(0)
        if type(l) == int and type(r) == int:
            if l == r:
                continue
            return l < r
        elif type(l) == list and type(r) == list:
            result = test_pair(l, r)
            if result == "NA":
                continue
            return result
        else:
            if type(l) == int:
                l = [l]
            elif type(r) == int:
                r = [r]
            result = test_pair(l, r)
            if result == "NA":
                continue
            return result


def sort_packets(a, b):
    return -1 if test_pair(a, b) else 1


with open("2022/res/in13.txt") as file:
    pairs = file.read().split("\n\n")

pt1 = 0
for i, pair in enumerate(pairs, start=1):
    str1, str2 = pair.split("\n")
    left = eval(str1)
    right = eval(str2)
    if test_pair(left, right):
        pt1 += i


with open("2022/res/in13.txt") as file:
    packets = list(map(eval, filter(lambda x: x != "", file.read().split("\n"))))

dividers = [[[2]], [[6]]]
packets.extend(dividers)
packets.sort(key=cmp_to_key(sort_packets))

pt2 = prod([packets.index(divider) + 1 for divider in dividers])

print("Part 1: ", pt1)
print("Part 2: ", pt2)
