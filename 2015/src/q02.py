with open("2015/res/in02.txt") as file:
    boxes = file.read().split('\n')

pt1 = 0
pt2 = 0
for box in boxes:
    w = int(box.split('x')[0])
    l = int(box.split('x')[1])
    h = int(box.split('x')[2])
    areas = [w * l, w * h, h * l]
    pt1 += sum(areas) * 2 + min(areas)
    half_perims = [w + l, w + h, h + l]
    pt2 += min(half_perims) * 2 + w * h * l

print("Part 1: ", pt1)
print("Part 2: ", pt2)
