# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=10)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    instructions = [0] * (len(data) * 2)
    cycle = 0
    for line in data:
        if line.startswith("noop"):
            cycle += 1
        elif line.startswith("addx"):
            cycle += 1
            addx = int(line.strip().split()[1])
            instructions[cycle] = addx
            cycle += 1

    instructions = [0] + instructions
    signal = 1 + sum(instructions[:20])
    sum_signal = 20 * signal
    for i in range(20, 220, 40):
        signal += sum(instructions[i : i + 40])
        # print(i + 40, signal)
        sum_signal += (i + 40) * signal

    return sum_signal


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
