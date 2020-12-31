with open("2020/res/in07.txt") as file:
    rules = file.read().split("\n")

# Build Graphs
contained = {}
inverse = {}
for rule in rules:
    outer, inners = rule.split(" bags contain ")
    inners = inners.split(", ")
    iCurr = inverse.get(outer, [])
    for inner in inners:
        if inner[0].isdigit():
            num, *inner = inner.split(" ")
            num = int(num)
            inner = " ".join(inner[:2])  # modifier, color
            current = contained.get(inner, set())
            current.add(outer)
            contained[inner] = current
            iCurr.append((inner, num))
    inverse[outer] = iCurr

# BFS
visited = set()
queue = ["shiny gold"]
while len(queue) > 0:
    current = queue.pop(0)  # deque would be more performant than array
    for neighbor in contained.get(current, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# Could memoize recursion for performance improvement
def nest(color, graph):
    total = 0
    for bag in graph.get(color, []):
        total += bag[1] * (1 + nest(bag[0], graph))
    return total


print("Part 1: ", len(visited))
print("Part 2: ", nest("shiny gold", inverse))
