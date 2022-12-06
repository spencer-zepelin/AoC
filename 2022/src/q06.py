with open("2022/res/in06.txt") as file:
    stream = file.read()


def packet(stream, unique_chars):
    for i in range(len(stream)):
        char_set = set(stream[i : (i + unique_chars)])
        if len(char_set) == unique_chars:
            return i + unique_chars
    return -1


pt1 = packet(stream, 4)
pt2 = packet(stream, 14)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
