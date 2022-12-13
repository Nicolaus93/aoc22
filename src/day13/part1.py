# -*- coding: utf-8 -*-

from aocd.models import Puzzle
import utils


def compare(first, second, debug=False):
    if debug:
        print(first, "vs", second)
    if isinstance(second, int) and isinstance(first, int):
        if first == second:
            return None
        return first < second
    if isinstance(first, int):
        first = [first]
    if isinstance(second, int):
        second = [second]

    for i, j in zip(first, second):
        # now both lists
        is_valid = compare(i, j)
        if is_valid is not None:
            return is_valid

    if len(first) < len(second):
        return True
    if len(first) > len(second):
        return False
    return None


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=13)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    data.append("\n")
    processed_data = []
    idx = 1
    res = 0
    for line in data:
        if line.strip():
            item = eval(line.strip())
            processed_data.append(item)
        else:
            is_right = compare(processed_data[0], processed_data[1])
            if is_right:
                res += idx
            idx += 1
            processed_data = []
    return res


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
