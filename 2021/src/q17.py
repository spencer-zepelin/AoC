def check_hit(x_speed, y_speed, x_borders, y_borders):
    x_min, x_max = x_borders
    y_min, y_max = y_borders
    x_pos = 0
    y_pos = 0

    step = 0
    hit = False
    missed = False
    top_y = -1
    while not hit and not missed:
        step += 1
        x_pos += x_speed
        y_pos += y_speed
        if y_pos > top_y:
            top_y = y_pos
        if x_speed > 0:
            x_speed -= 1
        y_speed -= 1

        if x_pos >= x_min and x_pos <= x_max and y_pos >= y_min and y_pos <= y_max:
            hit = True
        elif x_pos > x_max or y_pos < y_min:
            missed = True

    if hit:
        return (top_y, True)
    if missed:
        return (-1, False)


# target area: x=56..76, y=-162..-134
x_range = (56, 76)
y_range = (-162, -134)

pt1 = -1
pt2 = 0
# 11 is first triangular number that will reach x border
for x in range(11, x_range[1] + 1):
    for y in range(y_range[0] - 2, abs(y_range[0]) + 2):
        val, result = check_hit(x, y, x_range, y_range)
        if val > pt1:
            pt1 = val
        if result:
            pt2 += 1

print("Part 1: ", pt1)
print("Part 2: ", pt2)
