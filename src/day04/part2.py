# -*- coding: utf-8 -*-

from aocd.models import Puzzle
from utils import timeit
import re


@timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=4)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    count = 0
    for pos, line in enumerate(data):
        sections = [int(i) for i in re.findall("[0-9]+", line)]
        first_section = {int(i) for i in range(sections[0], sections[1] + 1)}
        second_section = {int(i) for i in range(sections[2], sections[3] + 1)}
        if first_section & second_section:
            count += 1

    print(pos)
    return count


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("part1: ", res)

    # real puzzle
    print("--------------PART-1--------------")
    res = solve()
    print("res: ", res)
