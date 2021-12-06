with open("2021/res/in06.txt") as file:
    fishies = [int(fish) for fish in file.read().split(",")]

school = {i: 0 for i in range(9)}

for fish in fishies:
    school[fish] += 1

days1 = 80
days2 = 256
for day in range(days2):
    new_school = {}
    for i in range(9):
        if i == 6:
            new_school[i] = school[0] + school[7]
        elif i == 8:
            new_school[i] = school[0]
        else:
            new_school[i] = school[i + 1]
    school = new_school
    if day == days1 - 1:
        print('Part 1: ', sum(school.values()))

print('Part 2: ', sum(school.values()))
