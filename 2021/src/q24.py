def safe_decrement(str_num):
    valid = False
    if str_num == "1111":
        return -1
    while not valid:
        str_num = str(int(str_num) - 1)
        if "0" not in str_num:
            valid = True
            return str_num


def test_valid(insts, num):
    idx = 0
    mem = {"w": 0, "x": 0, "y": 0, "z": 0}
    for inst in insts:
        op = inst[0]
        if op == "inp":
            model_val = int(num[idx])
            mem[inst[1]] = model_val
            idx += 1
        else:
            key = inst[1]
            val = mem[inst[2]] if inst[2] in "wxyz" else int(inst[2])
            if op == "add":
                mem[key] += val
            elif op == "mul":
                mem[key] *= val
            elif op == "div":
                mem[key] = mem[key] // val
            elif op == "mod":
                mem[key] = mem[key] % val
            elif op == "eql":
                mem[key] = 1 if mem[key] == val else 0
            else:
                print("unexpected OP")
                print(inst)
    is_valid = mem["z"] == 0
    if is_valid:
        print(f"{num} is a valid model number")
    else:
        print(f"{num} is NOT a valid model number")


def run_all(num, check_break=None):
    z = 0
    # first block
    z = int(num[0]) + 9

    # second block
    z = 26 * z + int(num[1]) + 1

    # third block
    z = 26 * z + int(num[2]) + 11

    # fourth block
    z = 26 * z + int(num[3]) + 3

    # fifth block
    check = (z % 26) - 11
    if check_break == 5:
        return check
    z = z // 26
    if check != int(num[4]):
        print("missed check 1")
        z = z * 26 + int(num[4]) + 10

    # sixth block
    z = z * 26 + int(num[5]) + 5

    # seventh block
    z = z * 26 + int(num[6])

    # eighth block
    check = (z % 26) - 6
    if check_break == 8:
        return check
    z = z // 26
    if check != int(num[7]):
        print("missed check 2")
        z = z * 26 + int(num[7]) + 7

    # ninth block
    z = z * 26 + int(num[8]) + 9

    # tenth block
    check = (z % 26) - 6
    if check_break == 10:
        return check
    z = z // 26
    if check != int(num[9]):
        print("missed check 3")
        z = z * 26 + int(num[9]) + 15

    # eleventh block
    check = (z % 26) - 6
    if check_break == 11:
        return check
    z = z // 26
    if check != int(num[10]):
        print("missed check 4")
        z = z * 26 + int(num[10]) + 4

    # twelth block
    check = (z % 26) - 16
    if check_break == 12:
        return check
    z = z // 26
    if check != int(num[11]):
        print("missed check 5")
        z = z * 26 + int(num[11]) + 10

    # thirteenth block
    # z needs to pass check or be less than 26
    check = (z % 26) - 4
    if check_break == 13:
        return check
    z = z // 26
    if check != int(num[12]):
        print("missed check 6")
        z = z * 26 + int(num[12]) + 4

    # fourteenth block
    # z needs to be less than 26 and pass check coming in
    check = (z % 26) - 2
    if check_break == 14:
        return check
    z = z // 26
    if check != int(num[13]):
        print("missed check 7")
        z = z * 26 + int(num[13]) + 9

    return z


first_four = "9999"
next_two = "99"
last_one = "9"

finished = False
pt1 = None
answer = ""
while not finished:
    restart = False
    test_string = ""
    while len(test_string) < 5:
        fifth = run_all(test_string + first_four, 5)
        if fifth > 0 and fifth < 10:
            test_string += first_four + str(fifth)
        else:
            first_four = safe_decrement(first_four)
            if first_four == -1:
                finished = True
                restart = True
                break

    if restart:
        continue

    while len(test_string) < 8:
        eighth = run_all(test_string + next_two, 8)
        if eighth > 0 and eighth < 10:
            test_string += next_two + str(eighth)
        else:
            if next_two == "11":
                next_two = "99"
                first_four = safe_decrement(first_four)
                restart = True
                if first_four == -1:
                    finished = True
                break
            next_two = safe_decrement(next_two)

    if restart:
        continue

    while len(test_string) < 14:
        tenth = run_all(test_string + last_one, 10)
        if tenth > 0 and tenth < 10:
            eleventh = run_all(test_string + last_one + str(tenth), 11)
            if eleventh > 0 and eleventh < 10:
                twelth = run_all(
                    test_string + last_one + str(tenth) + str(eleventh), 12
                )
                if twelth > 0 and twelth < 10:
                    thirteenth = run_all(
                        test_string
                        + last_one
                        + str(tenth)
                        + str(eleventh)
                        + str(twelth),
                        13,
                    )
                    if thirteenth > 0 and thirteenth < 10:
                        fourteenth = run_all(
                            test_string
                            + last_one
                            + str(tenth)
                            + str(eleventh)
                            + str(twelth)
                            + str(thirteenth),
                            14,
                        )
                        if fourteenth > 0 and fourteenth < 10:
                            answer = (
                                test_string
                                + last_one
                                + str(tenth)
                                + str(eleventh)
                                + str(twelth)
                                + str(thirteenth)
                                + str(fourteenth)
                            )
                            if not pt1:
                                pt1 = answer
        if last_one == "1":
            last_one = "9"
            if next_two == "11":
                next_two == "99"
                first_four = safe_decrement(first_four)
                if first_four == -1:
                    finished = True
            else:
                next_two = safe_decrement(next_two)
            break
        last_one = safe_decrement(last_one)

pt2 = answer

# Test model numbers against naive solution
with open("2021/res/in24.txt") as file:
    lines = file.read().split("\n")

insts = [line.split(" ") for line in lines]
test_valid(insts, pt1)
test_valid(insts, pt2)

print("Part 1: " + pt1)
print("Part 2: " + pt2)
