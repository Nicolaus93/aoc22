# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils
import numpy as np
from pprint import pprint


def check_neighbors(curr_i, curr_j, mat):
    max_i, max_j = mat.shape
    current = mat[curr_i][curr_j]

    right = 0
    for col in range(curr_j + 1, max_j):
        right += 1
        if mat[curr_i][col] >= current:
            break

    left = 0
    for col in reversed(range(0, curr_j)):
        left += 1
        if mat[curr_i][col] >= current:
            break

    down = 0
    for row in range(curr_i + 1, max_i):
        down += 1
        if mat[row][curr_j] >= current:
            break

    up = 0
    for row in reversed(range(0, curr_i)):
        up += 1
        if mat[row][curr_j] >= current:
            break

    return right * left * down * up


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

    scores = np.zeros_like(processed_data, dtype=int)
    for i in range(processed_data.shape[0]):
        for j in range(processed_data.shape[1]):
            scores[i][j] = check_neighbors(i, j, processed_data)

    return scores.max()


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt", debug=True)
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
