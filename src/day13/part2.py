# -*- coding: utf-8 -*-
from dataclasses import dataclass
from aocd.models import Puzzle
import utils
from part1 import compare
from pprint import pprint as pp


@dataclass
class Packet:
    data: int | list[int]

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return not compare(self.data, other.data)


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=13)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    data.append("\n")
    processed_data = []
    for line in data:
        if line.strip():
            item = eval(line.strip())
            processed_data.append(Packet(item))

    two = Packet([[2]])
    six = Packet([[6]])
    processed_data.append(two)
    processed_data.append(six)
    processed_data = sorted(processed_data)
    ans = 1
    for pos, value in enumerate(processed_data):
        if value == two or value == six:
            ans *= pos + 1
    return ans


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    pp(res)
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
