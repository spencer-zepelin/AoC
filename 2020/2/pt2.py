def main():
    file = open("in.txt")
    passwords = file.read().splitlines()[:-1]
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
    print(ctr)


if __name__ == "__main__":
    main()
