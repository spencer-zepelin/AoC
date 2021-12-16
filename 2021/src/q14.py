def get_score(pair_dict):
    char_count = {}
    for key, count in pair_dict.items():
        l_char, r_char = key
        l_val = char_count.get(l_char, 0)
        char_count[l_char] = l_val + count
        r_val = char_count.get(r_char, 0)
        char_count[r_char] = r_val + count
    # every letter counted twice except for first and last
    char_count[start[0]] += 1
    char_count[start[-1]] += 1
    return (max(char_count.values()) - min(char_count.values())) // 2


with open("2021/res/in14.txt") as file:
    start, str_rules = file.read().split("\n\n")

rules = [rule.split(" -> ") for rule in str_rules.split("\n")]
rules_memo = {k: v for k, v in rules}

poly_memo = {}
for i in range(len(start) - 1):
    key = start[i : (i + 2)]
    val = poly_memo.get(key, 0)
    poly_memo[key] = val + 1

pt1 = 0
pt2 = 0
pt1_steps = 10
steps = 40
curr_memo = poly_memo
for step in range(steps):
    if step == pt1_steps:
        pt1 = get_score(curr_memo)
    new_memo = {}
    for pair, count in curr_memo.items():
        insert = rules_memo[pair]
        left_key = pair[0] + insert
        right_key = insert + pair[1]
        l_val = new_memo.get(left_key, 0)
        new_memo[left_key] = l_val + count
        r_val = new_memo.get(right_key, 0)
        new_memo[right_key] = r_val + count
    curr_memo = new_memo

pt2 = get_score(curr_memo)

print("Part 1: ", pt1)
print("Part 2: ", pt2)
