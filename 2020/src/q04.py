import re

with open("2020/res/in04.txt") as file:
    passports = file.read().split("\n\n")


def heightValidator(hgtStr):
    if "cm" in hgtStr:
        val = int(hgtStr[:-2])
        return True if val >= 150 and val <= 193 else False
    elif "in" in hgtStr:
        val = int(hgtStr[:-2])
        return True if val >= 59 and val <= 76 else False
    return False


def isValid(key, value):
    EYE_CODES = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    validators = {
        "byr": lambda val: True if int(val) >= 1920 and int(val) <= 2002 else False,
        "iyr": lambda val: True if int(val) >= 2010 and int(val) <= 2020 else False,
        "eyr": lambda val: True if int(val) >= 2020 and int(val) <= 2030 else False,
        "hgt": heightValidator,
        "hcl": lambda val: True
        if len(val) == 7 and re.match("#[0-9a-f]{6}", val)
        else False,
        "ecl": lambda val: True if value in EYE_CODES else False,
        "pid": lambda val: True if len(value) == 9 and value.isdigit() else False,
    }
    if key in validators:
        return validators[key](value)
    return False


valid1 = valid2 = 0
for passport in passports:
    stillNeeded1 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    stillNeeded2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    pairs = re.split(" |\n", passport)
    for pair in pairs:
        if ":" in pair:
            key, value = pair.split(":")
            stillNeeded1.discard(key)
            if isValid(key, value):
                stillNeeded2.discard(key)
    if len(stillNeeded1) == 0:
        valid1 += 1
    if len(stillNeeded2) == 0:
        valid2 += 1

print("Part 1: ", valid1)
print("Part 2: ", valid2)
