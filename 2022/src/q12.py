from collections import deque

with open("2022/res/in12.txt") as file:
    rows = file.read().split("\n")


def find_letter(rows, letter):
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == letter:
                return (i, j)


def valid_adjacent(node, rows):
    max_row = len(rows) - 1
    max_col = len(rows[0]) - 1

    row, col = node
    valid = []
    if row + 1 <= max_row:
        valid.append((row + 1, col))
    if col + 1 <= max_col:
        valid.append((row, col + 1))
    if row - 1 >= 0:
        valid.append((row - 1, col))
    if col - 1 >= 0:
        valid.append((row, col - 1))
    return valid


def get_adjacent_inverse(node, rows):
    valid = valid_adjacent(node, rows)

    row, col = node
    elev = rows[row][col]
    out = []
    for r, c in valid:
        char = rows[r][c]
        if char in "yz" and elev == "E":
            out.append((r, c))
        elif elev in "ab" and char == "S":
            out.append((r, c))
        elif ord(char) - ord(elev) >= -1:
            out.append((r, c))
    return out


def pathfinder_2e(graph, start_node, search_node):
    q = deque()
    visited = set()

    visited.add(start_node)
    q.append((start_node, 0))

    shortest = len(graph) * len(graph[0])
    while len(q) > 0:
        n, dist = q.popleft()
        neighbors = get_adjacent_inverse(n, graph)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, dist + 1))
                r, c = neighbor
                if graph[r][c] == search_node and dist + 1 < shortest:
                    shortest = dist + 1
    return shortest


e = find_letter(rows, "E")
pt1 = pathfinder_2e(rows, e, "S")
pt2 = pathfinder_2e(rows, e, "a")
print("Part 1: ", pt1)
print("Part 2: ", pt2)
