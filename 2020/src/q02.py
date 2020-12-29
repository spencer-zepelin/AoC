with open("2020/res/in02.txt") as file:
    passwords = file.read().split("\n")

ctr = 0
for pw_string in passwords:
    times, letter, password = pw_string.split(" ")
    low, high = times.split("-")
    low = int(low)
    high = int(high)
    letter = letter[0]
    ltr_ctr = 0
    for char in password:
        if char == letter:
            ltr_ctr += 1
    if ltr_ctr <= high and ltr_ctr >= low:
        ctr += 1
print("Part 1: ", ctr)

ctr = 0
for pw_string in passwords:
    times, letter, password = pw_string.split(" ")
    low, high = times.split("-")
    low = int(low) - 1
    high = int(high) - 1
    letter = letter[0]
    valid = False
    if password[low] == letter:
        valid = not valid
    if password[high] == letter:
        valid = not valid
    if valid:
        ctr += 1
print("Part 2: ", ctr)
