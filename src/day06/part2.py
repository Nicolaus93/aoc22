# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=6)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    for line in data:
        for pos, value in enumerate(line):
            letters = set(i for i in line[pos : pos + 14])
            if len(letters) == 14:
                return pos + 14
    return -1


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
