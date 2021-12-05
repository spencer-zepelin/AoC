with open("2021/res/in05.txt") as file:
    lines = file.read().split("\n")

coords = [line.split(' -> ') for line in lines]

memo = {}
danger_spots = 0
memo2 = {}
danger_spots2 = 0
for coord in coords:
    coords1 = coord[0].split(',')
    x1 = int(coords1[0])
    y1 = int(coords1[1])
    coords2 = coord[1].split(',')
    x2 = int(coords2[0])
    y2 = int(coords2[1])
    # Handle diagonals
    if x1 != x2 and y1 != y2:
        x_sign = 1 if x2 >= x1 else -1
        y_sign = 1 if y2 >= y1 else -1
        diff = abs(x1 - x2)
        for delta in range(diff + 1):
            x = x1 + (delta * x_sign)
            y = y1 + (delta * y_sign)
            key = f'{x}-{y}'
            val = memo2.get(key, 0)
            if val == 1:
                danger_spots2 += 1
            memo2[key] = val + 1
    # Handle straight lines
    else:
        x_small, x_big = (x1, x2) if x1 <= x2 else (x2, x1)
        y_small, y_big = (y1, y2) if y1 <= y2 else (y2, y1)
        for x in range(x_small, x_big + 1):
            for y in range(y_small, y_big + 1):
                key = f'{x}-{y}'
                val = memo.get(key, 0)
                if val == 1:
                    danger_spots += 1
                memo[key] = val + 1
                val2 = memo2.get(key, 0)
                if val2 == 1:
                    danger_spots2 += 1
                memo2[key] = val2 + 1

print("Part 1: ", danger_spots)
print("Part 2: ", danger_spots2)
