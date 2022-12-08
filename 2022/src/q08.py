def visible(tree):
    h = tree["height"]
    return (
        1
        if h > tree["left"] or h > tree["right"] or h > tree["up"] or h > tree["down"]
        else 0
    )


with open("2022/res/in08.txt") as file:
    rows = file.read().split("\n")

forest = [[{"height": int(height)} for height in row] for row in rows]

ROW_NUM = len(forest)
COL_NUM = len(forest[0])

for row_idx in range(ROW_NUM):
    for col_idx in range(COL_NUM):
        tree = forest[row_idx][col_idx]
        if col_idx == 0:
            tree["left"] = -1
        else:
            left_tree = forest[row_idx][col_idx - 1]
            tree["left"] = max(left_tree["left"], left_tree["height"])
        if row_idx == 0:
            tree["up"] = -1
        else:
            up_tree = forest[row_idx - 1][col_idx]
            tree["up"] = max(up_tree["up"], up_tree["height"])

for row_idx in reversed(range(ROW_NUM)):
    for col_idx in reversed(range(COL_NUM)):
        tree = forest[row_idx][col_idx]
        if row_idx == (ROW_NUM - 1):
            tree["down"] = -1
        else:
            down_tree = forest[row_idx + 1][col_idx]
            tree["down"] = max(down_tree["down"], down_tree["height"])
        if col_idx == (COL_NUM - 1):
            tree["right"] = -1
        else:
            right_tree = forest[row_idx][col_idx + 1]
            tree["right"] = max(right_tree["right"], right_tree["height"])

pt1 = 0
for row_idx in range(ROW_NUM):
    for col_idx in range(COL_NUM):
        tree = forest[row_idx][col_idx]
        pt1 += visible(tree)
print("Part 1: ", pt1)

for row_idx in range(ROW_NUM):
    for col_idx in range(COL_NUM):
        tree = forest[row_idx][col_idx]
        if col_idx == 0:
            tree["left"] = 0
            tree["l_memo"] = {tree["height"]: col_idx}
        else:
            memo = forest[row_idx][col_idx - 1]["l_memo"]
            closest_taller = 0
            for h in range(tree["height"], 10):
                if h in memo:
                    idx = memo[h]
                    if idx > closest_taller:
                        closest_taller = idx

            tree["left"] = col_idx - closest_taller
            memo[tree["height"]] = col_idx
            tree["l_memo"] = memo

        if row_idx == 0:
            tree["up"] = 0
            tree["u_memo"] = {tree["height"]: row_idx}
        else:
            memo = forest[row_idx - 1][col_idx]["u_memo"]
            closest_taller = 0
            for h in range(tree["height"], 10):
                if h in memo:
                    idx = memo[h]
                    if idx > closest_taller:
                        closest_taller = idx

            tree["up"] = row_idx - closest_taller
            memo[tree["height"]] = row_idx
            tree["u_memo"] = memo

for row_idx in reversed(range(ROW_NUM)):
    for col_idx in reversed(range(COL_NUM)):
        tree = forest[row_idx][col_idx]

        if col_idx == (COL_NUM - 1):
            tree["right"] = 0
            tree["r_memo"] = {tree["height"]: col_idx}
        else:
            memo = forest[row_idx][col_idx + 1]["r_memo"]
            closest_taller = COL_NUM - 1
            for h in range(tree["height"], 10):
                if h in memo:
                    idx = memo[h]
                    if idx < closest_taller:
                        closest_taller = idx

            tree["right"] = closest_taller - col_idx
            memo[tree["height"]] = col_idx
            tree["r_memo"] = memo

        if row_idx == (ROW_NUM - 1):
            tree["down"] = 0
            tree["d_memo"] = {tree["height"]: row_idx}
        else:
            memo = forest[row_idx + 1][col_idx]["d_memo"]
            closest_taller = ROW_NUM - 1
            for h in range(tree["height"], 10):
                if h in memo:
                    idx = memo[h]
                    if idx < closest_taller:
                        closest_taller = idx

            tree["down"] = closest_taller - row_idx
            memo[tree["height"]] = row_idx
            tree["d_memo"] = memo

pt2 = 0
for row_idx in range(ROW_NUM):
    for col_idx in range(COL_NUM):
        tree = forest[row_idx][col_idx]
        view = tree["left"] * tree["right"] * tree["up"] * tree["down"]
        if view > pt2:
            pt2 = view

print("Part 2: ", pt2)
