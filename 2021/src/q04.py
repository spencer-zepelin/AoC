def nums_win(nums, called):
    for num in nums:
        if num not in called:
            return False
    return True


def board_won(board, called):
    # Check rows for win
    for row in board:
        if nums_win(row, called):
            return True
    # Check cols for win
    for i in range(len(board[0])):
        nums = [row[i] for row in board]
        if nums_win(nums, called):
            return True
    return False


def string_to_board(card):
    board = []
    for row in card.split('\n'):
        board.append([int(val) for val in row.split(' ')])
    return board


def print_score(board, called, number, part_num):
    sum = 0
    for row in board:
        for num in row:
            if num not in called:
                sum += num
    print(f'Part {part_num}: ', sum * number)


with open("2021/res/in04.txt") as file:
    bingo, *all_cards = file.read().replace('  ', ' ').replace('\n ', '\n').split("\n\n")

balls = [int(val) for val in bingo.split(',')]

cards = [card.split('\n') for card in all_cards]

winner_found = False
balls_called = set()
winning_boards = set()
for ball in balls:
    balls_called.add(ball)
    for card in all_cards:
        if card not in winning_boards:
            board = string_to_board(card)
            if board_won(board, balls_called):
                # Part 1 condition
                if not winner_found:
                    print_score(board, balls_called, ball, 1)
                    winner_found = True
                # Part 2 condition
                if len(winning_boards) == len(cards) - 1:
                    print_score(board, balls_called, ball, 2)
                    exit()
                winning_boards.add(card)
