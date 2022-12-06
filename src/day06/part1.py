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
        for pos, value in enumerate(zip(line, line[1:], line[2:], line[3:])):
            first, second, third, fourth = value
            letters = {first, second, third, fourth}
            if len(letters) == 4:
                return pos + 4
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
