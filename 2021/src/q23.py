"""AoC 2021 Day 23 Solution

A product of foolishness and tenacity

Constants moved to the `helpers` folder for readability
"""

from collections import deque

from helpers.p23_helpers import *


def home1(board, position, marker):
    if marker != position[0]:
        return False
    if position[1] == "1" and board[marker + "2"] != marker:
        return False
    return True


def home2(board, position, marker):
    if marker != position[0]:
        return False
    if position[1] == "1" and (
        board[marker + "2"] != marker
        or board[marker + "3"] != marker
        or board[marker + "4"] != marker
    ):
        return False
    if position[1] == "2" and (
        board[marker + "3"] != marker or board[marker + "4"] != marker
    ):
        return False
    if position[1] == "3" and board[marker + "4"] != marker:
        return False
    return True


def clear_path(board, hall, room, curr):
    move = f"{hall}-{room}"
    _, spaces = DIST_MAP[move]
    start = hall if curr == hall else room
    for space in spaces:
        if space != start and board[space]:
            return False
    return True


def all_valid_moves1(board, home_func, bases):
    valid_moves = []
    for pos, marker in board.items():
        if marker:
            if pos in bases and not home_func(board, pos, marker):
                for hall in HALLS:
                    if clear_path(board, hall, pos, pos):
                        valid_moves.append((f"{hall}-{pos}", marker))
            if pos in HALLS:
                if not board[f"{marker}2"] and clear_path(
                    board, pos, f"{marker}2", pos
                ):
                    valid_moves.append((f"{pos}-{marker}2", marker))
                if (
                    board[f"{marker}2"] == marker
                    and not board[f"{marker}1"]
                    and clear_path(board, pos, f"{marker}1", pos)
                ):
                    valid_moves.append((f"{pos}-{marker}1", marker))
    return valid_moves


def all_valid_moves2(board, home_func, bases):
    valid_moves = []
    for pos, marker in board.items():
        if marker:
            if pos in bases and not home_func(board, pos, marker):
                for hall in HALLS:
                    if clear_path(board, hall, pos, pos):
                        valid_moves.append((f"{hall}-{pos}", marker))
            if pos in HALLS:
                if not board[f"{marker}4"] and clear_path(
                    board, pos, f"{marker}4", pos
                ):
                    valid_moves.append((f"{pos}-{marker}4", marker))
                if (
                    board[f"{marker}4"] == marker
                    and not board[f"{marker}3"]
                    and clear_path(board, pos, f"{marker}3", pos)
                ):
                    valid_moves.append((f"{pos}-{marker}3", marker))
                if (
                    board[f"{marker}4"] == marker
                    and board[f"{marker}3"] == marker
                    and not board[f"{marker}2"]
                    and clear_path(board, pos, f"{marker}2", pos)
                ):
                    valid_moves.append((f"{pos}-{marker}2", marker))
                if (
                    board[f"{marker}4"] == marker
                    and board[f"{marker}3"] == marker
                    and board[f"{marker}2"] == marker
                    and not board[f"{marker}1"]
                    and clear_path(board, pos, f"{marker}1", pos)
                ):
                    valid_moves.append((f"{pos}-{marker}1", marker))
    return valid_moves


def key_to_board(board_key, positions):
    out_board = {}
    for pos, mark in zip(positions, board_key):
        out_board[pos] = mark if mark != "-" else None
    return out_board


def board_to_key(board, positions):
    out_string = ""
    for pos in positions:
        marker = board[pos]
        if marker:
            out_string += marker
        else:
            out_string += "-"
    return out_string


def get_edges(board_key, part):
    positions = POSITIONS1 if part == 1 else POSITIONS2
    bases = BASES1 if part == 1 else BASES2
    home_func = home1 if part == 1 else home2
    all_valid_moves_func = all_valid_moves1 if part == 1 else all_valid_moves2

    board = key_to_board(board_key, positions)
    valid_moves = all_valid_moves_func(board, home_func, bases)
    edges = []
    for valid_move, marker in valid_moves:
        new_board = board.copy()
        hall, room = valid_move.split("-")
        if not new_board[hall]:
            new_board[hall] = new_board[room]
            new_board[room] = None
        else:  # not new_board[room]
            new_board[room] = new_board[hall]
            new_board[hall] = None
        new_key = board_to_key(new_board, positions)
        weight = DIST_MAP[valid_move][0] * ENERGY[marker]
        edges.append((new_key, weight))
    return edges


class Game:
    def __init__(self, initial_board_key, winning_key, part=1):
        self.nodes = {}
        self.distances = {}
        self.queue = deque()
        self.added = set()
        self.winning_key = winning_key

        print("Creating board")
        self.queue.append(initial_board_key)
        ctr = 0
        while len(self.queue) > 0:
            ctr = (ctr + 1) % 10000
            if ctr == 0:
                print(len(self.queue))
            curr_key = self.queue.popleft()
            if curr_key != winning_key:
                edges = get_edges(curr_key, part)
                self.nodes[curr_key] = edges
                for edge_key, _edge_weight in edges:
                    if edge_key == winning_key:
                        print("winning key edge found")
                    if edge_key not in self.added:
                        self.added.add(edge_key)
                        self.queue.append(edge_key)
        self.nodes[winning_key] = []

        print("Calculating distances")
        self.seen = set()
        self.distances[initial_board_key] = 0
        ctr = 0
        while len(self.seen) < len(self.nodes):
            ctr = (ctr + 1) % 1000
            if ctr == 0:
                print(len(self.seen), " out of ", len(self.nodes))
            curr_key, curr_dist = self.get_min_dist()
            self.seen.add(curr_key)
            edges = self.nodes[curr_key]
            for edge_key, edge_weight in edges:
                old_dist = self.distances.get(edge_key, -1)
                new_dist = curr_dist + edge_weight
                if old_dist == -1 or new_dist < old_dist:
                    self.distances[edge_key] = new_dist

    def get_min_dist(self):
        min_key = None
        min_dist = -1
        for key, dist in self.distances.items():
            if key not in self.seen and (min_dist == -1 or dist < min_dist):
                min_dist = dist
                min_key = key
        return (min_key, min_dist)


initial_board_key1 = "-------cbaadbdc"
winning_key1 = "-------aabbccdd"

initial_board_key2 = "-------cddbacbadbabdacc"
winning_key2 = "-------aaaabbbbccccdddd"

g1 = Game(initial_board_key1, winning_key1)
pt1 = g1.distances[winning_key1]
print("Part 1: ", pt1)

g2 = Game(initial_board_key2, winning_key2, 2)
pt2 = g2.distances[winning_key2]
print("Part 1: ", pt1)
print("Part 2: ", pt2)
