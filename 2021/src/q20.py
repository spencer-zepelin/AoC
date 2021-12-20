def get_pixel_val(grid, code_string, row, col, step_num):
    w = len(grid[0])
    h = len(grid)
    bin_string = ""
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r < 0 or r >= h or c < 0 or c >= w:
                # Infinite background flips each step
                # since code[0] == "#" and code[-1] == "."
                bin_string += "0" if step_num % 2 == 0 else "1"
            else:
                bin_string += grid[r][c]
    idx = int(bin_string, 2)
    return code_string[idx]


def enhance(grid, code_string, step_num):
    w = len(grid[0])
    h = len(grid)
    new_grid = [["0" for _char in range(w)] for _row in range(h)]
    for row in range(w):
        for col in range(h):
            new_grid[row][col] = get_pixel_val(grid, code_string, row, col, step_num)
    return new_grid


with open("2021/res/in20.txt") as file:
    encoding, str_image = file.read().split("\n\n")

encoding = encoding.replace(".", "0").replace("#", "1")

init_image = str_image.split("\n")

w = len(init_image[0])
h = len(init_image)

# This could be abstracted to increase size on each step
image1 = [["0" for _char in range(w + 4)] for _row in range(h + 4)]
image2 = [["0" for _char in range(w + 100)] for _row in range(h + 100)]

for i, row in enumerate(init_image):
    for j, char in enumerate(row):
        if char == "#":
            image1[i + 2][j + 2] = "1"
            image2[i + 50][j + 50] = "1"

for step in range(2):
    image1 = enhance(image1, encoding, step)

for step in range(50):
    image2 = enhance(image2, encoding, step)

pt1 = 0
for row in image1:
    for char in row:
        if char == "1":
            pt1 += 1

pt2 = 0
for row in image2:
    for char in row:
        if char == "1":
            pt2 += 1

print("Part 1: ", pt1)
print("Part 2: ", pt2)
