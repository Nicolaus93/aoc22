# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit


@timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=1)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    processed_data = []
    cal = 0
    for line in data:
        if len(line.split()) > 0:
            cal += int(line.split()[0])
        else:
            processed_data.append(cal)
            cal = 0
    return sorted(processed_data, reverse=True)


if __name__ == "__main__":
    # test_puzzle
    print("--------------PART-1--------------")
    res = solve("test.txt")
    print("part1: ", res[0])
    print("part2: ", sum(res[:3]))

    # real puzzle
    print("--------------PART-2--------------")
    res = solve()
    print(res[0], sum(res[:3]))

