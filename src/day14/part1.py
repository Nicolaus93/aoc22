# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from pprint import pprint as pp
from aocd.models import Puzzle
import utils

EXTEND = 200


@dataclass(frozen=True)
class Point2d:
    x: int
    y: int


@dataclass
class Map2d:
    rocks: set[Point2d] = field(default_factory=set)
    sand: set[Point2d] = field(default_factory=set)

    def __repr__(self):
        occupied = self.rocks.union(self.sand)
        min_x = min(occupied, key=lambda p: p.x).x
        max_x = max(occupied, key=lambda p: p.x).x
        min_y = min(occupied, key=lambda p: p.y).y
        max_y = max(occupied, key=lambda p: p.y).y
        line = ""
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                if Point2d(i, j) in self.rocks:
                    line += "#"
                elif Point2d(i, j) in self.sand:
                    line += "o"
                else:
                    line += "."
            line += "\n"
        return line

    @property
    def occupied(self):
        return self.rocks.union(self.sand)


def sand_falling(map2d, max_step):
    row_sand = 0
    col_sand = 500
    occupied = map2d.occupied
    for step in range(max_step):
        step += 1
        down = Point2d(row_sand + 1, col_sand)
        diag_left = Point2d(row_sand + 1, col_sand - 1)
        diag_right = Point2d(row_sand + 1, col_sand + 1)
        if down not in occupied:
            row_sand += 1
            continue
        if diag_left not in occupied:
            row_sand += 1
            col_sand -= 1
            continue
        if diag_right not in occupied:
            row_sand += 1
            col_sand += 1
            continue
        break

    return Point2d(row_sand, col_sand)


def get_rocks(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=14)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()
    map2d = Map2d()
    for line in data:
        pts = line.split("->")
        pts2d = []
        for pnt in pts:
            y, x = [int(i) for i in pnt.split(",")]
            pts2d.append(Point2d(x, y))

        for p1, p2 in zip(pts2d, pts2d[1:]):
            map2d.rocks.add(p1)
            map2d.rocks.add(p2)
            if p1.x == p2.x:
                y1, y2 = sorted([p1.y, p2.y])
                for y in range(y1, y2):
                    map2d.rocks.add(Point2d(p1.x, y))
            elif p1.y == p2.y:
                x1, x2 = sorted([p1.x, p2.x])
                for x in range(x1, x2):
                    map2d.rocks.add(Point2d(x, p1.y))
            else:
                raise ValueError
    return map2d


@utils.timeit
def solve(input_f=None, debug=False):
    map2d = get_rocks(input_f)

    max_row = max(map2d.rocks, key=lambda p: p.x).x
    for step in range(1000):
        stopped_sand = sand_falling(map2d, max_step=max_row + 10)
        if stopped_sand.x > max_row:
            break
        map2d.sand.add(stopped_sand)

    if debug:
        pp(map2d)
    return step


@utils.timeit
def part_2(input_f=None, debug=False):
    map2d = get_rocks(input_f)
    max_row = max(map2d.rocks, key=lambda p: p.x).x + 2
    max_col = max(map2d.rocks, key=lambda p: p.y).y + EXTEND
    min_col = max(map2d.rocks, key=lambda p: p.y).y - EXTEND
    for i in range(min_col, max_col):
        map2d.rocks.add(Point2d(max_row, i))

    source = Point2d(0, 500)
    for step in range(100000):
        stopped_sand = sand_falling(map2d, max_step=max_row + 1)
        if stopped_sand == source:
            break
        map2d.sand.add(stopped_sand)

    if debug:
        pp(map2d)
    return step + 1


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PART 1--------------")
    res = solve()
    print("PART 1 answer", res)

    print("--------------PART 2--------------")
    res = part_2()
    print("PART 2 answer", res)
