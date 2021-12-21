# (SUM_OF_ROLLS, FREQUENCY_OF_SUM)
DIRAC_OUTCOMES = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def step(memo, p1turn):
    new_memo = {}
    games_won = 0
    for k, v in memo.items():
        for advance, uni_count in DIRAC_OUTCOMES:
            p1_space, p2_space, p1_score, p2_score = k
            if p1turn:
                p1_space = (p1_space + advance) % 10
                p1_score += p1_space + 1
            else:
                p2_space = (p2_space + advance) % 10
                p2_score += p2_space + 1
            new_key = p1_space, p2_space, p1_score, p2_score
            curr_count = new_memo.get(new_key, 0)
            new_val = curr_count + (v * uni_count)
            if p1_score >= 21 or p2_score >= 21:
                games_won += new_val
            else:
                new_memo[new_key] = new_val
    return new_memo, games_won


# Input trivial, hardcoded
p1_space = 2
p2_space = 6
p1 = 0
p2 = 0
p1turn = True
die_val = 0
rolls = 0
while p1 < 1000 and p2 < 1000:
    advance = ((die_val + 1) * 3) + 3
    die_val = (die_val + 3) % 100
    rolls += 3
    if p1turn:
        p1_space = (p1_space + advance) % 10
        p1 += p1_space + 1
    else:
        p2_space = (p2_space + advance) % 10
        p2 += p2_space + 1
    p1turn = not p1turn

pt1 = rolls * p1 if p1 < p2 else rolls * p2
print("Part 1: ", pt1)

# Input trivial, hardcoded
p1_init = 2
p2_init = 6
p1_games = 0
p2_games = 0
p1turn = True
memo = {(p1_init, p2_init, 0, 0): 1}
while len(memo) > 0:
    memo, games_won = step(memo, p1turn)
    if p1turn:
        p1_games += games_won
    else:
        p2_games += games_won
    p1turn = not p1turn

pt2 = max(p1_games, p2_games)
print("Part 2: ", pt2)
