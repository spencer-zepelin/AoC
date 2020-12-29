with open("2020/5/in.txt") as file:
    tickets = file.read().split("\n")


highest = 0
seatsRemaining = set(range(0, (127 * 8 + 7)))
for ticket in tickets:
    row = col = 0
    rowPlace, colPlace = 64, 4
    for char in ticket:
        if char in "BF":
            if char == "B":
                row += rowPlace
            rowPlace /= 2
        else:
            if char == "R":
                col += colPlace
            colPlace /= 2
    seatId = int(row * 8 + col)
    seatsRemaining.discard(seatId)
    if seatId > highest:
        highest = seatId

print("Part 1: ", highest)


falseSeats = set()
for seat in seatsRemaining:
    if seat - 1 in seatsRemaining or seat + 1 in seatsRemaining:
        falseSeats.add(seat)

seatsRemaining.difference_update(falseSeats)

print("Part 2: ", seatsRemaining)
