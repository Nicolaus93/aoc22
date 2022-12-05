# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit


@timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=3)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    priorities = 0
    for line in data:
        line = line.strip()
        length = len(line)
        first_half = line[: length // 2]
        second_half = line[length // 2 :]
        common = set(first_half).intersection(second_half)
        for i in common:
            if i.islower():
                priorities += ord(i) - 96
            else:
                priorities += ord(i) - 38
    return priorities


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("part1: ", res)

    # real puzzle
    print("--------------PART-1--------------")
    res = solve()
    print(res)
