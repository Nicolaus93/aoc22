# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils
import numpy as np
from pprint import pprint


@utils.timeit
def solve(input_f=None, debug=False):
    if not input_f:
        puzzle = Puzzle(year=2022, day=8)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    processed_data = []
    for line in data:
        processed_data.append([int(i) for row in line.split() for i in row])
    if debug:
        pprint(processed_data)
    processed_data = np.array(processed_data)

    # right
    right = np.zeros_like(processed_data, dtype=bool)
    for i in range(processed_data.shape[0]):
        max_n = -1
        for j in range(processed_data.shape[1]):
            if processed_data[i][j] > max_n:
                right[i][j] = True
                max_n = processed_data[i][j]

    left = np.zeros_like(processed_data, dtype=bool)
    for i in range(processed_data.shape[0]):
        max_n = -1
        for j in reversed(range(processed_data.shape[1])):
            if processed_data[i][j] > max_n:
                left[i][j] = True
                max_n = processed_data[i][j]

    up = np.zeros_like(processed_data, dtype=bool)
    for j in range(processed_data.shape[1]):
        max_n = -1
        for i in range(processed_data.shape[0]):
            if processed_data[i][j] > max_n:
                up[i][j] = True
                max_n = processed_data[i][j]

    down = np.zeros_like(processed_data, dtype=bool)
    for j in range(processed_data.shape[1]):
        max_n = -1
        for i in reversed(range(processed_data.shape[0])):
            if processed_data[i][j] > max_n:
                down[i][j] = True
                max_n = processed_data[i][j]

    res = right | left | down | up
    return res.sum()


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt", debug=True)
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
