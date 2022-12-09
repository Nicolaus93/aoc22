# -*- coding: utf-8 -*-

from dataclasses import dataclass
from aocd.models import Puzzle
import utils


@dataclass
class Pos2d:
    x: int
    y: int

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def up(pos2d):
    pos2d.y += 1


def down(pos2d):
    pos2d.y -= 1


def right(pos2d):
    pos2d.x += 1


def left(pos2d):
    pos2d.x -= 1


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=9)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    head = Pos2d(0, 0)
    tail = Pos2d(0, 0)
    dirs = {
        "U": up,
        "D": down,
        "L": left,
        "R": right,
    }
    visited = dict()
    for line in data:
        where, steps = line.strip().split()
        steps = int(steps)
        for i in range(steps):
            direction = dirs[where]
            direction(head)
            if tail.dist(head) >= 2:
                if tail.x != head.x and tail.y != head.y:
                    if tail.dist(head) > 2:
                        if head.x < tail.x:
                            left(tail)
                        if head.y < tail.y:
                            down(tail)
                        if head.y > tail.y:
                            up(tail)
                        if head.x > tail.x:
                            right(tail)
                else:
                    direction(tail)
            visited[(tail.x, tail.y)] = None
    print(visited.keys())
    return len(visited)


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
