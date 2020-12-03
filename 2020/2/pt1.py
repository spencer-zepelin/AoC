def main():
    file = open("in.txt")
    passwords = file.read().splitlines()[:-1]
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
    print(ctr)


if __name__ == "__main__":
    main()
