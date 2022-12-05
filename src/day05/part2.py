# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit
import re
from collections import defaultdict


@timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=5)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    stacks = defaultdict(list)
    for line in data:
        moves = []
        if line.startswith("move"):
            moves = [int(i) for i in re.findall("[0-9]+", line)]

        else:
            values = [line[i] for i in range(1, len(line), 4)]
            for pos, value in enumerate(values):
                if value.isalpha():
                    stacks[pos].append(value)

        if moves:
            how_much, from_col, to_col = moves
            from_col -= 1
            to_col -= 1
            to_move = stacks[from_col][:how_much]
            stacks[to_col] = to_move + stacks[to_col]
            stacks[from_col] = stacks[from_col][how_much:]

    result = ""
    for col in range(len(stacks)):
        result += stacks[col][0]
    return result


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("part1: ", res)

    # real puzzle
    print("--------------PART-1--------------")
    res = solve()
    print(res)
