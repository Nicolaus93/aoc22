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
    common = set()
    for pos, line in enumerate(data):
        line = line.strip()
        if pos % 3 == 0:
            if len(common) > 1:
                print(common)
                raise ValueError
            for i in common:
                if i.islower():
                    priorities += ord(i) - 96
                else:
                    priorities += ord(i) - 38
            common = set(i for i in line)
        else:
            common = common & set(i for i in line)

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
