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

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1


@dataclass
class Knot:
    head: Pos2d
    tail: Pos2d
    dirs = {
        "U": Pos2d.up,
        "D": Pos2d.down,
        "L": Pos2d.left,
        "R": Pos2d.right,
    }

    def dist(self):
        return self.head.dist(self.tail)

    def follow(self):
        head = self.head
        tail = self.tail
        distance = head.dist(tail)
        if distance >= 2:
            if tail.x != head.x and tail.y != head.y:
                if distance > 2:
                    if head.x < tail.x:
                        tail.left()
                    if head.y < tail.y:
                        tail.down()
                    if head.y > tail.y:
                        tail.up()
                    if head.x > tail.x:
                        tail.right()
            elif tail.x != head.x:
                if head.x > tail.x:
                    tail.x += 1
                else:
                    tail.x -= 1
            else:
                if head.y > tail.y:
                    tail.y += 1
                else:
                    tail.y -= 1


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=9)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    visited = dict()
    parts = [Pos2d(0, 0) for _ in range(10)]
    knots = [Knot(p1, p2) for p1, p2 in zip(parts, parts[1:])]
    tail = parts[-1]
    head = parts[0]
    for line in data:
        where, steps = line.strip().split()
        steps = int(steps)
        for i in range(steps):
            direction = Knot.dirs[where]
            direction(head)
            for knot in knots:
                knot.follow()

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
