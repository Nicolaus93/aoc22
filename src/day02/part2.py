# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit

SCORES = {
    "A": 1,
    "B": 2,
    "C": 3,
}
WIN = {
    "A": "B",
    "B": "C",
    "C": "A",
}
LOSE = {
    "A": "C",
    "B": "A",
    "C": "B",
}


@timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=2)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    tot_score = 0
    for line in data:
        first = line.split()[0]
        strategy = line.split()[1]
        if strategy == "X":
            # lose
            tot_score += SCORES[LOSE[first]]
        elif strategy == "Y":
            # draw
            tot_score += 3
            tot_score += SCORES[first]
        elif strategy == "Z":
            # win
            tot_score += 6
            tot_score += SCORES[WIN[first]]

    return tot_score


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test: ", res)

    # real puzzle
    print("--------------PART-1--------------")
    res = solve()
    print("part1: ", res)
