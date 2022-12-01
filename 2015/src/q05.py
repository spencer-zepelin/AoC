with open("2015/res/in05.txt") as file:
    words = file.read().split("\n")


NAUGHTY_WORDS = ["ab", "cd", "pq", "xy"]


def nice1(word):
    has_double = False
    vowels = 0
    for i in range(len(word) - 1):
        if word[i] in "aeiou":
            vowels += 1
        substring = word[i : i + 2]
        if substring in NAUGHTY_WORDS:
            return False
        if substring[0] == substring[1]:
            has_double = True
    if word[-1] in "aeiou":
        vowels += 1

    return vowels >= 3 and has_double


def nice2(word):
    memo = {}
    has_repeated = False
    for i in range(len(word) - 1):
        substring = word[i : i + 2]
        found = memo.get(substring, "NA")
        if found == "NA":
            memo[substring] = [i]
        else:
            for index in found:
                if i - index > 1:
                    has_repeated = True
            memo[substring] = found + [i]

    has_sandwich = False
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            has_sandwich = True
    return has_repeated and has_sandwich


def count_nice(words):
    count1 = 0
    count2 = -0
    for word in words:
        if nice1(word):
            count1 += 1
        if nice2(word):
            count2 += 1
    return count1, count2


pt1, pt2 = count_nice(words)
print("Part 1: ", pt1)
print("Part 2: ", pt2)
