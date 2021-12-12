def visit(node, visited, adj_list):
    if node == 'end':
        return 1
    paths = 0
    new_visited = visited.copy()
    if not node.isupper():
        new_visited.append(node)
    for adj in adj_list[node]:
        if adj not in new_visited:
            paths += visit(adj, new_visited, adj_list)
    return paths


def visit2(node, visited, adj_list, double_done):
    if node == 'end':
        return 1
    paths = 0
    new_visited = visited.copy()
    if not node.isupper() and node not in new_visited:
        new_visited.append(node)
    for adj in adj_list[node]:
        if adj in new_visited and not double_done and adj != 'start':
            paths += visit2(adj, new_visited, adj_list, True)
        elif adj not in new_visited:
            paths += visit2(adj, new_visited, adj_list, double_done)
    return paths


with open("2021/res/in12.txt") as file:
    edges = file.read().split("\n")

adj_list = {}
for edge in edges:
    n1, n2 = edge.split('-')
    n1_list = adj_list.get(n1, [])
    n2_list = adj_list.get(n2, [])
    n1_list.append(n2)
    n2_list.append(n1)
    adj_list[n1] = n1_list
    adj_list[n2] = n2_list

node = 'start'
visited = []
pt1 = visit(node, visited, adj_list)
pt2 = visit2(node, visited, adj_list, False)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
