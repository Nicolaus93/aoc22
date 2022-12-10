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
    sprite_pos = 1
    message = ""
    pixel = 0
    for cycle in range(1, 240):
        if pixel in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
            message += "█"
        else:
            message += " "
        sprite_pos += instructions[cycle]
        if cycle % 40 == 0:
            message += "\n"
            pixel = 0
        else:
            pixel += 1
    return message


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print(res)

    # real puzzle
    print()
    print("--------------PUZZLE--------------")
    res = solve()
    print(res)
