# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit

SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
RELATION = {"A": "X", "B": "Y", "C": "Z"}


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
        second = line.split()[1]
        tot_score += SCORES[second]
        if RELATION[first] == second:
            tot_score += 3
        elif first == "A":
            if second == "Y":
                tot_score += 6
        elif first == "B":
            if second == "Z":
                tot_score += 6
        elif first == "C":
            if second == "X":
                tot_score += 6
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
