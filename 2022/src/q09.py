with open("2022/res/in09.txt") as file:
    ops = file.read().split("\n")

dirs = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}


def follow(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail
    if head_x > tail_x:
        tail_x += 1
    elif head_x < tail_x:
        tail_x -= 1
    if head_y > tail_y:
        tail_y += 1
    elif head_y < tail_y:
        tail_y -= 1
    return (tail_x, tail_y)


h = (0, 0)
t = (0, 0)
knots = [(0, 0) for _ in range(10)]

visited = set()
visited.add((0, 0))
visited2 = set()
visited.add((0, 0))

for op in ops:
    d, num = op.split()
    x_delt, y_delt = dirs[d]
    for i in range(int(num)):
        h_x, h_y = h
        h = (h_x + x_delt, h_y + y_delt)
        t = follow(h, t)
        visited.add(t)

        h_x, h_y = knots[0]
        knots[0] = (h_x + x_delt, h_y + y_delt)
        for i in range(1, len(knots)):
            knots[i] = follow(knots[i - 1], knots[i])
            if i == (len(knots) - 1):
                visited2.add(knots[i])

pt1 = len(visited)
pt2 = len(visited2)
print("Part 1: ", pt1)
print("Part 2: ", pt2)
