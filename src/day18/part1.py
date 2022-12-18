# -*- coding: utf-8 -*-

from dataclasses import dataclass
from aocd.models import Puzzle
import utils


@dataclass(frozen=True)
class Face:
    min_xyz: tuple[int, int, int]
    max_xyz: tuple[int, int, int]


def surface_area(voxels: set[tuple[int, int, int]]):
    faces: set[Face] = set()
    covered: set[Face] = set()
    for vox in voxels:
        x, y, z = vox
        for offset_min, offset_max in (
            [(0, 0, 0), (1, 1, 0)],  # front
            [(0, 0, 1), (1, 1, 1)],  # back
            [(0, 0, 0), (0, 1, 1)],  # left
            [(1, 0, 0), (1, 1, 1)],  # right
            [(0, 1, 0), (1, 1, 1)],  # up
            [(0, 0, 0), (1, 0, 1)],  # down
        ):
            pnts = [
                tuple((x + off_x, y + off_y, z + off_z))
                for off_x, off_y, off_z in (offset_min, offset_max)
            ]
            face = Face(*pnts)
            if face in faces:
                covered.add(face)
            faces.add(face)

    return len(faces) - len(covered)


@utils.timeit
def solve(input_f=None):
    if not input_f:
        puzzle = Puzzle(year=2022, day=18)
        data = puzzle.input_data.split("\n")
    else:
        data = open(input_f).readlines()

    voxels = {tuple(utils.read_ints(line)) for line in data}
    return surface_area(voxels)


if __name__ == "__main__":
    # test_puzzle
    print("--------------TEST--------------")
    res = solve("test.txt")
    print("test answer: ", res)

    # real puzzle
    print("--------------PUZZLE--------------")
    res = solve()
    print("puzzle answer", res)
